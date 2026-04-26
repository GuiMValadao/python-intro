import config
import numpy as np
import pygame

from entities import Staff, MovingBlock, KeyChangeMarker
from songs import SONGS


def load_sound(key_name, frequency, duration=0.7, sample_rate=22050):
    """
    Load a sound file for the given key, or generate it if file doesn't exist.
    Uses enharmonic equivalents for flat notes to save space.
    """
    actual_note_name = config.get_sound_file_name(key_name)
    sound_file = (
        config.ROOT_PATH / "sounds" / config.INSTRUMENT / f"note_{actual_note_name}.wav"
    )
    try:
        return pygame.mixer.Sound(str(sound_file))
    except (pygame.error, FileNotFoundError):
        return generate_sound(frequency, duration, sample_rate)


def generate_sound(frequency, duration=0.7, sample_rate=22050):
    """Generate a sine wave sound for a given frequency."""
    frames = int(duration * sample_rate)
    arr = np.sin(2.0 * np.pi * frequency * np.linspace(0, duration, frames))
    envelope = np.linspace(1.0, 0.0, frames)
    arr *= envelope
    arr = (arr * 32767).astype(np.int16)
    stereo = np.ascontiguousarray(np.column_stack((arr, arr)))
    return pygame.sndarray.make_sound(stereo)


def generate_distorted_sound(
    frequency, duration=0.5, sample_rate=22050, distortion_factor=0.5, volume=0.1
):
    """Generate a distorted sine wave sound for missed notes."""
    frames = int(duration * sample_rate)
    arr = np.sin(2.0 * np.pi * frequency * np.linspace(0, duration, frames))
    arr = np.clip(arr * (1 + distortion_factor), -1, 1)
    noise = np.random.normal(0, 0.1, frames)
    arr = arr + noise * distortion_factor
    arr = np.clip(arr, -1, 1)
    envelope = np.linspace(1.0, 0.0, frames)
    arr *= envelope
    arr *= volume
    arr = (arr * 32767).astype(np.int16)
    stereo = np.ascontiguousarray(np.column_stack((arr, arr)))
    return pygame.sndarray.make_sound(stereo)


def get_modifier_color_overlay(modifier):
    """
    Get a color overlay and symbol based on note modifier.

    Returns:
        tuple: (overlay_color, symbol_text) or None for natural notes
    """
    if modifier & config.SHARP_MODIFIER:
        return ((150, 150, 150), "#")
    elif modifier & config.FLAT_MODIFIER:
        return ((40, 40, 40), "b")
    else:
        return None


class BattleEvent:
    def __init__(self, game, npc=None):
        self.game = game
        self.staff = Staff(game)
        self.npc = npc
        self.moving_blocks = []
        self.key_change_markers = []  # visual-only markers travelling the screen
        self.spawn_timer = 0
        self.score = 0
        self.full_hits = 0
        self.half_hits = 0
        self.previous_keys = pygame.key.get_pressed()

        # Active key-change notification banner (Easy / Medium only)
        # {"key": str, "timer": int} or None
        self.key_change_banner = None

        self._load_all_sounds()

        self.button_states = {
            key: {"lit": False, "time": 0} for key in config.get_all_playable_keys()
        }

        # Load song and apply starting key signature
        raw_song = SONGS[config.CURRENT_SONG]
        config.CURRENT_KEY_SIGNATURE = raw_song["key_signature"]

        # Validate and process
        self._validate_song(raw_song["notes"], config.CURRENT_SONG)
        processed_notes = self.process_song_for_difficulty(raw_song["notes"])

        # Inject visual warning markers for Easy / Medium before actual key changes
        self.song = self._precompute_key_change_markers(processed_notes)

        self.song_index = 0
        self.song_finished = False

    # ------------------------------------------------------------------
    # Song loading helpers
    # ------------------------------------------------------------------

    def _validate_song(self, notes, song_name):
        """
        Raise ValueError if any chord contains notes with mixed modifier types.
        Key-change events are skipped.
        """
        for frame_time, event in notes:
            if isinstance(event, dict):
                continue  # key change event — not a note chord
            if len(event) > 1:
                modifiers = set()
                for note_key in event:
                    mod = note_key[1] if isinstance(note_key, tuple) else 0
                    modifiers.add(mod)
                if len(modifiers) > 1:
                    raise ValueError(
                        f"Song '{song_name}' has a mixed-modifier chord at frame "
                        f"{frame_time}. All notes in a chord must share the same "
                        f"modifier (all natural, all sharp, or all flat)."
                    )

    def _get_travel_frames(self):
        """
        How many frames a block takes to travel from spawn to the staff buttons.
        Mirrors the speed logic in MovingBlock so markers arrive in sync.
        """
        base_speed = 3
        if config.DIFFICULTY == "Easy":
            speed = base_speed * 0.7
        elif config.DIFFICULTY == "Hard":
            speed = base_speed
        else:
            speed = base_speed
        # Distance from right edge to the staff (approx button x position = 50)
        distance = config.DISPLAY_WIDTH - 50
        return int(distance / speed)

    def _precompute_key_change_markers(self, notes):
        """
        For Easy and Medium, insert visual warning events into the song timeline
        timed so that a KeyChangeMarker arrives at the staff exactly when the key
        actually changes.  Hard mode: no warnings injected.

        Visual warning events use the dict key "key_change_warning" to distinguish
        them from the real "key_change" events that mutate config.CURRENT_KEY_SIGNATURE.
        """
        if config.DIFFICULTY == "Hard":
            return notes

        travel_frames = self._get_travel_frames()
        warnings = []
        for frame_time, event in notes:
            if isinstance(event, dict) and "key_change" in event:
                warning_frame = max(0, frame_time - travel_frames)
                warnings.append(
                    (warning_frame, {"key_change_warning": event["key_change"]})
                )

        combined = notes + warnings
        combined.sort(key=lambda e: e[0])
        return combined

    def process_song_for_difficulty(self, notes):
        """Filter and adjust note timing based on current difficulty."""
        if not notes:
            return notes

        processed = []
        prev_frame = None

        for frame_time, event in notes:
            # Key change events always pass through unfiltered
            if isinstance(event, dict):
                processed.append((frame_time, event))
                continue

            include = True
            if config.DIFFICULTY == "Medium":
                if prev_frame is not None and (frame_time - prev_frame) < 30:
                    include = False
            elif config.DIFFICULTY == "Easy":
                if prev_frame is not None and (frame_time - prev_frame) < 50:
                    include = False

            if include:
                adjusted = (
                    int(frame_time * 0.8)
                    if (
                        config.DIFFICULTY == "Hard"
                        and (
                            (frame_time * 0.8 / frame_time) > config.SPAWN_MIN
                        )  # Stops notes close together from swarming each other
                    )
                    else frame_time
                )
                processed.append((adjusted, event))
                prev_frame = frame_time  # use original for spacing check

        return processed

    # ------------------------------------------------------------------
    # Sound loading
    # ------------------------------------------------------------------

    def _load_all_sounds(self):
        """Load natural, sharp, and flat sounds plus distorted miss sounds."""
        self.sounds = {}
        self.distorted_sounds = {}

        for key in config.get_all_playable_keys():
            note_name = config.NOTE_NAMES[key]
            for modifier, suffix in [
                (0, ""),
                (config.SHARP_MODIFIER, "#"),
                (config.FLAT_MODIFIER, "b"),
            ]:
                freq = config.get_note_frequency(key, modifier)
                if freq:
                    self.sounds[(key, modifier)] = load_sound(note_name + suffix, freq)
                    self.distorted_sounds[(key, modifier)] = generate_distorted_sound(
                        freq
                    )

    # ------------------------------------------------------------------
    # Note resolution
    # ------------------------------------------------------------------

    def _resolve_note_name(self, key, current_mods):
        """
        Resolve the actual note produced by a key press given the key signature.

        The key signature sets which buttons are altered by default.
        The modifier overrides the signature back to natural:
          - If key sig raises a note (e.g. F→F# in G major), Ctrl gives natural F
          - If key sig lowers a note (e.g. B→Bb in F major), Shift gives natural B
          - Notes outside the key sig behave exactly as before (Shift=sharp, Ctrl=flat)

        Returns:
            str: resolved note name (e.g. "F3", "F3#", "B2b")
        """
        key_sig = config.get_key_signature()
        note_name = config.NOTE_NAMES[key]  # e.g. "F3"

        if note_name in key_sig:
            altered = key_sig[note_name]  # e.g. "F3#"
            is_raised = altered.endswith("#")

            if is_raised and (current_mods & config.FLAT_MODIFIER):
                # Ctrl overrides a raised note back to natural
                return note_name
            elif not is_raised and (current_mods & config.SHARP_MODIFIER):
                # Shift overrides a lowered note back to natural
                return note_name
            else:
                return altered
        else:
            # Not in key signature — modifiers work as usual
            if current_mods & config.SHARP_MODIFIER:
                return note_name + "#"
            elif current_mods & config.FLAT_MODIFIER:
                return note_name + "b"
            else:
                return note_name

    def _note_name_to_sound_key(self, note_name, base_key):
        """Convert a resolved note name to the (key, modifier) tuple used in self.sounds."""
        if note_name.endswith("#"):
            return (base_key, config.SHARP_MODIFIER)
        elif note_name.endswith("b"):
            return (base_key, config.FLAT_MODIFIER)
        else:
            return (base_key, 0)

    # ------------------------------------------------------------------
    # Main update — sequenced passes
    # ------------------------------------------------------------------

    def update(self):
        current_keys = pygame.key.get_pressed()
        current_mods = pygame.key.get_mods()

        self._spawn_blocks()
        self._move_blocks()
        self._update_button_timers()
        self._update_indicators()
        self._evaluate_input(current_keys, current_mods)
        self._check_song_completion()

        self.previous_keys = current_keys

    # ------------------------------------------------------------------
    # Update submethods
    # ------------------------------------------------------------------

    def _spawn_blocks(self):
        """Advance spawn timer and emit blocks or key-change events on schedule."""
        self.spawn_timer += 1

        # Use while so same-frame events (e.g. warning + note) are all processed
        while (
            self.song_index < len(self.song)
            and self.spawn_timer >= self.song[self.song_index][0]
        ):
            frame_time, event = self.song[self.song_index]

            if isinstance(event, dict):
                if "key_change" in event:
                    self._trigger_key_change(event["key_change"])
                elif "key_change_warning" in event:
                    self._spawn_key_change_marker(event["key_change_warning"])
            else:
                # Regular note list (chord or single note)
                for note_key in event:
                    base_key = note_key[0] if isinstance(note_key, tuple) else note_key
                    target_button = next(
                        (b for b in self.staff.buttons if b.key == base_key), None
                    )
                    if target_button:
                        self.moving_blocks.append(
                            MovingBlock(self.game, target_button, note_key)
                        )

            self.song_index += 1

    def _trigger_key_change(self, new_key):
        """Apply a key signature change and show the notification banner."""
        config.CURRENT_KEY_SIGNATURE = new_key
        if config.DIFFICULTY != "Hard":
            self.key_change_banner = {
                "key": new_key,
                "timer": 180,  # 3 seconds at 60 fps
            }

    def _spawn_key_change_marker(self, incoming_key):
        """Spawn a visual marker that travels toward the staff as an advance warning."""
        self.key_change_markers.append(KeyChangeMarker(self.game, incoming_key))

    def _move_blocks(self):
        """Advance all moving objects and remove those that have passed the target."""
        for block in self.moving_blocks:
            block.update()
        self.moving_blocks = [b for b in self.moving_blocks if b.position.x >= 0]

        for marker in self.key_change_markers:
            marker.update()
        self.key_change_markers = [
            m for m in self.key_change_markers if m.position.x >= 0
        ]

    def _update_button_timers(self):
        """Tick down the lit-button highlight timers."""
        for state in self.button_states.values():
            if state["lit"]:
                state["time"] -= 1
                if state["time"] <= 0:
                    state["lit"] = False

    def _update_indicators(self):
        """Tick down the key-change notification banner timer."""
        if self.key_change_banner:
            self.key_change_banner["timer"] -= 1
            if self.key_change_banner["timer"] <= 0:
                self.key_change_banner = None

    def _evaluate_input(self, current_keys, current_mods):
        """Check all freshly pressed keys and route each to hit or miss handling."""
        for key in config.get_all_playable_keys():
            if current_keys[key] and not self.previous_keys[key]:
                self._handle_key_press(key, current_mods)
                # NPC reacts to the overall state after all input is processed
        if self.npc:
            self.npc.on_battle_update(self)

    def _handle_key_press(self, key, current_mods):
        """Resolve the note produced, then register a hit or miss."""
        resolved_note = self._resolve_note_name(key, current_mods)
        hit_block = self._find_hit_block(key, resolved_note)
        if hit_block:
            self._register_hit(hit_block)
        else:
            self._register_miss(key, resolved_note)

    def _find_hit_block(self, key, resolved_note):
        """
        Find the first colliding block whose note matches the resolved note name.
        Blocks store their original note_key; we resolve that too for comparison.
        """
        for block in self.moving_blocks:
            if block.target.key != key:
                continue
            if not block.is_colliding():
                continue
            # Resolve the block's note under the current key signature
            block_base = (
                block.note_key[0]
                if isinstance(block.note_key, tuple)
                else block.note_key
            )
            block_mod = block.note_key[1] if isinstance(block.note_key, tuple) else 0

            # Derive block's sounding note from key sig, treating stored modifier
            # as an explicit override already baked in at song-author time.
            # For blocks authored with explicit accidentals (tuple), use as-is.
            # For natural key blocks, apply signature resolution.
            if isinstance(block.note_key, tuple):
                # Explicit accidental authored in song data
                block_resolved = config.NOTE_NAMES[block_base]
                if block_mod & config.SHARP_MODIFIER:
                    block_resolved += "#"
                elif block_mod & config.FLAT_MODIFIER:
                    block_resolved += "b"
            else:
                # Natural key — apply current key signature
                key_sig = config.get_key_signature()
                natural_name = config.NOTE_NAMES[block_base]
                block_resolved = key_sig.get(natural_name, natural_name)

            if block_resolved == resolved_note:
                return block
        return None

    def _register_hit(self, block):
        """Award points, play the note sound, and light up the button."""
        precision = self.calculate_precision(block.rect(), block.target.rect())
        if precision >= 80.0:
            self.score += 1
            self.full_hits += 1
        else:
            self.score += 0.5
            self.half_hits += 1

        base_key = (
            block.note_key[0] if isinstance(block.note_key, tuple) else block.note_key
        )
        # Resolve the sound that should actually play
        key_sig = config.get_key_signature()
        natural_name = config.NOTE_NAMES[base_key]
        if isinstance(block.note_key, tuple):
            sound_key = (
                block.note_key
                if isinstance(block.note_key, tuple)
                else (block.note_key, 0)
            )
        else:
            sounding_name = key_sig.get(natural_name, natural_name)
            sound_key = self._note_name_to_sound_key(sounding_name, base_key)

        if sound_key in self.sounds:
            self.sounds[sound_key].play()

        self.button_states[base_key]["lit"] = True
        self.button_states[base_key]["time"] = 10
        self.moving_blocks.remove(block)

        # NPC on-hit note interference/interaction
        if self.npc:
            self.npc.on_player_hit(self)

    def _register_miss(self, key, resolved_note):
        """Play a distorted version of whatever note the player pressed."""
        sound_key = self._note_name_to_sound_key(resolved_note, key)
        if sound_key in self.distorted_sounds:
            self.distorted_sounds[sound_key].play()

        # NPC on-missed note interference/interaction
        if self.npc:
            self.npc.on_player_miss(self)

    def _check_song_completion(self):
        if self.song_index >= len(self.song) and len(self.moving_blocks) == 0:
            self.song_finished = True

    # ------------------------------------------------------------------
    # Precision calculation
    # ------------------------------------------------------------------

    def calculate_precision(self, rect1, rect2):
        intersection = rect1.clip(rect2)
        if intersection.width <= 0 or intersection.height <= 0:
            return 0.0
        intersection_area = intersection.width * intersection.height
        rect1_area = rect1.width * rect1.height
        if rect1_area == 0:
            return 0.0
        return min((intersection_area / rect1_area) * 100, 100.0)

    # ------------------------------------------------------------------
    # Drawing
    # ------------------------------------------------------------------

    def draw(self):
        self._draw_staff_and_buttons()
        self._draw_moving_objects()
        self._draw_key_signature_hud()
        self._draw_key_change_banner()

    def _draw_staff_and_buttons(self):
        """Draw the staff and all buttons, with highlight for lit buttons."""
        self.staff.draw()
        for button in self.staff.buttons:
            if self.button_states[button.key]["lit"]:
                self.game.display_surface.blit(
                    button.image, (button.position.x, button.position.y)
                )
                highlight = pygame.Surface(
                    (button.width, button.height), pygame.SRCALPHA
                )
                highlight.fill((255, 255, 255, 150))
                self.game.display_surface.blit(
                    highlight, (button.position.x, button.position.y)
                )
            else:
                # Show the altered note name on the button if key sig changes it
                button.draw()
                self._draw_button_note_label(button)

    def _draw_button_note_label(self, button):
        """
        On Easy, draw the current sounding note name on each button so players
        can see which notes have been altered by the key signature.
        """
        if config.DIFFICULTY != "Easy":
            return

        key_sig = config.get_key_signature()
        natural_name = config.NOTE_NAMES[button.key]
        sounding_name = key_sig.get(natural_name, natural_name)

        # Only label if the note has been altered (saves visual clutter)
        if sounding_name == natural_name:
            return

        font = pygame.font.SysFont(config.GAME_FONT, 14)
        label = font.render(sounding_name, True, (255, 255, 0))
        label_rect = label.get_rect(
            center=(
                button.position.x + button.width // 2,
                button.position.y - 10,
            )
        )
        self.game.display_surface.blit(label, label_rect)

    def _draw_moving_objects(self):
        """Draw all moving blocks and key-change warning markers."""
        for block in self.moving_blocks:
            block.draw()
        for marker in self.key_change_markers:
            marker.draw()

    def _draw_key_signature_hud(self):
        """
        Draw the current key signature in the top-right corner of the screen.
        Hidden on Hard mode.
        """
        if config.DIFFICULTY == "Hard":
            return

        display_name = config.KEY_SIGNATURE_DISPLAY.get(
            config.CURRENT_KEY_SIGNATURE, config.CURRENT_KEY_SIGNATURE
        )
        font = pygame.font.SysFont(config.GAME_FONT, 24)
        label = font.render(f"Key: {display_name}", True, (220, 220, 220))
        x = config.DISPLAY_WIDTH - label.get_width() - 20
        self.game.display_surface.blit(label, (x, 20))

    def _draw_key_change_banner(self):
        """
        Draw a temporary notification banner when the key signature changes.
        Easy: large, prominent, with altered notes listed.
        Medium: compact, just the new key name.
        Hard: nothing.
        """
        if not self.key_change_banner or config.DIFFICULTY == "Hard":
            return

        banner_key = self.key_change_banner["key"]
        timer = self.key_change_banner["timer"]
        display_name = config.KEY_SIGNATURE_DISPLAY.get(banner_key, banner_key)

        # Fade out over the last 60 frames (1 second)
        alpha = min(255, int((timer / 60) * 255)) if timer < 60 else 255

        cx = config.DISPLAY_WIDTH // 2
        cy = config.DISPLAY_HEIGHT // 3

        if config.DIFFICULTY == "Easy":
            # Large banner with altered notes listed
            title_font = pygame.font.SysFont(config.GAME_FONT, 42)
            detail_font = pygame.font.SysFont(config.GAME_FONT, 24)

            title_surf = title_font.render(f"Key: {display_name}", True, (255, 215, 0))
            title_surf.set_alpha(alpha)
            title_rect = title_surf.get_rect(center=(cx, cy))
            self.game.display_surface.blit(title_surf, title_rect)

            # List the altered notes
            key_sig = config.KEY_SIGNATURES.get(banner_key, {})
            if key_sig:
                changes = "  ".join(f"{nat}→{alt}" for nat, alt in key_sig.items())
                detail_surf = detail_font.render(changes, True, (255, 240, 180))
                detail_surf.set_alpha(alpha)
                detail_rect = detail_surf.get_rect(center=(cx, cy + 50))
                self.game.display_surface.blit(detail_surf, detail_rect)
            else:
                # C major / A minor — no alterations
                detail_surf = detail_font.render(
                    "No alterations", True, (200, 200, 200)
                )
                detail_surf.set_alpha(alpha)
                detail_rect = detail_surf.get_rect(center=(cx, cy + 50))
                self.game.display_surface.blit(detail_surf, detail_rect)

        elif config.DIFFICULTY == "Medium":
            # Compact banner — key name only
            font = pygame.font.SysFont(config.GAME_FONT, 32)
            surf = font.render(f"→ {display_name}", True, (255, 215, 0))
            surf.set_alpha(alpha)
            rect = surf.get_rect(center=(cx, cy))
            self.game.display_surface.blit(surf, rect)


class TalkEvent: ...
