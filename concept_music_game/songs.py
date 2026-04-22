from config import EXTENDED_NOTE_NAMES

# ---------------------------------------------------------------------------
# Song format
# ---------------------------------------------------------------------------
# Each song is a dict with two keys:
#   "key_signature" : starting key (must match a key in config.KEY_SIGNATURES)
#   "notes"         : list of (frame_time, event) tuples where event is either
#                       - a list of note keys  →  [EXTENDED_NOTE_NAMES["A2"], ...]
#                       - a key change dict    →  {"key_change": "G_major"}
#
# Notes within a chord (same frame) must share the same modifier type
# (all natural, all sharp, or all flat) due to the global modifier constraint.
# A validator in BattleEvent.__init__ will catch violations at load time.
# ---------------------------------------------------------------------------

SONG_1 = {
    "key_signature": "C_major",
    "notes": [
        (60, [EXTENDED_NOTE_NAMES["A2"]]),
        (120, [EXTENDED_NOTE_NAMES["A2"], EXTENDED_NOTE_NAMES["B2"]]),  # chord
        (180, [EXTENDED_NOTE_NAMES["C3"]]),
        (240, [EXTENDED_NOTE_NAMES["D3"]]),
        (300, [EXTENDED_NOTE_NAMES["E3"]]),
        (360, [EXTENDED_NOTE_NAMES["F3"]]),
        (420, [EXTENDED_NOTE_NAMES["G3"]]),
        (480, [EXTENDED_NOTE_NAMES["A2"]]),
        (540, [EXTENDED_NOTE_NAMES["B2"]]),
        (600, [EXTENDED_NOTE_NAMES["C3"]]),
        (660, [EXTENDED_NOTE_NAMES["D3"]]),
        (720, [EXTENDED_NOTE_NAMES["E3"]]),
        (780, [EXTENDED_NOTE_NAMES["F3"]]),
        (840, [EXTENDED_NOTE_NAMES["G3"]]),
        (900, [EXTENDED_NOTE_NAMES["A2"]]),
        (960, [EXTENDED_NOTE_NAMES["B2"]]),
        (1020, [EXTENDED_NOTE_NAMES["C3"]]),
        (1080, [EXTENDED_NOTE_NAMES["D3"]]),
        (1140, [EXTENDED_NOTE_NAMES["E3"]]),
        (1200, [EXTENDED_NOTE_NAMES["F3"]]),
        (1260, [EXTENDED_NOTE_NAMES["G3"]]),
    ],
}

SONG_2 = {
    "key_signature": "C_major",
    "notes": [
        (60, [EXTENDED_NOTE_NAMES["A2"]]),
        (80, [EXTENDED_NOTE_NAMES["A2"]]),
        (100, [EXTENDED_NOTE_NAMES["B2"]]),
        (140, [EXTENDED_NOTE_NAMES["A2"]]),
        (180, [EXTENDED_NOTE_NAMES["C3"]]),
        (220, [EXTENDED_NOTE_NAMES["A2"]]),
        (250, [EXTENDED_NOTE_NAMES["D3"]]),
        (280, [EXTENDED_NOTE_NAMES["D3"]]),
        (340, [EXTENDED_NOTE_NAMES["C3"]]),
        (380, [EXTENDED_NOTE_NAMES["D3"]]),
        (420, [EXTENDED_NOTE_NAMES["D3"]]),
        (460, [EXTENDED_NOTE_NAMES["C3"]]),
        (500, [EXTENDED_NOTE_NAMES["D3"]]),
        (530, [EXTENDED_NOTE_NAMES["A2"]]),
        (560, [EXTENDED_NOTE_NAMES["A2"]]),
        (590, [EXTENDED_NOTE_NAMES["B2"]]),
        (640, [EXTENDED_NOTE_NAMES["A2"]]),
        (690, [EXTENDED_NOTE_NAMES["B2"]]),
        (740, [EXTENDED_NOTE_NAMES["D3"]]),
        (790, [EXTENDED_NOTE_NAMES["B2"]]),
        (800, [EXTENDED_NOTE_NAMES["A2"]]),
        (830, [EXTENDED_NOTE_NAMES["A2"]]),
        (860, [EXTENDED_NOTE_NAMES["A2"]]),
        (890, [EXTENDED_NOTE_NAMES["B2"]]),
        (920, [EXTENDED_NOTE_NAMES["A2"]]),
        (950, [EXTENDED_NOTE_NAMES["C3"]]),
        (980, [EXTENDED_NOTE_NAMES["A2"]]),
        (1010, [EXTENDED_NOTE_NAMES["D3"]]),
        (1040, [EXTENDED_NOTE_NAMES["D3"]]),
        (1070, [EXTENDED_NOTE_NAMES["C3"]]),
        (1100, [EXTENDED_NOTE_NAMES["D3"]]),
        (1130, [EXTENDED_NOTE_NAMES["D3"]]),
        (1160, [EXTENDED_NOTE_NAMES["C3"]]),
        (1190, [EXTENDED_NOTE_NAMES["D3"]]),
        (1220, [EXTENDED_NOTE_NAMES["A2"]]),
        (1250, [EXTENDED_NOTE_NAMES["A2"]]),
        (1280, [EXTENDED_NOTE_NAMES["B2"]]),
        (1310, [EXTENDED_NOTE_NAMES["A2"]]),
        (1340, [EXTENDED_NOTE_NAMES["B2"]]),
        (1370, [EXTENDED_NOTE_NAMES["D3"]]),
        (1400, [EXTENDED_NOTE_NAMES["B2"]]),
        (1500, [EXTENDED_NOTE_NAMES["A2"]]),
    ],
}

SONG_3 = {
    "key_signature": "C_major",
    "notes": [
        # Intro
        (60, [EXTENDED_NOTE_NAMES["A2"]]),
        (120, [EXTENDED_NOTE_NAMES["A2"], EXTENDED_NOTE_NAMES["C3"]]),  # chord
        (180, [EXTENDED_NOTE_NAMES["E3"]]),
        (240, [EXTENDED_NOTE_NAMES["A2"]]),
        (300, [EXTENDED_NOTE_NAMES["C3"]]),
        (360, [EXTENDED_NOTE_NAMES["E3"]]),
        (420, [EXTENDED_NOTE_NAMES["A2"]]),
        (480, [EXTENDED_NOTE_NAMES["C3"]]),
        (540, [EXTENDED_NOTE_NAMES["E3"]]),
        # Build up
        (600, [EXTENDED_NOTE_NAMES["A2"]]),
        (630, [EXTENDED_NOTE_NAMES["B2"]]),
        (660, [EXTENDED_NOTE_NAMES["C3"]]),
        (690, [EXTENDED_NOTE_NAMES["D3"]]),
        (720, [EXTENDED_NOTE_NAMES["E3"]]),
        (750, [EXTENDED_NOTE_NAMES["F3"]]),
        (780, [EXTENDED_NOTE_NAMES["G3"]]),
        (810, [EXTENDED_NOTE_NAMES["A2"]]),
        (840, [EXTENDED_NOTE_NAMES["B2"]]),
        (870, [EXTENDED_NOTE_NAMES["C3"]]),
        (900, [EXTENDED_NOTE_NAMES["D3"]]),
        (930, [EXTENDED_NOTE_NAMES["E3"]]),
        (960, [EXTENDED_NOTE_NAMES["F3"]]),
        (990, [EXTENDED_NOTE_NAMES["G3"]]),
        # Key change to G major — F becomes F# from here
        (1020, {"key_change": "G_major"}),
        # Chorus — F3 notes now sound as F#
        (1050, [EXTENDED_NOTE_NAMES["A2"]]),
        (1080, [EXTENDED_NOTE_NAMES["A2"]]),
        (1110, [EXTENDED_NOTE_NAMES["B2"]]),
        (1140, [EXTENDED_NOTE_NAMES["B2"]]),
        (1170, [EXTENDED_NOTE_NAMES["C3"]]),
        (1200, [EXTENDED_NOTE_NAMES["C3"]]),
        (1230, [EXTENDED_NOTE_NAMES["D3"]]),
        (1260, [EXTENDED_NOTE_NAMES["D3"]]),
        (1290, [EXTENDED_NOTE_NAMES["E3"]]),
        (1320, [EXTENDED_NOTE_NAMES["E3"]]),
        (1350, [EXTENDED_NOTE_NAMES["F3"]]),  # plays as F#
        (1380, [EXTENDED_NOTE_NAMES["F3"]]),  # plays as F#
        (1410, [EXTENDED_NOTE_NAMES["G3"]]),
        (1440, [EXTENDED_NOTE_NAMES["G3"]]),
        # Bridge — back to C major
        (1470, {"key_change": "C_major"}),
        (1500, [EXTENDED_NOTE_NAMES["A2"]]),
        (1530, [EXTENDED_NOTE_NAMES["G3"]]),
        (1560, [EXTENDED_NOTE_NAMES["E3"]]),
        (1590, [EXTENDED_NOTE_NAMES["C3"]]),
        (1620, [EXTENDED_NOTE_NAMES["A2"]]),
        (1650, [EXTENDED_NOTE_NAMES["G3"]]),
        (1680, [EXTENDED_NOTE_NAMES["E3"]]),
        (1710, [EXTENDED_NOTE_NAMES["C3"]]),
        # Climax — fast run
        (1800, [EXTENDED_NOTE_NAMES["A2"]]),
        (1810, [EXTENDED_NOTE_NAMES["B2"]]),
        (1820, [EXTENDED_NOTE_NAMES["C3"]]),
        (1830, [EXTENDED_NOTE_NAMES["D3"]]),
        (1840, [EXTENDED_NOTE_NAMES["E3"]]),
        (1850, [EXTENDED_NOTE_NAMES["F3"]]),
        (1860, [EXTENDED_NOTE_NAMES["G3"]]),
        (1870, [EXTENDED_NOTE_NAMES["A2"]]),
        (1880, [EXTENDED_NOTE_NAMES["B2"]]),
        (1890, [EXTENDED_NOTE_NAMES["C3"]]),
        (1900, [EXTENDED_NOTE_NAMES["D3"]]),
        (1910, [EXTENDED_NOTE_NAMES["E3"]]),
        (1920, [EXTENDED_NOTE_NAMES["F3"]]),
        (1930, [EXTENDED_NOTE_NAMES["G3"]]),
        (1940, [EXTENDED_NOTE_NAMES["A2"]]),
        (1950, [EXTENDED_NOTE_NAMES["B2"]]),
        (1960, [EXTENDED_NOTE_NAMES["C3"]]),
        (1970, [EXTENDED_NOTE_NAMES["D3"]]),
        (1980, [EXTENDED_NOTE_NAMES["E3"]]),
        (1990, [EXTENDED_NOTE_NAMES["F3"]]),
        (2000, [EXTENDED_NOTE_NAMES["G3"]]),
    ],
}

SONG_4 = {
    "key_signature": "A_major",
    "notes": [
        # Intro in A major (F#, C#, G# by default)
        (60, [EXTENDED_NOTE_NAMES["A2"]]),
        (120, [EXTENDED_NOTE_NAMES["A2"], EXTENDED_NOTE_NAMES["C3"]]),  # C3 plays as C#
        (180, [EXTENDED_NOTE_NAMES["E3"]]),
        (240, [EXTENDED_NOTE_NAMES["A2"]]),
        (300, [EXTENDED_NOTE_NAMES["C3"]]),  # C#
        (360, [EXTENDED_NOTE_NAMES["E3"]]),
        (420, [EXTENDED_NOTE_NAMES["A2"]]),
        (480, [EXTENDED_NOTE_NAMES["C3"]]),  # C#
        (540, [EXTENDED_NOTE_NAMES["E3"]]),
        # Build up
        (600, [EXTENDED_NOTE_NAMES["A2"]]),
        (630, [EXTENDED_NOTE_NAMES["B2"]]),
        (660, [EXTENDED_NOTE_NAMES["C3"]]),  # C#
        (690, [EXTENDED_NOTE_NAMES["D3"]]),
        (720, [EXTENDED_NOTE_NAMES["E3"]]),
        (750, [EXTENDED_NOTE_NAMES["F3"]]),  # F#
        (780, [EXTENDED_NOTE_NAMES["G3"]]),  # G#
        (810, [EXTENDED_NOTE_NAMES["A2"]]),
        (840, [EXTENDED_NOTE_NAMES["B2"]]),
        (870, [EXTENDED_NOTE_NAMES["C3"]]),  # C#
        (900, [EXTENDED_NOTE_NAMES["D3"]]),
        (930, [EXTENDED_NOTE_NAMES["E3"]]),
        (960, [EXTENDED_NOTE_NAMES["F3"]]),  # F#
        (990, [EXTENDED_NOTE_NAMES["G3"]]),  # G#
        # Key change to D minor (flatter territory)
        (1020, {"key_change": "D_minor"}),
        # Chorus in D minor (B becomes Bb)
        (1050, [EXTENDED_NOTE_NAMES["A2"]]),
        (1080, [EXTENDED_NOTE_NAMES["A2"]]),
        (1110, [EXTENDED_NOTE_NAMES["B2"]]),  # Bb
        (1140, [EXTENDED_NOTE_NAMES["B2"]]),  # Bb
        (1170, [EXTENDED_NOTE_NAMES["C3"]]),
        (1200, [EXTENDED_NOTE_NAMES["C3"]]),
        (1230, [EXTENDED_NOTE_NAMES["D3"]]),
        (1260, [EXTENDED_NOTE_NAMES["D3"]]),
        (1290, [EXTENDED_NOTE_NAMES["E3"]]),
        (1320, [EXTENDED_NOTE_NAMES["E3"]]),
        (1350, [EXTENDED_NOTE_NAMES["F3"]]),
        (1380, [EXTENDED_NOTE_NAMES["F3"]]),
        (1410, [EXTENDED_NOTE_NAMES["G3"]]),
        (1440, [EXTENDED_NOTE_NAMES["G3"]]),
        # Bridge — back to A major
        (1470, {"key_change": "A_major"}),
        (1500, [EXTENDED_NOTE_NAMES["A2"]]),
        (1530, [EXTENDED_NOTE_NAMES["G3"]]),  # G#
        (1560, [EXTENDED_NOTE_NAMES["E3"]]),
        (1590, [EXTENDED_NOTE_NAMES["C3"]]),  # C#
        (1620, [EXTENDED_NOTE_NAMES["A2"]]),
        (1650, [EXTENDED_NOTE_NAMES["G3"]]),  # G#
        (1680, [EXTENDED_NOTE_NAMES["E3"]]),
        (1710, [EXTENDED_NOTE_NAMES["C3"]]),  # C#
        # Climax
        (1800, [EXTENDED_NOTE_NAMES["A2"]]),
        (1810, [EXTENDED_NOTE_NAMES["B2"]]),
        (1820, [EXTENDED_NOTE_NAMES["C3"]]),  # C#
        (1830, [EXTENDED_NOTE_NAMES["D3"]]),
        (1840, [EXTENDED_NOTE_NAMES["E3"]]),
        (1850, [EXTENDED_NOTE_NAMES["F3"]]),  # F#
        (1860, [EXTENDED_NOTE_NAMES["G3"]]),  # G#
        (1870, [EXTENDED_NOTE_NAMES["A2"]]),
        (1880, [EXTENDED_NOTE_NAMES["B2"]]),
        (1890, [EXTENDED_NOTE_NAMES["C3"]]),  # C#
        (1900, [EXTENDED_NOTE_NAMES["D3"]]),
        (1910, [EXTENDED_NOTE_NAMES["E3"]]),
        (1920, [EXTENDED_NOTE_NAMES["F3"]]),  # F#
        (1930, [EXTENDED_NOTE_NAMES["G3"]]),  # G#
        (1940, [EXTENDED_NOTE_NAMES["A2"]]),
        (1950, [EXTENDED_NOTE_NAMES["B2"]]),
        (1960, [EXTENDED_NOTE_NAMES["C3"]]),  # C#
        (1970, [EXTENDED_NOTE_NAMES["D3"]]),
        (1980, [EXTENDED_NOTE_NAMES["E3"]]),
        (1990, [EXTENDED_NOTE_NAMES["F3"]]),  # F#
        (2000, [EXTENDED_NOTE_NAMES["G3"]]),  # G#
    ],
}

# Dictionary of available songs
SONGS = {
    "song1": SONG_1,
    "song2": SONG_2,
    "song3": SONG_3,
    "song4": SONG_4,
}
