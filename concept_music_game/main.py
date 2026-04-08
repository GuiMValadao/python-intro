import pygame
import config
from enum import Enum
from entities import Player
from events import BattleEvent, load_sound


class GameState(Enum):
    MENU = "menu"
    OPTIONS = "options"
    PLAY = "play"
    VICTORY = "victory"


class Game:

    def __init__(self):
        print("Inicializing PyGame")
        pygame.init()
        self.display_surface = pygame.display.set_mode(
            (config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT)
        )
        pygame.display.set_caption("Concept of Music Game")
        self.game_font = pygame.font.SysFont("Bauhaus 93", 30)

        # Sets a background image
        BACKGROUND = pygame.image.load(
            config.ROOT_PATH / "images/background1.png"
        ).convert()
        self.BACKGROUND = pygame.transform.scale(
            BACKGROUND, (config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT)
        )

        self.BATTLE_BACKGROUND = pygame.transform.scale(
            pygame.image.load(
                config.ROOT_PATH / "images/background_battle.png"
            ).convert(),
            (config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT),
        )

        self.clock = pygame.time.Clock()
        self.player = Player(self)
        self.current_state = GameState.MENU
        self.battle_event = None

        # Load sounds for note keys
        key_names = {
            pygame.K_a: "a",
            pygame.K_s: "s",
            pygame.K_d: "d",
            pygame.K_f: "f",
            pygame.K_g: "g",
            pygame.K_h: "h",
            pygame.K_j: "j",
        }
        self.note_sounds = {
            key: load_sound(key_names[key], freq)
            for key, freq in config.NOTE_FREQUENCIES.items()
        }

    def run(self):
        """Main game loop using state management."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    if not self.handle_input(event):
                        running = False

            self.update()
            self.draw()
            pygame.display.flip()
            self.clock.tick(config.FRAME_REFRESH_RATE)

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
        elif event.key == pygame.K_m:
            self.set_state(GameState.MENU)
        elif event.key == pygame.K_b:
            if self.battle_event is None:
                self.battle_event = BattleEvent(self)
            else:
                self.battle_event = None
        elif event.key in config.NOTE_FREQUENCIES:
            self.note_sounds[event.key].play()
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
                self.player.load_image(
                    config.ROOT_PATH / "images/player/player_right.png"
                )
            elif keys[pygame.K_LEFT]:
                self.player.load_image(
                    config.ROOT_PATH / "images/player/player_left.png"
                )
            elif keys[pygame.K_UP]:
                self.player.load_image(config.ROOT_PATH / "images/player/player_up.png")
            elif keys[pygame.K_DOWN]:
                self.player.load_image(config.ROOT_PATH / "images/player/player.png")

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
        self.display_surface.fill(config.MENU_BACKGROUND)
        self.display_surface.blit(self.BATTLE_BACKGROUND, (0, 0))
        title_text = self.game_font.render("Victory!", True, (255, 255, 255))
        info_text = self.game_font.render(
            "Press M to return to menu or Q to quit", True, (255, 255, 255)
        )
        self.display_surface.blit(
            title_text,
            (
                (config.DISPLAY_WIDTH - title_text.get_width()) // 2,
                config.DISPLAY_HEIGHT // 3,
            ),
        )
        self.display_surface.blit(
            info_text,
            (
                (config.DISPLAY_WIDTH - info_text.get_width()) // 2,
                config.DISPLAY_HEIGHT // 2,
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
            config.DISPLAY_WIDTH // 2 - button_width // 2,
            config.DISPLAY_HEIGHT // 4,
            button_width,
            button_height,
        )
        self.menu_options_rect = pygame.Rect(
            config.DISPLAY_WIDTH // 2 - button_width // 2,
            config.DISPLAY_HEIGHT // 4 + 80,
            button_width,
            button_height,
        )
        self.menu_quit_rect = pygame.Rect(
            config.DISPLAY_WIDTH // 2 - button_width // 2,
            config.DISPLAY_HEIGHT // 4 + 160,
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
            config.DISPLAY_WIDTH // 2 - button_width // 2,
            config.DISPLAY_HEIGHT // 4,
            button_width,
            button_height,
        )
        self.options_medium_rect = pygame.Rect(
            config.DISPLAY_WIDTH // 2 - button_width // 2,
            config.DISPLAY_HEIGHT // 4 + 80,
            button_width,
            button_height,
        )
        self.options_hard_rect = pygame.Rect(
            config.DISPLAY_WIDTH // 2 - button_width // 2,
            config.DISPLAY_HEIGHT // 4 + 160,
            button_width,
            button_height,
        )
        self.options_back_rect = pygame.Rect(
            config.DISPLAY_WIDTH // 2 - button_width // 2,
            config.DISPLAY_HEIGHT // 4 + 240,
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
            config.DIFFICULTY = "Easy"
        elif self.options_medium_rect.collidepoint(event.pos):
            config.DIFFICULTY = "Medium"
        elif self.options_hard_rect.collidepoint(event.pos):
            config.DIFFICULTY = "Hard"
        elif self.options_back_rect.collidepoint(event.pos):
            self.set_state(GameState.MENU)
        return True

    def draw_menu(self):
        """Draw the menu screen."""
        self.display_surface.fill(config.MENU_BACKGROUND)
        if hasattr(self, "menu_surfaces"):
            for surface, rect in self.menu_surfaces.values():
                self.display_surface.blit(surface, rect.topleft)

    def draw_options(self):
        """Draw the options screen."""
        self.display_surface.fill(config.MENU_BACKGROUND)
        if hasattr(self, "options_surfaces"):
            for surface, rect in self.options_surfaces.values():
                self.display_surface.blit(surface, rect.topleft)


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
