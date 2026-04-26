import config
import pygame
import maps

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
        self.game_font = pygame.font.SysFont(config.GAME_FONT, 30)

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
        self.current_state = config.GameState.MENU
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
            freq_sharp = config.get_note_frequency(key, config.SHARP_MODIFIER)
            if freq_sharp:
                self.note_sounds[(key, config.SHARP_MODIFIER)] = load_sound(
                    note_name + "#", freq_sharp
                )
            # Flat (CTRL modifier)
            freq_flat = config.get_note_frequency(key, config.FLAT_MODIFIER)
            if freq_flat:
                self.note_sounds[(key, config.FLAT_MODIFIER)] = load_sound(
                    note_name + "b", freq_flat
                )
        # Initialize menus
        self.main_menu = MainMenu(self)
        self.options_menu = OptionsMenu(self)
        self.pause_menu = PauseMenu(self)

        # Add maps
        self.maps = maps.load_maps()
        self.current_map = self.maps["town_square"]
        self.camera = maps.Camera(self.current_map.width, self.current_map.height)
        self.player.position = self.current_map.spawn_point.copy()

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

        if new_state == config.GameState.MENU:
            # Reset all game state when returning to menu
            self.reset_game()
        elif new_state == config.GameState.OPTIONS:
            # Reset options menu selection
            self.options_menu.selected_index = 0
            self.options_menu.hovered_button = None
        elif new_state == config.GameState.PAUSE:
            # Reset pause menu selection
            self.pause_menu.selected_index = 0
            self.pause_menu.hovered_button = None
        elif new_state == config.GameState.SONG_END:
            pass  # Keep the battle_event for statistics display

    def handle_input(self, event):
        """Centralized input handling based on current state."""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and (
                self.current_state == config.GameState.MENU
            ):
                return False  # Quit game

            if self.current_state == config.GameState.MENU:
                return self.handle_menu_input(event)
            elif self.current_state == config.GameState.OPTIONS:
                return self.handle_options_input(event)
            elif self.current_state == config.GameState.PLAY:
                return self.handle_play_input(event)
            elif self.current_state == config.GameState.PAUSE:
                return self.handle_pause_input(event)
            elif self.current_state == config.GameState.SONG_END:
                return self.handle_song_end_input(event)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if self.current_state == config.GameState.MENU:
                return self.handle_menu_click(event)
            elif self.current_state == config.GameState.OPTIONS:
                return self.handle_options_click(event)
            elif self.current_state == config.GameState.PAUSE:
                return self.handle_pause_click(event)

        elif event.type == pygame.MOUSEMOTION:
            return self.handle_mouse_motion(event)

        return True

    def handle_menu_input(self, event):
        """Handle menu keyboard input."""
        if event.key == pygame.K_q:
            return False  # Quit from menu
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
            self.set_state(config.GameState.PAUSE)
        elif event.key == pygame.K_m:
            self.set_state(config.GameState.MENU)
        elif event.key == pygame.K_b:
            if self.battle_event is None:
                self.battle_event = BattleEvent(self)
            else:
                self.battle_event = None
        elif event.key in config.get_all_playable_keys():
            # Normalize modifier to standard pygame constants
            if self.battle_event is None:
                modifier = 0
                if event.mod & config.SHARP_MODIFIER:
                    modifier = config.SHARP_MODIFIER
                elif event.mod & config.FLAT_MODIFIER:
                    modifier = config.FLAT_MODIFIER

                sound_key = (event.key, modifier)
                if sound_key in self.note_sounds:
                    self.note_sounds[sound_key].play()
        return True

    def handle_song_end_input(self, event):
        """Handle song end screen input."""
        if event.key == pygame.K_RETURN:
            # Return to the game world
            self.set_state(config.GameState.PLAY)
            self.battle_event = None
        if event.key == pygame.K_m:
            self.reset_game()
            self.set_state(config.GameState.MENU)
        return True

    def update(self):
        """Update game state."""
        # Get pressed keys for sprite animation
        keys = pygame.key.get_pressed()
        if self.current_state == config.GameState.PLAY:
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
                    self.set_state(config.GameState.SONG_END)

            # Only move player when actually playing (not paused)
            self.player.move()
            self.camera.follow(self.player)

    def draw(self):
        """Draw based on current state."""
        if self.current_state == config.GameState.MENU:
            self.draw_menu()
        elif self.current_state == config.GameState.OPTIONS:
            self.draw_options()
        elif self.current_state == config.GameState.PLAY:
            self.draw_play()
        elif self.current_state == config.GameState.PAUSE:
            self.draw_pause()
        elif self.current_state == config.GameState.SONG_END:
            self.draw_song_end()

    def draw_menu(self):
        """Draw menu screen."""
        self.main_menu.draw(self.display_surface)

    def draw_options(self):
        """Draw options screen."""
        self.options_menu.draw(self.display_surface)

    def draw_play(self):
        """Draw play screen."""
        self.current_map.draw(self.display_surface, self.camera)
        # Draw player at camera-adjusted position
        screen_pos = self.camera.apply(self.player.position)
        self.display_surface.blit(self.player.image, screen_pos)

        if self.battle_event:
            # Battle UI draws in screen space — no camera offset needed
            self.display_surface.blit(self.BATTLE_BACKGROUND, (0, 0))
            self.battle_event.draw()
            score_surface = self.game_font.render(
                f"Score: {self.battle_event.score}", True, (255, 255, 255)
            )
            self.display_surface.blit(score_surface, (20, 20))

    def draw_song_end(self):
        """Draw song end screen with statistics."""
        # Draw the battle background
        self.display_surface.blit(self.BATTLE_BACKGROUND, (0, 0))

        # Draw semi-transparent overlay
        overlay = pygame.Surface(
            (config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT), pygame.SRCALPHA
        )
        overlay.fill((0, 0, 0, 180))  # Dark overlay
        self.display_surface.blit(overlay, (0, 0))

        # Calculate statistics
        if self.battle_event:
            full_hits = self.battle_event.full_hits
            half_hits = self.battle_event.half_hits
            correct_notes = full_hits + (
                0.5 * half_hits
            )  # Score including fractional hits
            total_notes = len(self.battle_event.song)
            accuracy = (correct_notes / total_notes * 100) if total_notes > 0 else 0
        else:
            full_hits = 0
            half_hits = 0
            correct_notes = 0
            total_notes = 0
            accuracy = 0

        # Create a larger font for statistics
        small_font = pygame.font.SysFont(config.GAME_FONT, 24)
        medium_font = pygame.font.SysFont(config.GAME_FONT, 36)
        large_font = pygame.font.SysFont(config.GAME_FONT, 48)

        # Title
        title_text = large_font.render("Song Complete!", True, (255, 215, 0))
        title_rect = title_text.get_rect(center=(config.DISPLAY_WIDTH // 2, 80))
        self.display_surface.blit(title_text, title_rect)

        # Statistics section
        stats_y = 180
        line_height = 50

        # Perfect hits (full score)
        perfect_text = medium_font.render(
            f"Perfect Hits: {full_hits}", True, (100, 255, 100)
        )
        self.display_surface.blit(
            perfect_text,
            ((config.DISPLAY_WIDTH - perfect_text.get_width()) // 2, stats_y),
        )

        # Good hits (half score)
        good_text = medium_font.render(f"Good Hits: {half_hits}", True, (255, 200, 100))
        self.display_surface.blit(
            good_text,
            (
                (config.DISPLAY_WIDTH - good_text.get_width()) // 2,
                stats_y + line_height,
            ),
        )

        # Total notes
        total_text = medium_font.render(
            f"Total Notes: {total_notes}", True, (100, 150, 255)
        )
        self.display_surface.blit(
            total_text,
            (
                (config.DISPLAY_WIDTH - total_text.get_width()) // 2,
                stats_y + line_height * 2,
            ),
        )

        # Accuracy percentage
        accuracy_color = (
            (100, 255, 100)
            if accuracy >= 90
            else (255, 255, 100) if accuracy >= 70 else (255, 150, 100)
        )
        accuracy_text = medium_font.render(
            f"Accuracy: {accuracy:.1f}%", True, accuracy_color
        )
        self.display_surface.blit(
            accuracy_text,
            (
                (config.DISPLAY_WIDTH - accuracy_text.get_width()) // 2,
                stats_y + line_height * 3,
            ),
        )

        # Instructions
        continue_text = small_font.render(
            "Press ENTER to play again", True, (255, 255, 255)
        )
        self.display_surface.blit(
            continue_text,
            (
                (config.DISPLAY_WIDTH - continue_text.get_width()) // 2,
                stats_y + line_height * 5,
            ),
        )

        menu_text = small_font.render(
            "Press M to return to menu", True, (200, 200, 200)
        )
        self.display_surface.blit(
            menu_text,
            (
                (config.DISPLAY_WIDTH - menu_text.get_width()) // 2,
                stats_y + line_height * 5 + 50,
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
        if self.current_state == config.GameState.MENU:
            self.main_menu.handle_mouse_motion(event)
        elif self.current_state == config.GameState.OPTIONS:
            self.options_menu.handle_mouse_motion(event)
        elif self.current_state == config.GameState.PAUSE:
            self.pause_menu.handle_mouse_motion(event)
        return True

    def transition_to_map(self, map_key):
        self.current_map = self.maps[map_key]
        self.camera = maps.Camera(self.current_map.width, self.current_map.height)
        self.player.position = self.current_map.spawn_point.copy()


def main():

    print("Iniciando o jogo")

    game = Game()
    # Run the main game loop
    game.run()
    print("Fim de jogo")


if __name__ == "__main__":
    main()
