import pygame
import numpy as np
from entities import Staff, MovingBlock
import config
from songs import SONGS


def load_sound(key_name, frequency, duration=0.5, sample_rate=22050):
    """Load a sound file for the given key, or generate it if file doesn't exist."""
    sound_file = config.ROOT_PATH / "sounds" / f"note_{key_name}.wav"
    try:
        return pygame.mixer.Sound(str(sound_file))
    except (pygame.error, FileNotFoundError):
        # Fallback to generating the sound
        return generate_sound(frequency, duration, sample_rate)


def generate_sound(frequency, duration=0.5, sample_rate=22050):
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


class BattleEvent:
    def __init__(self, game):
        self.game = game
        self.staff = Staff(game)
        self.moving_blocks = []
        self.spawn_timer = 0
        self.score = 0
        self.previous_keys = pygame.key.get_pressed()
        # Load sounds for each button (try files first, fallback to generated)
        key_names = {
            pygame.K_a: 'a',
            pygame.K_s: 's', 
            pygame.K_d: 'd',
            pygame.K_f: 'f',
            pygame.K_g: 'g',
            pygame.K_h: 'h',
            pygame.K_j: 'j'
        }
        self.sounds = {
            key: load_sound(key_names[key], freq) for key, freq in config.NOTE_FREQUENCIES.items()
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

    def update(self):
        self.spawn_timer += 1
        current_keys = pygame.key.get_pressed()

        # Spawn blocks based on song
        if (
            self.song_index < len(self.song)
            and self.spawn_timer >= self.song[self.song_index][0]
        ):
            frame_time, note_key = self.song[self.song_index]
            # Find the button for this note
            target_button = None
            for button in self.staff.buttons:
                if button.key == note_key:
                    target_button = button
                    break
            if target_button:
                self.moving_blocks.append(MovingBlock(self.game, target_button))
            self.song_index += 1

        for block in self.moving_blocks[:]:
            block.update()
            if block.is_colliding():
                if (
                    current_keys[block.target.key]
                    and not self.previous_keys[block.target.key]
                ):
                    self.score += 1
                    # Play the corresponding note
                    if block.target.key in self.sounds:
                        self.sounds[block.target.key].play()
                    self.moving_blocks.remove(block)
            elif block.position.x < 0:
                self.moving_blocks.remove(block)

        # Check if song is finished
        if self.song_index >= len(self.song) and len(self.moving_blocks) == 0:
            self.song_finished = True

        self.previous_keys = current_keys

    def draw(self):
        self.staff.draw()
        for block in self.moving_blocks:
            block.draw()


class TalkEvent: ...
