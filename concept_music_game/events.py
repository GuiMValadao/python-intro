import pygame
import numpy as np
from entities import Staff, MovingBlock
import config
from songs import SONGS


def load_sound(key_name, frequency, duration=0.7, sample_rate=22050):
    """
    Load a sound file for the given key, or generate it if file doesn't exist.
    Uses enharmonic equivalents for flat notes to save space (e.g., Db uses C# file).
    """
    # Resolve enharmonic equivalents (e.g., "A2b" → "G3#")
    actual_note_name = config.get_sound_file_name(key_name)
    sound_file = config.ROOT_PATH / "sounds" / f"note_{actual_note_name}.wav"
    try:
        return pygame.mixer.Sound(str(sound_file))
    except (pygame.error, FileNotFoundError):
        # Fallback to generating the sound
        return generate_sound(frequency, duration, sample_rate)


def generate_sound(frequency, duration=0.7, sample_rate=22050):
    """Generate a sine wave sound for a given frequency."""
    frames = int(duration * sample_rate)
    arr = np.sin(2.0 * np.pi * frequency * np.linspace(0, duration, frames))
    # Apply envelope to avoid clicks
    envelope = np.linspace(1.0, 0.0, frames)
    arr *= envelope
    # Scale to int16 range and convert
    arr = (arr * 32767).astype(np.int16)
    # Create stereo sound (duplicate for both channels and ensure C-contiguous)
    stereo = np.ascontiguousarray(np.column_stack((arr, arr)))
    return pygame.sndarray.make_sound(stereo)


def generate_distorted_sound(
    frequency, duration=0.5, sample_rate=22050, distortion_factor=0.3, volume=0.3
):
    """Generate a distorted sine wave sound with lower volume for failure when hitting notes."""
    frames = int(duration * sample_rate)
    arr = np.sin(2.0 * np.pi * frequency * np.linspace(0, duration, frames))
    # Add distortion by clipping and adding noise
    arr = np.clip(arr * (1 + distortion_factor), -1, 1)
    noise = np.random.normal(0, 0.1, frames)
    arr = arr + noise * distortion_factor
    arr = np.clip(arr, -1, 1)
    # Apply envelope to avoid clicks
    envelope = np.linspace(1.0, 0.0, frames)
    arr *= envelope
    # Reduce volume for failed attempt
    arr *= volume
    # Scale to int16 range and convert
    arr = (arr * 32767).astype(np.int16)
    # Create stereo sound (duplicate for both channels and ensure C-contiguous)
    stereo = np.ascontiguousarray(np.column_stack((arr, arr)))
    return pygame.sndarray.make_sound(stereo)


class BattleEvent:
    def __init__(self, game):
        self.game = game
        self.staff = Staff(game)
        self.moving_blocks = []
        self.spawn_timer = 0
        self.score = 0
        self.full_hits = 0  # Hits with 80%+ precision
        self.half_hits = 0  # Hits with <80% precision
        self.previous_keys = pygame.key.get_pressed()
        # Load sounds for each button (try files first, fallback to generated)
        # Includes natural notes, sharps (with SHARP_MODIFIER, default SHIFT), and flats (with FLAT_MODIFIER, default CTRL)
        self._load_all_sounds()
        # Track button states: {key: {'lit': False, 'time': 0}}
        # Only track natural note buttons (sharps/flats share same button)
        self.button_states = {
            key: {"lit": False, "time": 0} for key in config.get_all_playable_keys()
        }
        # Load and process song based on config.DIFFICULTY
        raw_song = SONGS[config.CURRENT_SONG]
        self.song = self.process_song_for_difficulty(raw_song)
        self.song_index = 0
        self.song_finished = False

    def process_song_for_difficulty(self, raw_song):
        """Process the song based on current config.DIFFICULTY settings."""
        if not raw_song:
            return raw_song

        processed_song = []
        prev_frame = None

        for frame, key in raw_song:
            include_note = True

            if config.DIFFICULTY == "Medium":
                # Hide notes with frame difference < 30
                if prev_frame is not None and (frame - prev_frame) < 30:
                    include_note = False
            elif config.DIFFICULTY == "Easy":
                # Hide notes with frame difference < 50
                if prev_frame is not None and (frame - prev_frame) < 50:
                    include_note = False

            if include_note:
                # Adjust frame timing for Hard mode (shorten intervals)
                adjusted_frame = frame
                if config.DIFFICULTY == "Hard":
                    # Scale down frame times to make intervals shorter (e.g., 20% faster)
                    adjusted_frame = int(frame * 0.8)
                processed_song.append((adjusted_frame, key))
                prev_frame = frame  # Use original frame for difference calculation

        return processed_song

    def _load_all_sounds(self):
        """Load all sound variants (natural, sharp, flat) and distorted sounds for missed attempts."""
        # Load sounds for each button (try files first, fallback to generated)
        # Includes natural notes, sharps (with SHIFT), and flats (with CTRL)
        self.sounds = {}
        for key in config.get_all_playable_keys():
            note_name = config.NOTE_NAMES[key]
            # Natural note
            freq = config.get_note_frequency(key, 0)
            if freq:
                self.sounds[(key, 0)] = load_sound(note_name, freq)
            # Sharp (SHIFT modifier)
            freq_sharp = config.get_note_frequency(key, config.SHARP_MODIFIER)
            if freq_sharp:
                self.sounds[(key, config.SHARP_MODIFIER)] = load_sound(
                    note_name + "#", freq_sharp
                )
            # Flat (CTRL modifier)
            freq_flat = config.get_note_frequency(key, config.FLAT_MODIFIER)
            if freq_flat:
                self.sounds[(key, config.FLAT_MODIFIER)] = load_sound(
                    note_name + "b", freq_flat
                )

        # Generate distorted sounds for missed attempts
        self.distorted_sounds = {}
        for key in config.get_all_playable_keys():
            # Natural note
            freq = config.get_note_frequency(key, 0)
            if freq:
                self.distorted_sounds[(key, 0)] = generate_distorted_sound(freq)
            # Sharp
            freq_sharp = config.get_note_frequency(key, config.SHARP_MODIFIER)
            if freq_sharp:
                self.distorted_sounds[(key, config.SHARP_MODIFIER)] = (
                    generate_distorted_sound(freq_sharp)
                )
            # Flat
            freq_flat = config.get_note_frequency(key, config.FLAT_MODIFIER)
            if freq_flat:
                self.distorted_sounds[(key, config.FLAT_MODIFIER)] = (
                    generate_distorted_sound(freq_flat)
                )

    def update(self):
        self.spawn_timer += 1
        current_keys = pygame.key.get_pressed()
        current_mods = pygame.key.get_mods()  # Get current modifier state

        # Spawn blocks based on song
        if (
            self.song_index < len(self.song)
            and self.spawn_timer >= self.song[self.song_index][0]
        ):
            frame_time, note_key = self.song[self.song_index]
            # Extract base key if note_key is a tuple (for sharps/flats)
            base_key = note_key[0] if isinstance(note_key, tuple) else note_key
            # Find the button for this note
            target_button = None
            for button in self.staff.buttons:
                if button.key == base_key:
                    target_button = button
                    break
            if target_button:
                # Pass original note_key to preserve accidental information
                self.moving_blocks.append(
                    MovingBlock(self.game, target_button, note_key)
                )
            self.song_index += 1

        # Update button light-up timers
        for key, state in self.button_states.items():
            if state["lit"]:
                state["time"] -= 1
                if state["time"] <= 0:
                    state["lit"] = False

        # Check for key presses (detect both successful and missed inputs)
        for key in config.get_all_playable_keys():
            if current_keys[key] and not self.previous_keys[key]:
                # Key was just pressed
                # Check if there's a collision
                has_collision = False
                for block in self.moving_blocks:
                    if block.target.key == key and block.is_colliding():
                        has_collision = True
                        break

                if not has_collision:
                    # Missed input - play distorted sound and button stays normal
                    if (key, 0) in self.distorted_sounds:
                        self.distorted_sounds[(key, 0)].play()

        for block in self.moving_blocks[:]:
            block.update()
            if block.is_colliding():
                # Extract expected base key and modifier from note_key
                if isinstance(block.note_key, tuple):
                    expected_base_key, expected_modifier = block.note_key
                else:
                    expected_base_key = block.note_key
                    expected_modifier = 0

                # Get current modifier state
                current_modifier = 0
                if current_mods & config.SHARP_MODIFIER:
                    current_modifier = config.SHARP_MODIFIER
                elif current_mods & config.FLAT_MODIFIER:
                    current_modifier = config.FLAT_MODIFIER

                # Check if the correct key with correct modifier is pressed
                if (
                    current_keys[expected_base_key]
                    and not self.previous_keys[expected_base_key]
                    and current_modifier == expected_modifier
                ):
                    # Calculate precision based on overlap
                    precision = self.calculate_precision(
                        block.rect(), block.target.rect()
                    )

                    # Award points based on precision (80% threshold)
                    if precision >= 80.0:
                        self.score += 1
                        self.full_hits += 1
                    else:
                        self.score += 0.5  # Half points for imprecise hits
                        self.half_hits += 1

                    # Play the corresponding note using preserved note_key (handles sharps/flats)
                    if block.note_key is not None:
                        # note_key is either a simple key or (key, modifier) tuple
                        sound_key = (
                            block.note_key
                            if isinstance(block.note_key, tuple)
                            else (block.note_key, 0)
                        )
                    else:
                        # Fallback for blocks without note_key
                        sound_key = (block.target.key, 0)
                    if sound_key in self.sounds:
                        self.sounds[sound_key].play()
                    # Light up the button on successful hit (use base key for button state)
                    base_key = (
                        block.target.key[0]
                        if isinstance(block.target.key, tuple)
                        else block.target.key
                    )
                    self.button_states[base_key]["lit"] = True
                    self.button_states[base_key]["time"] = 10  # Display for 10 frames
                    self.moving_blocks.remove(block)
            elif block.position.x < 0:
                self.moving_blocks.remove(block)

        # Check if song is finished
        if self.song_index >= len(self.song) and len(self.moving_blocks) == 0:
            self.song_finished = True

        self.previous_keys = current_keys

    def calculate_precision(self, rect1, rect2):
        """
        Calculate the precision/accuracy of a hit based on rectangle overlap.

        Args:
            rect1: pygame.Rect of the moving block
            rect2: pygame.Rect of the target button

        Returns:
            float: Overlap percentage (0-100)
        """
        # Calculate intersection
        intersection = rect1.clip(rect2)

        if intersection.width <= 0 or intersection.height <= 0:
            return 0.0

        intersection_area = intersection.width * intersection.height
        rect1_area = rect1.width * rect1.height

        # Calculate percentage of rect1 that overlaps with rect2
        # (how much of the block is inside the button area)
        if rect1_area == 0:
            return 0.0

        overlap_percentage = (intersection_area / rect1_area) * 100
        return min(overlap_percentage, 100.0)  # Cap at 100%

    def draw(self):
        self.staff.draw()
        # Draw buttons with state coloring
        for button in self.staff.buttons:
            if self.button_states[button.key]["lit"]:
                # Draw button normally
                self.game.display_surface.blit(
                    button.image, (button.position.x, button.position.y)
                )
                # Draw a semi-transparent white overlay to lighten the button
                highlight = pygame.Surface(
                    (button.width, button.height), pygame.SRCALPHA
                )
                highlight.fill((255, 255, 255, 150))  # White with 100/255 alpha
                self.game.display_surface.blit(
                    highlight, (button.position.x, button.position.y)
                )
            else:
                # Draw button normally
                button.draw()

        for block in self.moving_blocks:
            block.draw()


class TalkEvent: ...
