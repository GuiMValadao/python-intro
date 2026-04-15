import pygame
import config
from config import GameState
from songs import SONGS


class Menu:
    """Base menu class with keyboard and mouse navigation support."""

    def __init__(self, game, title="Menu"):
        self.game = game
        self.title = title
        self.buttons = (
            {}
        )  # {"button_name": {"surface": surf, "rect": rect, "color": color, "label": label}}
        self.button_names = []  # Track button order for keyboard navigation
        self.button_width = 200
        self.button_height = 60
        self.selected_index = 0  # Current selection for keyboard navigation
        self.hovered_button = None  # Current button under mouse cursor

    def create_button(self, name, label, y_offset, color=(100, 100, 100)):
        """Create a button surface and rect at a specific vertical offset."""
        button_surf = pygame.Surface((self.button_width, self.button_height))
        button_surf.fill(color)

        # Render text
        font = self.game.game_font
        text = font.render(label, True, (255, 255, 255))
        text_rect = text.get_rect(
            center=(self.button_width // 2, self.button_height // 2)
        )
        button_surf.blit(text, text_rect)

        # Position button
        button_rect = pygame.Rect(
            config.DISPLAY_WIDTH // 2 - self.button_width // 2,
            y_offset,
            self.button_width,
            self.button_height,
        )

        self.buttons[name] = {
            "surface": button_surf,
            "rect": button_rect,
            "color": color,
            "label": label,
        }
        self.button_names.append(name)

    def draw(self, display_surface):
        """Draw all buttons on the display surface with white alpha overlay for highlights."""
        display_surface.fill(config.MENU_BACKGROUND)

        for i, button_name in enumerate(self.button_names):
            button_data = self.buttons[button_name]
            display_surface.blit(button_data["surface"], button_data["rect"].topleft)

            # Draw black alpha overlay if selected (keyboard or hovered)
            if i == self.selected_index:
                overlay = pygame.Surface(
                    (self.button_width, self.button_height), pygame.SRCALPHA
                )
                overlay.fill((0, 0, 0, 160))  # White with 80/255 alpha
                display_surface.blit(overlay, button_data["rect"].topleft)

    def handle_mouse_motion(self, event):
        """Handle mouse motion to detect button hover and sync keyboard selection."""
        for i, button_name in enumerate(self.button_names):
            button_data = self.buttons[button_name]
            if button_data["rect"].collidepoint(event.pos):
                # Sync keyboard selection to match the hovered button
                self.selected_index = i
                self.hovered_button = button_name
                return
        self.hovered_button = None

    def handle_key_press(self, event):
        """Handle keyboard navigation (arrow keys, enter)."""
        if event.key == pygame.K_UP:
            self.selected_index = (self.selected_index - 1) % len(self.button_names)
            self.hovered_button = None  # Clear hover when using keyboard
        elif event.key == pygame.K_DOWN:
            self.selected_index = (self.selected_index + 1) % len(self.button_names)
            self.hovered_button = None  # Clear hover when using keyboard
        elif event.key == pygame.K_RETURN:
            # Simulate click on selected button
            selected_button_name = self.button_names[self.selected_index]
            selected_button_data = self.buttons[selected_button_name]

            # Create a fake event with the selected button's rect center
            class FakeEvent:
                def __init__(self, rect):
                    self.pos = rect.center

            fake_event = FakeEvent(selected_button_data["rect"])
            return self.handle_click(fake_event)
        return True

    def handle_click(self, event):
        """Handle mouse clicks on buttons. Override in subclasses."""
        pass


class MainMenu(Menu):
    """Main game menu with Start, Options, and Quit buttons."""

    def __init__(self, game):
        super().__init__(game, title="Main Menu")

        # Create buttons
        self.create_button(
            "start", "Start", config.DISPLAY_HEIGHT // 4, color=(0, 0, 255)
        )
        self.create_button(
            "options", "Options", config.DISPLAY_HEIGHT // 4 + 80, color=(0, 255, 0)
        )
        self.create_button(
            "quit", "Quit", config.DISPLAY_HEIGHT // 4 + 160, color=(255, 0, 0)
        )

    def handle_click(self, event):
        """Handle main menu button clicks."""
        # Import GameState here to avoid circular imports
        from main import GameState

        for button_name, button_data in self.buttons.items():
            if button_data["rect"].collidepoint(event.pos):
                if button_name == "start":
                    self.game.set_state(GameState.PLAY)
                    return True
                elif button_name == "options":
                    self.game.set_state(GameState.OPTIONS)
                    return True
                elif button_name == "quit":
                    return False
        return True


class OptionsMenu(Menu):
    """Options menu for difficulty selection."""

    def __init__(self, game):
        super().__init__(game, title="Options")

        # Create difficulty buttons
        self.create_button(
            "easy", "Easy", config.DISPLAY_HEIGHT // 4, color=(0, 255, 0)
        )
        self.create_button(
            "medium", "Medium", config.DISPLAY_HEIGHT // 4 + 80, color=(255, 255, 0)
        )
        self.create_button(
            "hard", "Hard", config.DISPLAY_HEIGHT // 4 + 160, color=(255, 0, 0)
        )
        self.create_button(
            "back", "Back", config.DISPLAY_HEIGHT // 4 + 240, color=(128, 128, 128)
        )

    def draw(self, display_surface):
        """Draw options menu with highlighting for current difficulty."""
        super().draw(display_surface)

        # Draw additional highlight for current difficulty setting
        current_difficulty = config.DIFFICULTY.lower()
        if current_difficulty in self.buttons:
            rect = self.buttons[current_difficulty]["rect"]
            # Draw a gold/yellow indicator on the right side
            pygame.draw.rect(
                display_surface,
                (255, 215, 0),
                (rect.right + 10, rect.top, 5, rect.height),
            )

    def handle_click(self, event):
        """Handle options menu button clicks."""
        # Import GameState here to avoid circular imports
        from main import GameState

        for button_name, button_data in self.buttons.items():
            if button_data["rect"].collidepoint(event.pos):
                if button_name == "easy":
                    config.DIFFICULTY = "Easy"
                elif button_name == "medium":
                    config.DIFFICULTY = "Medium"
                elif button_name == "hard":
                    config.DIFFICULTY = "Hard"
                elif button_name == "back":
                    self.game.set_state(GameState.MENU)
                    return True
        return True


class PauseMenu(Menu):
    """Pause menu with song selection and resume/quit options."""

    def __init__(self, game):
        super().__init__(game, title="Pause Menu")
        self.button_width = 250  # Wider for song names

        # Create resume button
        self.create_button(
            "resume", "Resume", config.DISPLAY_HEIGHT // 4 - 60, color=(100, 150, 100)
        )

        # Create song selection buttons from SONGS dictionary
        y_offset = config.DISPLAY_HEIGHT // 4 + 20
        for i, song_key in enumerate(sorted(SONGS.keys())):
            display_name = f"Song: {song_key.replace('song', '').upper()}"
            color = (
                (100, 100, 200) if song_key == config.CURRENT_SONG else (80, 80, 150)
            )
            self.create_button(song_key, display_name, y_offset + (i * 70), color=color)

        # Create quit button
        quit_y = config.DISPLAY_HEIGHT // 4 + 20 + (len(SONGS) * 70)
        self.create_button("menu", "Return to Menu", quit_y, color=(150, 100, 100))

    def draw(self, display_surface):
        """Draw pause menu with current song highlight."""
        # Draw semi-transparent overlay
        overlay = pygame.Surface(
            (config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT), pygame.SRCALPHA
        )
        overlay.fill((0, 0, 0, 128))  # Black with 50% alpha
        display_surface.blit(overlay, (0, 0))

        # Draw pause title
        title = self.game.game_font.render("PAUSED", True, (255, 255, 255))
        title_rect = title.get_rect(center=(config.DISPLAY_WIDTH // 2, 50))
        display_surface.blit(title, title_rect)

        # Draw all buttons with selection highlight
        for i, button_name in enumerate(self.button_names):
            button_data = self.buttons[button_name]

            # Update color for current song
            if button_name in SONGS:
                if button_name == config.CURRENT_SONG:
                    button_data["color"] = (100, 200, 100)  # Brighter for current
                else:
                    button_data["color"] = (80, 80, 150)  # Darker for others

                # Redraw button surface with updated color
                button_surf = pygame.Surface((self.button_width, self.button_height))
                button_surf.fill(button_data["color"])
                font = self.game.game_font
                text = font.render(button_data["label"], True, (255, 255, 255))
                text_rect = text.get_rect(
                    center=(self.button_width // 2, self.button_height // 2)
                )
                button_surf.blit(text, text_rect)
                button_data["surface"] = button_surf

            display_surface.blit(button_data["surface"], button_data["rect"].topleft)

            # Draw selection highlight
            if i == self.selected_index:
                overlay = pygame.Surface(
                    (self.button_width, self.button_height), pygame.SRCALPHA
                )
                overlay.fill((255, 255, 255, 100))  # White highlight
                display_surface.blit(overlay, button_data["rect"].topleft)

    def handle_click(self, event):
        """Handle pause menu button clicks."""
        for button_name, button_data in self.buttons.items():
            if button_data["rect"].collidepoint(event.pos):
                if button_name == "resume":
                    self.game.set_state(GameState.PLAY)
                    return True
                elif button_name in SONGS:
                    config.CURRENT_SONG = button_name
                    return True
                elif button_name == "menu":
                    self.game.set_state(GameState.MENU)
                    return True
        return True
