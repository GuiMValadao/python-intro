import pygame
import config
from config import GameState
from entities import Player
from events import BattleEvent, load_sound
from menu import MainMenu, OptionsMenu, PauseMenu


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

        # Load sounds for note keys using key bindings from config
        # Includes natural notes, sharps (SHIFT+key), and flats (CTRL+key)
        self.note_sounds = {}
        for key in config.get_all_playable_keys():
            note_name = config.NOTE_NAMES[key]
            # Natural note
            freq = config.get_note_frequency(key, 0)
            if freq:
                self.note_sounds[(key, 0)] = load_sound(note_name, freq)
            # Sharp (SHIFT modifier)
            freq_sharp = config.get_note_frequency(key, pygame.KMOD_SHIFT)
            if freq_sharp:
                self.note_sounds[(key, pygame.KMOD_SHIFT)] = load_sound(
                    note_name + "#", freq_sharp
                )
            # Flat (CTRL modifier)
            freq_flat = config.get_note_frequency(key, pygame.KMOD_CTRL)
            if freq_flat:
                self.note_sounds[(key, pygame.KMOD_CTRL)] = load_sound(
                    note_name + "b", freq_flat
                )

        # Initialize menus
        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)
        self.pause_menu = PauseMenu(self)

    def reset_game(self):
        """Reset all game entities to their initial state without recreating pygame."""
        # Reset player
        self.player = Player(self)

        # Reset battle event
        self.battle_event = None

        # Recreate menus to reset their state
        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)
        self.pause_menu = PauseMenu(self)

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

        if new_state == GameState.MENU:
            # Reset all game state when returning to menu
            self.reset_game()
        elif new_state == GameState.OPTIONS:
            # Reset options menu selection
            self.options_menu.selected_index = 0
            self.options_menu.hovered_button = None
        elif new_state == GameState.PAUSE:
            # Reset pause menu selection
            self.pause_menu.selected_index = 0
            self.pause_menu.hovered_button = None
        elif new_state == GameState.VICTORY:
            pass  # Keep the battle_event for display

    def handle_input(self, event):
        """Centralized input handling based on current state."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and (
                self.current_state == GameState.MENU
                or self.current_state == GameState.VICTORY
            ):
                return False  # Quit game

            if self.current_state == GameState.MENU:
                return self.handle_menu_input(event)
            elif self.current_state == GameState.OPTIONS:
                return self.handle_options_input(event)
            elif self.current_state == GameState.PLAY:
                return self.handle_play_input(event)
            elif self.current_state == GameState.PAUSE:
                return self.handle_pause_input(event)
            elif self.current_state == GameState.VICTORY:
                return self.handle_victory_input(event)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.current_state == GameState.MENU:
                return self.handle_menu_click(event)
            elif self.current_state == GameState.OPTIONS:
                return self.handle_options_click(event)
            elif self.current_state == GameState.PAUSE:
                return self.handle_pause_click(event)

        elif event.type == pygame.MOUSEMOTION:
            return self.handle_mouse_motion(event)

        return True

    def handle_menu_input(self, event):
        """Handle menu keyboard input."""
        return self.main_menu.handle_key_press(event)

    def handle_menu_click(self, event):
        """Handle menu mouse input."""
        return self.main_menu.handle_click(event)

    def handle_options_input(self, event):
        """Handle options keyboard input."""
        return self.options_menu.handle_key_press(event)

    def handle_options_click(self, event):
        """Handle options mouse input."""
        return self.options_menu.handle_click(event)

    def handle_pause_input(self, event):
        """Handle pause menu keyboard input."""
        return self.pause_menu.handle_key_press(event)

    def handle_pause_click(self, event):
        """Handle pause menu mouse input."""
        return self.pause_menu.handle_click(event)

    def handle_play_input(self, event):
        """Handle play keyboard input."""
        if event.key == pygame.K_p:
            self.set_state(GameState.PAUSE)
        elif event.key == pygame.K_m:
            self.set_state(GameState.MENU)
        elif event.key == pygame.K_b:
            if self.battle_event is None:
                self.battle_event = BattleEvent(self)
            else:
                self.battle_event = None
        elif event.key in config.get_all_playable_keys():
            # Extract modifier (SHIFT or CTRL for accidentals)
            modifier = event.mod & (pygame.KMOD_SHIFT | pygame.KMOD_CTRL)
            sound_key = (event.key, modifier)
            if sound_key in self.note_sounds:
                self.note_sounds[sound_key].play()
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

            # Only move player when actually playing (not paused)
            self.player.move()

    def draw(self):
        """Draw based on current state."""
        if self.current_state == GameState.MENU:
            self.draw_menu()
        elif self.current_state == GameState.OPTIONS:
            self.draw_options()
        elif self.current_state == GameState.PLAY:
            self.draw_play()
        elif self.current_state == GameState.PAUSE:
            self.draw_pause()
        elif self.current_state == GameState.VICTORY:
            self.draw_victory()

    def draw_menu(self):
        """Draw menu screen."""
        self.main_menu.draw(self.display_surface)

    def draw_options(self):
        """Draw options screen."""
        self.options_menu.draw(self.display_surface)

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

    def draw_pause(self):
        """Draw pause menu over the game."""
        # First draw the game in background
        self.display_surface.blit(self.BACKGROUND, (0, 0))
        self.player.draw()
        if self.battle_event:
            self.display_surface.blit(self.BATTLE_BACKGROUND, (0, 0))
            self.battle_event.draw()

        # Then draw pause menu on top
        self.pause_menu.draw(self.display_surface)

    def handle_mouse_motion(self, event):
        """Handle mouse motion for menu hover effects."""
        if self.current_state == GameState.MENU:
            self.main_menu.handle_mouse_motion(event)
        elif self.current_state == GameState.OPTIONS:
            self.options_menu.handle_mouse_motion(event)
        elif self.current_state == GameState.PAUSE:
            self.pause_menu.handle_mouse_motion(event)
        return True

    def _pause(self):
        """Legacy pause method - now handled by PAUSE state."""
        pass


def main():

    print("Iniciando o jogo")

    game = Game()
    # Run the main game loop
    game.run()
    print("Fim de jogo")


if __name__ == "__main__":
    main()
