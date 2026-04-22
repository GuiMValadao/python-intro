import pygame
from pathlib import Path
from enum import Enum

ROOT_PATH = Path(__file__).parent


class GameState(Enum):
    """Game state enumeration."""

    MENU = "menu"
    OPTIONS = "options"
    PLAY = "play"
    SONG_END = "song_end"
    PAUSE = "pause"


DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
MENU_BACKGROUND = (0, 0, 0)
BATTLE_BACKGROUND = (255, 255, 255)
FRAME_REFRESH_RATE = 60
PLAYER_SPEED = 5
SPAWN_MIN = 10
SPAWN_MAX = 120
DIFFICULTY = "Medium"  # Default difficulty
CURRENT_SONG = "song2"  # variable to change the song to play
INSTRUMENT = "acoustic_guitar"  # change the folder with the sounds
GAME_FONT = "Bauhaus 93"

# Key bindings - maps pygame keys to note names
# Can be easily remapped for different key layouts
NOTES_TO_KEYS = {
    "A": pygame.K_a,
    "B": pygame.K_s,
    "C": pygame.K_d,
    "D": pygame.K_f,
    "E": pygame.K_g,
    "F": pygame.K_h,
    "G": pygame.K_j,
}

SHARP_MODIFIER = pygame.KMOD_SHIFT
FLAT_MODIFIER = pygame.KMOD_CTRL

NOTE_NAMES = {
    NOTES_TO_KEYS["A"]: "A2",  # A2
    NOTES_TO_KEYS["B"]: "B2",  # B2
    NOTES_TO_KEYS["C"]: "C3",  # C3
    NOTES_TO_KEYS["D"]: "D3",  # D3
    NOTES_TO_KEYS["E"]: "E3",  # E3
    NOTES_TO_KEYS["F"]: "F3",  # F3
    NOTES_TO_KEYS["G"]: "G3",  # G3
}

# Extended note names for songs - includes sharps and flats
# Format: "NOTE#" for sharps, "NOTEb" for flats
EXTENDED_NOTE_NAMES = {
    # Natural notes
    "A2": NOTES_TO_KEYS["A"],
    "B2": NOTES_TO_KEYS["B"],
    "C3": NOTES_TO_KEYS["C"],
    "D3": NOTES_TO_KEYS["D"],
    "E3": NOTES_TO_KEYS["E"],
    "F3": NOTES_TO_KEYS["F"],
    "G3": NOTES_TO_KEYS["G"],
    # Sharps
    "A2#": (NOTES_TO_KEYS["A"], SHARP_MODIFIER),
    "B2#": (NOTES_TO_KEYS["B"], SHARP_MODIFIER),
    "C3#": (NOTES_TO_KEYS["C"], SHARP_MODIFIER),
    "D3#": (NOTES_TO_KEYS["D"], SHARP_MODIFIER),
    "E3#": (NOTES_TO_KEYS["E"], SHARP_MODIFIER),
    "F3#": (NOTES_TO_KEYS["F"], SHARP_MODIFIER),
    "G3#": (NOTES_TO_KEYS["G"], SHARP_MODIFIER),
    # Flats
    "A2b": (NOTES_TO_KEYS["A"], FLAT_MODIFIER),
    "B2b": (NOTES_TO_KEYS["B"], FLAT_MODIFIER),
    "C3b": (NOTES_TO_KEYS["C"], FLAT_MODIFIER),
    "D3b": (NOTES_TO_KEYS["D"], FLAT_MODIFIER),
    "E3b": (NOTES_TO_KEYS["E"], FLAT_MODIFIER),
    "F3b": (NOTES_TO_KEYS["F"], FLAT_MODIFIER),
    "G3b": (NOTES_TO_KEYS["G"], FLAT_MODIFIER),
}


# Enharmonic equivalents for saving space on acoustic guitar samples
# Maps flat notes to their enharmonic sharp equivalents (same pitch, different names)
# This avoids needing separate files for Cb=B, Db=C#, Eb=D#, Fb=E, Gb=F#, etc.
ENHARMONIC_EQUIVALENTS = {
    "B2b": "A2#",  # Bb → A#
    "B2#": "C3",  # B# → C
    "C3b": "B2",  # Cb → B
    "D3b": "C3#",  # Db → C#
    "E3b": "D3#",  # Eb → D#
    "E3#": "F3",  # E# → F
    "F3b": "E3",  # Fb → E
    "G3b": "F3#",  # Gb → F#
}


def get_sound_file_name(note_name):
    """
    Get the actual sound file name, resolving enharmonic equivalents.

    Args:
        note_name: Note name like "A2", "A2#", "A2b"

    Returns:
        str: Actual note name to use for the sound file
    """
    return ENHARMONIC_EQUIVALENTS.get(note_name, note_name)


# Musical note frequencies (Hz) - natural notes only
# Sharps and flats are calculated using semitone ratio
_SEMITONE_RATIO = 2 ** (1 / 12)  # Equal temperament semitone ratio

# Natural note frequencies
_NATURAL_FREQUENCIES = {
    NOTES_TO_KEYS["A"]: 110,  # A2
    NOTES_TO_KEYS["B"]: 123,  # B2
    NOTES_TO_KEYS["C"]: 131,  # C3
    NOTES_TO_KEYS["D"]: 147,  # D3
    NOTES_TO_KEYS["E"]: 165,  # E3
    NOTES_TO_KEYS["F"]: 175,  # F3
    NOTES_TO_KEYS["G"]: 196,  # G3
}

# Sharp frequencies (up one semitone) - accessed with SHIFT modifier
_SHARP_FREQUENCIES = {
    k: int(v * _SEMITONE_RATIO) for k, v in _NATURAL_FREQUENCIES.items()
}

# Flat frequencies (down one semitone) - accessed with CTRL modifier
_FLAT_FREQUENCIES = {
    k: int(v / _SEMITONE_RATIO) for k, v in _NATURAL_FREQUENCIES.items()
}

# Keep original NOTE_FREQUENCIES for backward compatibility
NOTE_FREQUENCIES = _NATURAL_FREQUENCIES.copy()


def get_note_frequency(key, modifier=0):
    """
    Get frequency for a key with optional modifier.

    Args:
        key: pygame key constant (e.g., pygame.K_a)
        modifier: pygame key modifier (0, SHARP_MODIFIER, or FLAT_MODIFIER)

    Returns:
        int: Frequency in Hz, or None if key not found
    """
    if modifier & SHARP_MODIFIER:
        return _SHARP_FREQUENCIES.get(key)
    elif modifier & FLAT_MODIFIER:
        return _FLAT_FREQUENCIES.get(key)
    else:
        return _NATURAL_FREQUENCIES.get(key)


def get_all_playable_keys():
    """Return all keys that can be played (natural notes)."""
    return list(NOTES_TO_KEYS.values())
