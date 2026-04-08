import pygame
from pathlib import Path

ROOT_PATH = Path(__file__).parent

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

# Musical note frequencies (Hz)
NOTE_FREQUENCIES = {
    pygame.K_a: 220,  # A4
    pygame.K_s: 247,  # B4
    pygame.K_d: 262,  # C4
    pygame.K_f: 294,  # D4
    pygame.K_g: 330,  # E4
    pygame.K_h: 349,  # F4
    pygame.K_j: 392,  # G4
}
