import pygame
from pathlib import Path
from enum import Enum

ROOT_PATH = Path(__file__).parent


class GameState(Enum):
    """Game state enumeration."""

    MENU = "menu"
    OPTIONS = "options"
    PLAY = "play"
    VICTORY = "victory"
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
NUMBER_BUTTONS = 5  # Default number of buttons
CURRENT_SONG = "song2"  # variable to change the song to play

# Key bindings - maps pygame keys to note names
# Can be easily remapped for different key layouts
KEY_BINDINGS = {
    pygame.K_a: "a",  # A3
    pygame.K_s: "s",  # B3
    pygame.K_d: "d",  # C4
    pygame.K_f: "f",  # D4
    pygame.K_g: "g",  # E4
    pygame.K_h: "h",  # F4
    pygame.K_j: "j",  # G4
}

# Musical note frequencies (Hz)
NOTE_FREQUENCIES = {
    pygame.K_a: 220,  # A3
    pygame.K_s: 247,  # B3
    pygame.K_d: 262,  # C4
    pygame.K_f: 294,  # D4
    pygame.K_g: 330,  # E4
    pygame.K_h: 349,  # F4
    pygame.K_j: 392,  # G4
}
