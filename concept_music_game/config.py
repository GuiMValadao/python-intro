import pygame
from pathlib import Path
from enum import Enum

ROOT_PATH = Path(__file__).parent


class GameState(Enum):
    MENU = "menu"
    OPTIONS = "options"
    PLAY = "play"
    SONG_END = "song_end"
    PAUSE = "pause"
    DIALOGUE = "dialogue"


DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
MENU_BACKGROUND = (0, 0, 0)
BATTLE_BACKGROUND = (255, 255, 255)
FRAME_REFRESH_RATE = 60
PLAYER_SPEED = 5
SPAWN_MIN = 10
SPAWN_MAX = 120
DIFFICULTY = "Medium"
CURRENT_SONG = "song2"
INSTRUMENT = "acoustic_guitar"
GAME_FONT = "Bauhaus 93"
INTERACTION_KEY = pygame.K_x

NOTES_TO_KEYS = {
    "A": pygame.K_a,
    "B": pygame.K_s,
    "C": pygame.K_d,
    "D": pygame.K_h,
    "E": pygame.K_j,
    "F": pygame.K_k,
    "G": pygame.K_l,
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

EXTENDED_NOTE_NAMES = {
    "A2": NOTES_TO_KEYS["A"],
    "B2": NOTES_TO_KEYS["B"],
    "C3": NOTES_TO_KEYS["C"],
    "D3": NOTES_TO_KEYS["D"],
    "E3": NOTES_TO_KEYS["E"],
    "F3": NOTES_TO_KEYS["F"],
    "G3": NOTES_TO_KEYS["G"],
    "A2#": (NOTES_TO_KEYS["A"], SHARP_MODIFIER),
    "B2#": (NOTES_TO_KEYS["B"], SHARP_MODIFIER),
    "C3#": (NOTES_TO_KEYS["C"], SHARP_MODIFIER),
    "D3#": (NOTES_TO_KEYS["D"], SHARP_MODIFIER),
    "E3#": (NOTES_TO_KEYS["E"], SHARP_MODIFIER),
    "F3#": (NOTES_TO_KEYS["F"], SHARP_MODIFIER),
    "G3#": (NOTES_TO_KEYS["G"], SHARP_MODIFIER),
    "A2b": (NOTES_TO_KEYS["A"], FLAT_MODIFIER),
    "B2b": (NOTES_TO_KEYS["B"], FLAT_MODIFIER),
    "C3b": (NOTES_TO_KEYS["C"], FLAT_MODIFIER),
    "D3b": (NOTES_TO_KEYS["D"], FLAT_MODIFIER),
    "E3b": (NOTES_TO_KEYS["E"], FLAT_MODIFIER),
    "F3b": (NOTES_TO_KEYS["F"], FLAT_MODIFIER),
    "G3b": (NOTES_TO_KEYS["G"], FLAT_MODIFIER),
}

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

KEY_SIGNATURES = {
    "C_major": {},
    "G_major": {"F3": "F3#"},
    "D_major": {"F3": "F3#", "C3": "C3#"},
    "A_major": {"F3": "F3#", "C3": "C3#", "G3": "G3#"},
    "E_major": {"F3": "F3#", "C3": "C3#", "G3": "G3#", "D3": "D3#"},
    "B_major": {"F3": "F3#", "C3": "C3#", "G3": "G3#", "D3": "D3#", "A2": "A2#"},
    "F_major": {"B2": "B2b"},
    "Bb_major": {"B2": "B2b", "E3": "E3b"},
    "Eb_major": {"B2": "B2b", "E3": "E3b", "A2": "A2b"},
    "Ab_major": {"B2": "B2b", "E3": "E3b", "A2": "A2b", "D3": "D3b"},
    "A_minor": {},
    "E_minor": {"F3": "F3#"},
    "D_minor": {"B2": "B2b"},
    "G_minor": {"B2": "B2b", "E3": "E3b"},
}

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
    return KEY_SIGNATURES.get(CURRENT_KEY_SIGNATURE, {})


# ---------------------------------------------------------------------------
# Key remapping
# ---------------------------------------------------------------------------

_RESERVED_KEYS = {
    pygame.K_UP,
    pygame.K_DOWN,
    pygame.K_LEFT,
    pygame.K_RIGHT,
    pygame.K_p,
    pygame.K_m,
    pygame.K_b,
    pygame.K_q,
    pygame.K_RETURN,
    pygame.K_ESCAPE,
    INTERACTION_KEY,
}


def remap_key(note_name, new_key):
    """
    Reassign a note to a new key and rebuild all derived mappings.

    Args:
        note_name: One of "A", "B", "C", "D", "E", "F", "G"
        new_key:   A pygame key constant (e.g. pygame.K_z)

    Returns:
        str: Error message if the remap was rejected, or None on success.
    """
    if new_key in _RESERVED_KEYS:
        return "That key is reserved by the game."
    if new_key in NOTES_TO_KEYS.values() and NOTES_TO_KEYS[note_name] != new_key:
        return "That key is already assigned to another note."

    NOTES_TO_KEYS[note_name] = new_key
    _rebuild_note_maps()
    return None


def _rebuild_note_maps():
    """Rebuild NOTE_NAMES, EXTENDED_NOTE_NAMES, and frequency tables after a remap."""
    global NOTE_NAMES, EXTENDED_NOTE_NAMES
    global _NATURAL_FREQUENCIES, _SHARP_FREQUENCIES, _FLAT_FREQUENCIES, NOTE_FREQUENCIES

    NOTE_NAMES = {
        NOTES_TO_KEYS["A"]: "A2",
        NOTES_TO_KEYS["B"]: "B2",
        NOTES_TO_KEYS["C"]: "C3",
        NOTES_TO_KEYS["D"]: "D3",
        NOTES_TO_KEYS["E"]: "E3",
        NOTES_TO_KEYS["F"]: "F3",
        NOTES_TO_KEYS["G"]: "G3",
    }

    EXTENDED_NOTE_NAMES = {
        "A2": NOTES_TO_KEYS["A"],
        "B2": NOTES_TO_KEYS["B"],
        "C3": NOTES_TO_KEYS["C"],
        "D3": NOTES_TO_KEYS["D"],
        "E3": NOTES_TO_KEYS["E"],
        "F3": NOTES_TO_KEYS["F"],
        "G3": NOTES_TO_KEYS["G"],
        "A2#": (NOTES_TO_KEYS["A"], SHARP_MODIFIER),
        "B2#": (NOTES_TO_KEYS["B"], SHARP_MODIFIER),
        "C3#": (NOTES_TO_KEYS["C"], SHARP_MODIFIER),
        "D3#": (NOTES_TO_KEYS["D"], SHARP_MODIFIER),
        "E3#": (NOTES_TO_KEYS["E"], SHARP_MODIFIER),
        "F3#": (NOTES_TO_KEYS["F"], SHARP_MODIFIER),
        "G3#": (NOTES_TO_KEYS["G"], SHARP_MODIFIER),
        "A2b": (NOTES_TO_KEYS["A"], FLAT_MODIFIER),
        "B2b": (NOTES_TO_KEYS["B"], FLAT_MODIFIER),
        "C3b": (NOTES_TO_KEYS["C"], FLAT_MODIFIER),
        "D3b": (NOTES_TO_KEYS["D"], FLAT_MODIFIER),
        "E3b": (NOTES_TO_KEYS["E"], FLAT_MODIFIER),
        "F3b": (NOTES_TO_KEYS["F"], FLAT_MODIFIER),
        "G3b": (NOTES_TO_KEYS["G"], FLAT_MODIFIER),
    }

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


def get_key_name(key):
    """Return a human-readable uppercase name for a pygame key constant."""
    name = pygame.key.name(key)
    return name.upper() if name else "?"


# ---------------------------------------------------------------------------
# Sound helpers
# ---------------------------------------------------------------------------


def get_sound_file_name(note_name):
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
    if modifier & SHARP_MODIFIER:
        return _SHARP_FREQUENCIES.get(key)
    elif modifier & FLAT_MODIFIER:
        return _FLAT_FREQUENCIES.get(key)
    else:
        return _NATURAL_FREQUENCIES.get(key)


def get_all_playable_keys():
    return list(NOTES_TO_KEYS.values())
