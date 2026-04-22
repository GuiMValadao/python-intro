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
    NOTES_TO_KEYS["A"]: "A2",
    NOTES_TO_KEYS["B"]: "B2",
    NOTES_TO_KEYS["C"]: "C3",
    NOTES_TO_KEYS["D"]: "D3",
    NOTES_TO_KEYS["E"]: "E3",
    NOTES_TO_KEYS["F"]: "F3",
    NOTES_TO_KEYS["G"]: "G3",
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
ENHARMONIC_EQUIVALENTS = {
    "B2b": "A2#",
    "B2#": "C3",
    "C3b": "B2",
    "D3b": "C3#",
    "E3b": "D3#",
    "E3#": "F3",
    "F3b": "E3",
    "G3b": "F3#",
}

# ---------------------------------------------------------------------------
# Key signatures
# Each entry maps natural note names to their altered default in that key.
# The modifier key overrides the signature back to natural during play.
# Sharps: value ends with "#"  → Shift restores natural
# Flats:  value ends with "b"  → Ctrl  restores natural
# ---------------------------------------------------------------------------
KEY_SIGNATURES = {
    # Major keys (sharps)
    "C_major": {},
    "G_major": {"F3": "F3#"},
    "D_major": {"F3": "F3#", "C3": "C3#"},
    "A_major": {"F3": "F3#", "C3": "C3#", "G3": "G3#"},
    "E_major": {"F3": "F3#", "C3": "C3#", "G3": "G3#", "D3": "D3#"},
    "B_major": {"F3": "F3#", "C3": "C3#", "G3": "G3#", "D3": "D3#", "A2": "A2#"},
    # Major keys (flats)
    "F_major": {"B2": "B2b"},
    "Bb_major": {"B2": "B2b", "E3": "E3b"},
    "Eb_major": {"B2": "B2b", "E3": "E3b", "A2": "A2b"},
    "Ab_major": {"B2": "B2b", "E3": "E3b", "A2": "A2b", "D3": "D3b"},
    # Relative minor keys (same signatures as their relative major)
    "A_minor": {},       # relative of C major
    "E_minor": {"F3": "F3#"},
    "D_minor": {"B2": "B2b"},
    "G_minor": {"B2": "B2b", "E3": "E3b"},
}

# Human-readable display names for key signatures shown in the HUD
KEY_SIGNATURE_DISPLAY = {
    "C_major": "C Major",
    "G_major": "G Major",
    "D_major": "D Major",
    "A_major": "A Major",
    "E_major": "E Major",
    "B_major": "B Major",
    "F_major": "F Major",
    "Bb_major": "Bb Major",
    "Eb_major": "Eb Major",
    "Ab_major": "Ab Major",
    "A_minor": "A Minor",
    "E_minor": "E Minor",
    "D_minor": "D Minor",
    "G_minor": "G Minor",
}

CURRENT_KEY_SIGNATURE = "C_major"


def get_key_signature():
    """Return the alterations dict for the current key signature."""
    return KEY_SIGNATURES.get(CURRENT_KEY_SIGNATURE, {})


def get_sound_file_name(note_name):
    """
    Get the actual sound file name, resolving enharmonic equivalents.

    Args:
        note_name: Note name like "A2", "A2#", "A2b"

    Returns:
        str: Actual note name to use for the sound file
    """
    return ENHARMONIC_EQUIVALENTS.get(note_name, note_name)


_SEMITONE_RATIO = 2 ** (1 / 12)

_NATURAL_FREQUENCIES = {
    NOTES_TO_KEYS["A"]: 110,
    NOTES_TO_KEYS["B"]: 123,
    NOTES_TO_KEYS["C"]: 131,
    NOTES_TO_KEYS["D"]: 147,
    NOTES_TO_KEYS["E"]: 165,
    NOTES_TO_KEYS["F"]: 175,
    NOTES_TO_KEYS["G"]: 196,
}

_SHARP_FREQUENCIES = {
    k: int(v * _SEMITONE_RATIO) for k, v in _NATURAL_FREQUENCIES.items()
}

_FLAT_FREQUENCIES = {
    k: int(v / _SEMITONE_RATIO) for k, v in _NATURAL_FREQUENCIES.items()
}

NOTE_FREQUENCIES = _NATURAL_FREQUENCIES.copy()


def get_note_frequency(key, modifier=0):
    """
    Get frequency for a key with optional modifier.

    Args:
        key: pygame key constant
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
