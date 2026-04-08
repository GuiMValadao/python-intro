import pygame
from pathlib import Path
from math import sqrt
from random import randint
import numpy as np
from songs import SONGS
from enum import Enum

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
CURRENT_SONG = "song1"  # variable to change the song to play

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


class GameState(Enum):
    MENU = "menu"
    OPTIONS = "options"
    PLAY = "play"
    VICTORY = "victory"


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


class Game:

    def __init__(self):
        print("Inicializing PyGame")
        pygame.init()
        self.display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption("Concept of Music Game")
        self.game_font = pygame.font.SysFont("Bauhaus 93", 30)

        # Sets a background image
        BACKGROUND = pygame.image.load(ROOT_PATH / "images/background1.png").convert()
        self.BACKGROUND = pygame.transform.scale(
            BACKGROUND, (DISPLAY_WIDTH, DISPLAY_HEIGHT)
        )

        self.BATTLE_BACKGROUND = pygame.transform.scale(
            pygame.image.load(ROOT_PATH / "images/background_battle.png").convert(),
            (DISPLAY_WIDTH, DISPLAY_HEIGHT),
        )

        self.clock = pygame.time.Clock()
        self.player = Player(self)
        self.current_state = GameState.MENU
        self.battle_event = None

    def run(self):
        """Main game loop using state management."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    running = self.handle_input(event)

            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(FRAME_REFRESH_RATE)

        pygame.quit()

    def set_state(self, new_state):
        """Transition to a new game state."""
        self.current_state = new_state
        # Don't auto-create battle_event - let the B key handle it
        if new_state == GameState.MENU:
            self.battle_event = None
        elif new_state == GameState.VICTORY:
            pass  # Keep the battle_event for display

    def handle_input(self, event):
        """Centralized input handling based on current state."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                return False  # Quit game

            if self.current_state == GameState.MENU:
                return self.handle_menu_input(event)
            elif self.current_state == GameState.OPTIONS:
                return self.handle_options_input(event)
            elif self.current_state == GameState.PLAY:
                return self.handle_play_input(event)
            elif self.current_state == GameState.VICTORY:
                return self.handle_victory_input(event)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.current_state == GameState.MENU:
                return self.handle_menu_click(event)
            elif self.current_state == GameState.OPTIONS:
                return self.handle_options_click(event)

        return True

    def handle_menu_input(self, event):
        """Handle menu keyboard input."""
        return True

    def handle_menu_click(self, event):
        """Handle menu mouse input."""
        return True

    def handle_options_input(self, event):
        """Handle options keyboard input."""
        return True

    def handle_options_click(self, event):
        """Handle options mouse input."""
        return True

    def handle_play_input(self, event):
        """Handle play keyboard input."""
        if event.key == pygame.K_p:
            self._pause()
        elif event.key == pygame.K_b:
            if self.battle_event is None:
                self.battle_event = Battle_event(self)
            else:
                self.battle_event = None
        elif event.key in NOTE_FREQUENCIES:
            sound = generate_sound(NOTE_FREQUENCIES[event.key])
            sound.play()
        return True

    def handle_victory_input(self, event):
        """Handle victory screen input."""
        if event.key == pygame.K_m:
            self.set_state(GameState.MENU)
        return True

    def update(self):
        """Update game state."""
        # Get pressed keys for sprite animation
        keys = pygame.key.get_pressed()
        if self.current_state == GameState.PLAY:
            # Change player sprite based on movement keys
            if keys[pygame.K_RIGHT]:
                self.player.load_image(ROOT_PATH / "images/player/player_right.png")
            elif keys[pygame.K_LEFT]:
                self.player.load_image(ROOT_PATH / "images/player/player_left.png")
            elif keys[pygame.K_UP]:
                self.player.load_image(ROOT_PATH / "images/player/player_up.png")
            elif keys[pygame.K_DOWN]:
                self.player.load_image(ROOT_PATH / "images/player/player.png")
            else:
                self.player.load_image(ROOT_PATH / "images/player/player.png")

            if self.battle_event:
                self.battle_event.update()
                if self.battle_event.song_finished:
                    self.set_state(GameState.VICTORY)

        self.player.move()

    def draw(self):
        """Draw based on current state."""
        if self.current_state == GameState.MENU:
            self.draw_menu()
        elif self.current_state == GameState.OPTIONS:
            self.draw_options()
        elif self.current_state == GameState.PLAY:
            self.draw_play()
        elif self.current_state == GameState.VICTORY:
            self.draw_victory()

    def draw_menu(self):
        """Draw menu screen."""
        # Delegating to existing menu rendering logic
        # This will be called during draw loop
        pass

    def draw_options(self):
        """Draw options screen."""
        pass

    def draw_play(self):
        """Draw play screen."""
        self.display_surface.blit(self.BACKGROUND, (0, 0))
        self.player.draw()

        if self.battle_event:
            self.display_surface.blit(self.BATTLE_BACKGROUND, (0, 0))
            self.battle_event.draw()
            score_surface = self.game_font.render(
                f"Score: {self.battle_event.score}", True, (255, 255, 255)
            )
            self.display_surface.blit(score_surface, (20, 20))

    def draw_victory(self):
        """Draw victory screen."""
        self.display_surface.fill(MENU_BACKGROUND)
        self.display_surface.blit(self.BATTLE_BACKGROUND, (0, 0))
        title_text = self.game_font.render("Victory!", True, (255, 255, 255))
        info_text = self.game_font.render(
            "Press M to return to menu or Q to quit", True, (255, 255, 255)
        )
        self.display_surface.blit(
            title_text,
            (
                (DISPLAY_WIDTH - title_text.get_width()) // 2,
                DISPLAY_HEIGHT // 3,
            ),
        )
        self.display_surface.blit(
            info_text,
            (
                (DISPLAY_WIDTH - info_text.get_width()) // 2,
                DISPLAY_HEIGHT // 2,
            ),
        )

    def _pause(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False
                        break

    def menu(self):
        # Create and cache button surfaces
        button_width, button_height = 200, 60
        start_surf = pygame.Surface((button_width, button_height))
        options_surf = pygame.Surface((button_width, button_height))
        quit_surf = pygame.Surface((button_width, button_height))
        start_surf.fill((0, 0, 255))  # Blue
        options_surf.fill((0, 255, 0))  # Green
        quit_surf.fill((255, 0, 0))  # Red

        # Render text
        start_text = self.game_font.render("Start", True, (255, 255, 255))
        options_text = self.game_font.render("Options", True, (255, 255, 255))
        quit_text = self.game_font.render("Quit", True, (255, 255, 255))

        # Blit text onto surfaces
        start_surf.blit(
            start_text,
            (
                (button_width - start_text.get_width()) // 2,
                (button_height - start_text.get_height()) // 2,
            ),
        )
        options_surf.blit(
            options_text,
            (
                (button_width - options_text.get_width()) // 2,
                (button_height - options_text.get_height()) // 2,
            ),
        )
        quit_surf.blit(
            quit_text,
            (
                (button_width - quit_text.get_width()) // 2,
                (button_height - quit_text.get_height()) // 2,
            ),
        )

        # Button positions
        self.menu_start_rect = pygame.Rect(
            DISPLAY_WIDTH // 2 - button_width // 2,
            DISPLAY_HEIGHT // 4,
            button_width,
            button_height,
        )
        self.menu_options_rect = pygame.Rect(
            DISPLAY_WIDTH // 2 - button_width // 2,
            DISPLAY_HEIGHT // 4 + 80,
            button_width,
            button_height,
        )
        self.menu_quit_rect = pygame.Rect(
            DISPLAY_WIDTH // 2 - button_width // 2,
            DISPLAY_HEIGHT // 4 + 160,
            button_width,
            button_height,
        )

        self.menu_surfaces = {
            "start": (start_surf, self.menu_start_rect),
            "options": (options_surf, self.menu_options_rect),
            "quit": (quit_surf, self.menu_quit_rect),
        }

    def handle_menu_click(self, event):
        """Handle menu button clicks."""
        if self.menu_start_rect.collidepoint(event.pos):
            self.set_state(GameState.PLAY)
        elif self.menu_options_rect.collidepoint(event.pos):
            self.options_menu()
            self.set_state(GameState.OPTIONS)
        elif self.menu_quit_rect.collidepoint(event.pos):
            return False
        return True

    def options_menu(self):
        global DIFFICULTY, NUMBER_BUTTONS
        # Create and cache button surfaces
        button_width, button_height = 200, 60
        easy_surf = pygame.Surface((button_width, button_height))
        medium_surf = pygame.Surface((button_width, button_height))
        hard_surf = pygame.Surface((button_width, button_height))
        back_surf = pygame.Surface((button_width, button_height))
        easy_surf.fill((0, 255, 0))  # Green
        medium_surf.fill((255, 255, 0))  # Yellow
        hard_surf.fill((255, 0, 0))  # Red
        back_surf.fill((128, 128, 128))  # Gray

        # Render text
        easy_text = self.game_font.render("Easy", True, (0, 0, 0))
        medium_text = self.game_font.render("Medium", True, (0, 0, 0))
        hard_text = self.game_font.render("Hard", True, (0, 0, 0))
        back_text = self.game_font.render("Back", True, (0, 0, 0))

        # Blit text
        easy_surf.blit(
            easy_text,
            (
                (button_width - easy_text.get_width()) // 2,
                (button_height - easy_text.get_height()) // 2,
            ),
        )
        medium_surf.blit(
            medium_text,
            (
                (button_width - medium_text.get_width()) // 2,
                (button_height - medium_text.get_height()) // 2,
            ),
        )
        hard_surf.blit(
            hard_text,
            (
                (button_width - hard_text.get_width()) // 2,
                (button_height - hard_text.get_height()) // 2,
            ),
        )
        back_surf.blit(
            back_text,
            (
                (button_width - back_text.get_width()) // 2,
                (button_height - back_text.get_height()) // 2,
            ),
        )

        # Button positions
        self.options_easy_rect = pygame.Rect(
            DISPLAY_WIDTH // 2 - button_width // 2,
            DISPLAY_HEIGHT // 4,
            button_width,
            button_height,
        )
        self.options_medium_rect = pygame.Rect(
            DISPLAY_WIDTH // 2 - button_width // 2,
            DISPLAY_HEIGHT // 4 + 80,
            button_width,
            button_height,
        )
        self.options_hard_rect = pygame.Rect(
            DISPLAY_WIDTH // 2 - button_width // 2,
            DISPLAY_HEIGHT // 4 + 160,
            button_width,
            button_height,
        )
        self.options_back_rect = pygame.Rect(
            DISPLAY_WIDTH // 2 - button_width // 2,
            DISPLAY_HEIGHT // 4 + 240,
            button_width,
            button_height,
        )

        self.options_surfaces = {
            "easy": (easy_surf, self.options_easy_rect),
            "medium": (medium_surf, self.options_medium_rect),
            "hard": (hard_surf, self.options_hard_rect),
            "back": (back_surf, self.options_back_rect),
        }

    def handle_options_click(self, event):
        """Handle options menu button clicks."""
        if self.options_easy_rect.collidepoint(event.pos):
            global DIFFICULTY, NUMBER_BUTTONS
            DIFFICULTY = "Easy"
            NUMBER_BUTTONS = 3
        elif self.options_medium_rect.collidepoint(event.pos):
            DIFFICULTY = "Medium"
            NUMBER_BUTTONS = 5
        elif self.options_hard_rect.collidepoint(event.pos):
            DIFFICULTY = "Hard"
            NUMBER_BUTTONS = 7
        elif self.options_back_rect.collidepoint(event.pos):
            self.set_state(GameState.MENU)
        return True

    def draw_menu(self):
        """Draw the menu screen."""
        self.display_surface.fill(MENU_BACKGROUND)
        if hasattr(self, "menu_surfaces"):
            for surface, rect in self.menu_surfaces.values():
                self.display_surface.blit(surface, rect.topleft)

    def draw_options(self):
        """Draw the options screen."""
        self.display_surface.fill(MENU_BACKGROUND)
        if hasattr(self, "options_surfaces"):
            for surface, rect in self.options_surfaces.values():
                self.display_surface.blit(surface, rect.topleft)


class GameObject:
    def load_image(self, filename):
        self.image = pygame.image.load(filename).convert()
        # Sets the image backgound colour to be invisible
        self.image.set_colorkey((255, 255, 255))
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def rect(self):
        return pygame.Rect(self.position.x, self.position.y, self.width, self.height)

    def draw(self):
        self.game.display_surface.blit(self.image, (self.position.x, self.position.y))


class Player(GameObject):

    def __init__(self, game):
        self.game = game
        self.position = pygame.Vector2(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)
        self.load_image(ROOT_PATH / "images/player/player.png")
        self.PLAYER_SPEED = PLAYER_SPEED

    def move_right(self, right):
        if right:
            self.position.x += self.PLAYER_SPEED
        if self.position.x + self.width > DISPLAY_WIDTH:
            self.position.x = DISPLAY_WIDTH - self.width

    def move_left(self, left):
        if left:
            self.position.x -= self.PLAYER_SPEED
        if self.position.x < 0:
            self.position.x = 0

    def move_up(self, up):
        if up:
            self.position.y = self.position.y - self.PLAYER_SPEED
        if self.position.y < 0:
            self.position.y = 0

    def move_down(self, down):
        if down:
            self.position.y = self.position.y + self.PLAYER_SPEED
        if self.position.y + self.height > DISPLAY_HEIGHT:
            self.position.y = DISPLAY_HEIGHT - self.height

    def move(self):
        global PLAYER_SPEED
        keys = pygame.key.get_pressed()
        right = keys[pygame.K_RIGHT]
        left = keys[pygame.K_LEFT]
        up = keys[pygame.K_UP]
        down = keys[pygame.K_DOWN]

        # Calculate if moving diagonally
        is_diagonal = (right or left) and (up or down)
        self.PLAYER_SPEED = PLAYER_SPEED / sqrt(2) if is_diagonal else PLAYER_SPEED

        # Apply movement
        if right:
            self.move_right(True)
        if left:
            self.move_left(True)
        if up:
            self.move_up(True)
        if down:
            self.move_down(True)


class Staff(GameObject):
    def __init__(self, game):
        self.game = game
        self.position = pygame.Vector2(50, DISPLAY_HEIGHT / 2)
        self.load_image(ROOT_PATH / "images/staff.png")
        self.buttons = []
        # Create 7 fixed buttons
        for i in range(7):
            button = Button(self.game, i)
            button.position = pygame.Vector2(self.position.x, self.position.y + i * 30)
            self.buttons.append(button)

    def draw(self):
        super().draw()
        for button in self.buttons:
            button.draw()


class Button(GameObject):
    def __init__(self, game, index):
        self.game = game
        self.index = index
        self.key = [
            pygame.K_a,
            pygame.K_s,
            pygame.K_d,
            pygame.K_f,
            pygame.K_g,
            pygame.K_h,
            pygame.K_j,
        ][index]
        self.load_image(ROOT_PATH / f"images/buttons/button{index+1}.png")


class MovingBlock(GameObject):
    def __init__(self, game, target_button):
        self.game = game
        self.target = target_button
        self.speed = 3
        self.load_image(ROOT_PATH / "images/moving_block.png")
        self.position = pygame.Vector2(
            DISPLAY_WIDTH - self.width, self.target.position.y
        )
        direction = self.target.position - self.position
        if direction.length() > 0:
            self.direction = direction.normalize()
        else:
            self.direction = pygame.Vector2(-1, 0)  # fallback
        # Apply color mask based on target button
        colors = [
            (255, 255, 0),  # button 1 (index 0)
            (0, 0, 255),  # button 2
            (0, 255, 255),  # button 3
            (255, 0, 0),  # button 4
            (0, 255, 0),  # button 5
            (255, 125, 0),  # button 6
            (255, 255, 255),  # button 7
        ]
        color = colors[self.target.index]
        self.image = self.image.copy()
        self.image.fill(color, special_flags=pygame.BLEND_MULT)

    def update(self):
        self.position += self.direction * self.speed

    def is_colliding(self):
        return self.rect().colliderect(self.target.rect())


class Battle_event:
    def __init__(self, game):
        self.game = game
        self.staff = Staff(game)
        self.moving_blocks = []
        self.spawn_timer = 0
        self.score = 0
        self.previous_keys = pygame.key.get_pressed()
        # Generate sounds for each button
        self.sounds = {
            key: generate_sound(freq) for key, freq in NOTE_FREQUENCIES.items()
        }
        # Load song
        self.song = SONGS[CURRENT_SONG]
        self.song_index = 0
        self.song_finished = False

    def update(self):
        self.spawn_timer += 1
        current_keys = pygame.key.get_pressed()

        # Spawn blocks based on song
        if (
            self.song_index < len(self.song)
            and self.spawn_timer >= self.song[self.song_index][0]
        ):
            _, note_key = self.song[self.song_index]
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


def main():

    print("Iniciando o jogo")

    game = Game()
    # Initialize menu UI
    game.menu()
    game.options_menu()
    # Run the main game loop
    game.run()
    print("Fim de jogo")


if __name__ == "__main__":
    main()
