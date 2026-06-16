import pygame
import config
from config import GameState
from songs import SONGS

# ---------------------------------------------------------------------------
# Base Menu
# ---------------------------------------------------------------------------


class Menu:
    """Base menu class with keyboard and mouse navigation support."""

    def __init__(self, game, title="Menu"):
        self.game = game
        self.title = title
        self.buttons = {}
        self.button_names = []
        self.button_width = 200
        self.button_height = 60
        self.selected_index = 0
        self.hovered_button = None

    def create_button(
        self, name, label, y_offset, color=(100, 100, 100), x_center=None
    ):
        """Create a button surface and rect at a specific vertical offset."""
        button_surf = pygame.Surface((self.button_width, self.button_height))
        button_surf.fill(color)

        font = self.game.game_font
        text = font.render(label, True, (255, 255, 255))
        text_rect = text.get_rect(
            center=(self.button_width // 2, self.button_height // 2)
        )
        button_surf.blit(text, text_rect)

        cx = x_center if x_center is not None else config.DISPLAY_WIDTH // 2
        button_rect = pygame.Rect(
            cx - self.button_width // 2,
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

    def _redraw_button(self, name):
        """Redraw a button surface in-place (e.g. after a label or colour change)."""
        data = self.buttons[name]
        surf = pygame.Surface((self.button_width, self.button_height))
        surf.fill(data["color"])
        text = self.game.game_font.render(data["label"], True, (255, 255, 255))
        surf.blit(
            text,
            text.get_rect(center=(self.button_width // 2, self.button_height // 2)),
        )
        data["surface"] = surf

    def draw(self, display_surface):
        """Draw all buttons with a dark overlay on the selected one."""
        display_surface.fill(config.MENU_BACKGROUND)

        # Title
        title_font = pygame.font.SysFont(config.GAME_FONT, 36)
        title_surf = title_font.render(self.title, True, (200, 200, 200))
        title_rect = title_surf.get_rect(
            center=(config.DISPLAY_WIDTH // 2, config.DISPLAY_HEIGHT // 8)
        )
        display_surface.blit(title_surf, title_rect)

        for i, button_name in enumerate(self.button_names):
            button_data = self.buttons[button_name]
            display_surface.blit(button_data["surface"], button_data["rect"].topleft)

            if i == self.selected_index:
                overlay = pygame.Surface(
                    (self.button_width, self.button_height), pygame.SRCALPHA
                )
                overlay.fill((0, 0, 0, 160))
                display_surface.blit(overlay, button_data["rect"].topleft)

    def handle_mouse_motion(self, event):
        for i, button_name in enumerate(self.button_names):
            if self.buttons[button_name]["rect"].collidepoint(event.pos):
                self.selected_index = i
                self.hovered_button = button_name
                return
        self.hovered_button = None

    def handle_key_press(self, event):
        if event.key == pygame.K_UP:
            self.selected_index = (self.selected_index - 1) % len(self.button_names)
            self.hovered_button = None
        elif event.key == pygame.K_DOWN:
            self.selected_index = (self.selected_index + 1) % len(self.button_names)
            self.hovered_button = None
        elif event.key == pygame.K_RETURN:
            selected_data = self.buttons[self.button_names[self.selected_index]]

            class FakeEvent:
                def __init__(self, rect):
                    self.pos = rect.center

            return self.handle_click(FakeEvent(selected_data["rect"]))
        return True

    def handle_click(self, event):
        pass


# ---------------------------------------------------------------------------
# Main Menu
# ---------------------------------------------------------------------------


class MainMenu(Menu):
    def __init__(self, game):
        super().__init__(game, title="Main Menu")
        self.create_button(
            "start", "Start", config.DISPLAY_HEIGHT // 4, color=(0, 0, 255)
        )
        self.create_button(
            "options", "Options", config.DISPLAY_HEIGHT // 4 + 80, color=(0, 200, 0)
        )
        self.create_button(
            "quit", "Quit", config.DISPLAY_HEIGHT // 4 + 160, color=(255, 0, 0)
        )

    def handle_click(self, event):
        for name, data in self.buttons.items():
            if data["rect"].collidepoint(event.pos):
                if name == "start":
                    self.game.set_state(GameState.PLAY)
                    return True
                elif name == "options":
                    self.game.set_state(GameState.OPTIONS)
                    return True
                elif name == "quit":
                    return False
        return True


# ---------------------------------------------------------------------------
# Options Menu  (top-level — navigates to sub-pages)
# ---------------------------------------------------------------------------


class OptionsMenu(Menu):
    """
    Top-level options screen.  Delegates to sub-page menus for each section.
    The active sub-page (if any) intercepts all draw / input calls.
    """

    def __init__(self, game):
        super().__init__(game, title="Options")
        self.create_button(
            "difficulty", "Difficulty", config.DISPLAY_HEIGHT // 4, color=(60, 60, 180)
        )
        self.create_button(
            "keybinds",
            "Key Bindings",
            config.DISPLAY_HEIGHT // 4 + 80,
            color=(60, 60, 180),
        )
        self.create_button(
            "back", "Back", config.DISPLAY_HEIGHT // 4 + 160, color=(128, 128, 128)
        )

        # Sub-page instances — created once and reused
        self.sub_pages = {
            "difficulty": DifficultyMenu(game),
            "keybinds": KeyBindingsMenu(game),
        }
        self.active_sub_page = None

    # ------------------------------------------------------------------
    # Sub-page routing
    # ------------------------------------------------------------------

    def _open_sub_page(self, name):
        self.active_sub_page = self.sub_pages[name]
        self.active_sub_page.on_open()

    def _close_sub_page(self):
        self.active_sub_page = None

    # ------------------------------------------------------------------
    # Draw / input — delegate to sub-page when one is active
    # ------------------------------------------------------------------

    def draw(self, display_surface):
        if self.active_sub_page:
            self.active_sub_page.draw(display_surface)
        else:
            super().draw(display_surface)

    def handle_mouse_motion(self, event):
        if self.active_sub_page:
            self.active_sub_page.handle_mouse_motion(event)
        else:
            super().handle_mouse_motion(event)

    def handle_key_press(self, event):
        if self.active_sub_page:
            result = self.active_sub_page.handle_key_press(event)
            # Sub-page signals "close me" by returning the string "back"
            if result == "back":
                self._close_sub_page()
            return True
        # Escape closes options entirely
        if event.key == pygame.K_ESCAPE:
            self.game.set_state(GameState.MENU)
            return True
        return super().handle_key_press(event)

    def handle_click(self, event):
        if self.active_sub_page:
            result = self.active_sub_page.handle_click(event)
            if result == "back":
                self._close_sub_page()
            return True

        for name, data in self.buttons.items():
            if data["rect"].collidepoint(event.pos):
                if name in self.sub_pages:
                    self._open_sub_page(name)
                    return True
                elif name == "back":
                    self.game.set_state(GameState.MENU)
                    return True
        return True


# ---------------------------------------------------------------------------
# Sub-page base class
# ---------------------------------------------------------------------------


class SubMenu(Menu):
    """
    Base class for options sub-pages.
    handle_click / handle_key_press return the string "back" to signal the
    parent OptionsMenu that this page should be closed.
    """

    def on_open(self):
        """Called each time the sub-page is opened. Override to refresh state."""
        self.selected_index = 0
        self.hovered_button = None


# ---------------------------------------------------------------------------
# Difficulty sub-page
# ---------------------------------------------------------------------------


class DifficultyMenu(SubMenu):
    def __init__(self, game):
        super().__init__(game, title="Difficulty")
        self.create_button(
            "easy", "Easy", config.DISPLAY_HEIGHT // 4, color=(0, 200, 0)
        )
        self.create_button(
            "medium", "Medium", config.DISPLAY_HEIGHT // 4 + 80, color=(220, 200, 0)
        )
        self.create_button(
            "hard", "Hard", config.DISPLAY_HEIGHT // 4 + 160, color=(220, 60, 60)
        )
        self.create_button(
            "back", "Back", config.DISPLAY_HEIGHT // 4 + 260, color=(128, 128, 128)
        )

    def draw(self, display_surface):
        super().draw(display_surface)
        # Gold indicator next to the active difficulty
        current = config.DIFFICULTY.lower()
        if current in self.buttons:
            rect = self.buttons[current]["rect"]
            pygame.draw.rect(
                display_surface,
                (255, 215, 0),
                (rect.right + 10, rect.top, 5, rect.height),
            )

    def handle_click(self, event):
        for name, data in self.buttons.items():
            if data["rect"].collidepoint(event.pos):
                if name == "easy":
                    config.DIFFICULTY = "Easy"
                elif name == "medium":
                    config.DIFFICULTY = "Medium"
                elif name == "hard":
                    config.DIFFICULTY = "Hard"
                elif name == "back":
                    return "back"
        return True

    def handle_key_press(self, event):
        if event.key == pygame.K_ESCAPE:
            return "back"
        return super().handle_key_press(event)


# ---------------------------------------------------------------------------
# Key bindings sub-page
# ---------------------------------------------------------------------------

# Human-readable note labels shown in the left column
_NOTE_LABELS = ["A2", "B2", "C3", "D3", "E3", "F3", "G3"]
# Matching keys in NOTES_TO_KEYS
_NOTE_KEYS = ["A", "B", "C", "D", "E", "F", "G"]

# Layout constants
_ROW_HEIGHT = 54
_COL_NOTE_X = config.DISPLAY_WIDTH // 2 - 160  # centre of the note-label column
_COL_KEY_X = config.DISPLAY_WIDTH // 2 + 60  # centre of the key-button column
_TABLE_TOP = config.DISPLAY_HEIGHT // 5


class KeyBindingsMenu(SubMenu):
    """
    Displays a two-column table:
        Note label  |  [current key]
    Clicking a key button enters "listening" mode for that row.
    The next key press (that isn't reserved or already used) is assigned.
    """

    def __init__(self, game):
        super().__init__(game, title="Key Bindings")
        self.button_width = 80
        self.button_height = 40

        # One button per note, placed in the right column
        for i, note in enumerate(_NOTE_KEYS):
            y = _TABLE_TOP + i * _ROW_HEIGHT
            self._make_key_button(note, y)

        # Back button below the table
        back_y = _TABLE_TOP + len(_NOTE_KEYS) * _ROW_HEIGHT + 20
        self.button_width = 120
        self.create_button("back", "Back", back_y, color=(128, 128, 128))

        self.listening_for = None  # note name ("A"–"G") currently awaiting input
        self.error_message = None  # shown briefly on invalid assignment
        self.error_timer = 0

    def _make_key_button(self, note, y):
        """Create or recreate the key-display button for a note row."""
        self.button_width = 80
        key_const = config.NOTES_TO_KEYS[note]
        label = config.get_key_name(key_const)
        color = (60, 100, 160)
        # Position centred on _COL_KEY_X
        button_surf = pygame.Surface((self.button_width, self.button_height))
        button_surf.fill(color)
        font = self.game.game_font
        text = font.render(label, True, (255, 255, 255))
        button_surf.blit(
            text,
            text.get_rect(center=(self.button_width // 2, self.button_height // 2)),
        )

        button_rect = pygame.Rect(
            _COL_KEY_X - self.button_width // 2,
            y,
            self.button_width,
            self.button_height,
        )
        btn_name = f"key_{note}"
        self.buttons[btn_name] = {
            "surface": button_surf,
            "rect": button_rect,
            "color": color,
            "label": label,
        }
        if btn_name not in self.button_names:
            self.button_names.append(btn_name)

    def on_open(self):
        """Refresh all key labels when the page is opened."""
        super().on_open()
        self.listening_for = None
        self.error_message = None
        for i, note in enumerate(_NOTE_KEYS):
            y = _TABLE_TOP + i * _ROW_HEIGHT
            self._make_key_button(note, y)

    # ------------------------------------------------------------------
    # Drawing
    # ------------------------------------------------------------------

    def draw(self, display_surface):
        display_surface.fill(config.MENU_BACKGROUND)

        # Title
        title_font = pygame.font.SysFont(config.GAME_FONT, 36)
        title_surf = title_font.render(self.title, True, (200, 200, 200))
        display_surface.blit(
            title_surf,
            title_surf.get_rect(
                center=(config.DISPLAY_WIDTH // 2, config.DISPLAY_HEIGHT // 8)
            ),
        )

        # Column headers
        header_font = pygame.font.SysFont(config.GAME_FONT, 22)
        note_header = header_font.render("Note", True, (180, 180, 180))
        key_header = header_font.render("Key", True, (180, 180, 180))
        display_surface.blit(
            note_header, note_header.get_rect(center=(_COL_NOTE_X, _TABLE_TOP - 28))
        )
        display_surface.blit(
            key_header, key_header.get_rect(center=(_COL_KEY_X, _TABLE_TOP - 28))
        )

        # Rows
        row_font = pygame.font.SysFont(config.GAME_FONT, 26)
        for i, (note, label) in enumerate(zip(_NOTE_KEYS, _NOTE_LABELS)):
            y_centre = _TABLE_TOP + i * _ROW_HEIGHT + self.button_height // 2

            # Alternating row tint
            row_rect = pygame.Rect(
                config.DISPLAY_WIDTH // 2 - 220,
                _TABLE_TOP + i * _ROW_HEIGHT - 4,
                440,
                _ROW_HEIGHT,
            )
            tint = pygame.Surface((row_rect.width, row_rect.height), pygame.SRCALPHA)
            tint.fill((255, 255, 255, 12) if i % 2 == 0 else (0, 0, 0, 0))
            display_surface.blit(tint, row_rect.topleft)

            # Note name label (left column)
            note_surf = row_font.render(label, True, (220, 220, 220))
            display_surface.blit(
                note_surf, note_surf.get_rect(center=(_COL_NOTE_X, y_centre))
            )

            # Key button (right column)
            btn_name = f"key_{note}"
            btn_data = self.buttons[btn_name]

            # Listening state — flash the button
            if self.listening_for == note:
                listen_surf = pygame.Surface(
                    (self.button_width + 4, self.button_height + 4), pygame.SRCALPHA
                )
                listen_surf.fill((255, 215, 0, 200))
                display_surface.blit(
                    listen_surf, (btn_data["rect"].x - 2, btn_data["rect"].y - 2)
                )
                # Overwrite label with prompt
                prompt_surf = row_font.render("???", True, (255, 215, 0))
                prompt_rect = prompt_surf.get_rect(center=btn_data["rect"].center)
                waiting_bg = pygame.Surface(
                    (btn_data["rect"].width, btn_data["rect"].height)
                )
                waiting_bg.fill((40, 40, 80))
                display_surface.blit(waiting_bg, btn_data["rect"].topleft)
                display_surface.blit(prompt_surf, prompt_rect)
            else:
                display_surface.blit(btn_data["surface"], btn_data["rect"].topleft)
                # Selection highlight
                if self.button_names.index(btn_name) == self.selected_index:
                    hl = pygame.Surface(
                        (btn_data["rect"].width, btn_data["rect"].height),
                        pygame.SRCALPHA,
                    )
                    hl.fill((0, 0, 0, 140))
                    display_surface.blit(hl, btn_data["rect"].topleft)

        # Back button
        back_data = self.buttons["back"]
        display_surface.blit(back_data["surface"], back_data["rect"].topleft)
        if self.button_names.index("back") == self.selected_index:
            hl = pygame.Surface(
                (back_data["rect"].width, back_data["rect"].height), pygame.SRCALPHA
            )
            hl.fill((0, 0, 0, 140))
            display_surface.blit(hl, back_data["rect"].topleft)

        # Instructions line
        instr_font = pygame.font.SysFont(config.GAME_FONT, 20)
        if self.listening_for:
            msg = f"Press a key to assign to  {_NOTE_LABELS[_NOTE_KEYS.index(self.listening_for)]}  (Esc to cancel)"
            color = (255, 215, 0)
        else:
            msg = "Click a key button to reassign it"
            color = (160, 160, 160)
        instr_surf = instr_font.render(msg, True, color)
        display_surface.blit(
            instr_surf,
            instr_surf.get_rect(
                center=(
                    config.DISPLAY_WIDTH // 2,
                    _TABLE_TOP + len(_NOTE_KEYS) * _ROW_HEIGHT + 6,
                )
            ),
        )

        # Error message
        if self.error_message and self.error_timer > 0:
            err_surf = instr_font.render(self.error_message, True, (255, 80, 80))
            display_surface.blit(
                err_surf,
                err_surf.get_rect(
                    center=(
                        config.DISPLAY_WIDTH // 2,
                        _TABLE_TOP + len(_NOTE_KEYS) * _ROW_HEIGHT + 30,
                    )
                ),
            )
            self.error_timer -= 1
            if self.error_timer <= 0:
                self.error_message = None

    # ------------------------------------------------------------------
    # Input
    # ------------------------------------------------------------------

    def handle_key_press(self, event):
        # --- Listening mode: capture the next key press ---
        if self.listening_for:
            if event.key == pygame.K_ESCAPE:
                # Cancel without changing anything
                self.listening_for = None
                return True

            error = config.remap_key(self.listening_for, event.key)
            if error:
                self.error_message = error
                self.error_timer = 180  # show for 3 seconds
            else:
                # Refresh the button label to show the new key
                i = _NOTE_KEYS.index(self.listening_for)
                y = _TABLE_TOP + i * _ROW_HEIGHT
                self._make_key_button(self.listening_for, y)
                self.game._rebuild_note_sounds()  # keep explore-mode sounds in sync
                self.error_message = None
            self.listening_for = None
            return True

        # --- Normal navigation ---
        if event.key == pygame.K_ESCAPE:
            return "back"
        return super().handle_key_press(event)

    def handle_click(self, event):
        # Clicking anywhere cancels listening mode without assigning
        if self.listening_for:
            self.listening_for = None
            return True

        for name, data in self.buttons.items():
            if data["rect"].collidepoint(event.pos):
                if name == "back":
                    return "back"
                elif name.startswith("key_"):
                    note = name[4:]  # "key_A" → "A"
                    self.listening_for = note
                    return True
        return True

    def handle_mouse_motion(self, event):
        # Only update hover/selection for the back button during normal mode
        if self.listening_for:
            return
        super().handle_mouse_motion(event)


# ---------------------------------------------------------------------------
# Pause Menu
# ---------------------------------------------------------------------------


class PauseMenu(Menu):
    def __init__(self, game):
        super().__init__(game, title="Pause Menu")
        self.button_width = 250

        self.create_button(
            "resume", "Resume", config.DISPLAY_HEIGHT // 4 - 60, color=(100, 150, 100)
        )
        self.create_button(
            "training",
            "Training",
            config.DISPLAY_HEIGHT // 4 + 20,
            color=(80, 80, 150),
        )
        self.create_button(
            "menu",
            "Return to Menu",
            config.DISPLAY_HEIGHT // 4 + 100,
            color=(150, 100, 100),
        )

        self.sub_pages = {"training": TrainingMenu(game)}
        self.active_sub_page = None

    def _open_sub_page(self, name):
        self.active_sub_page = self.sub_pages[name]
        self.active_sub_page.on_open()

    def _close_sub_page(self):
        self.active_sub_page = None

    def draw(self, display_surface):
        overlay = pygame.Surface(
            (config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT), pygame.SRCALPHA
        )
        overlay.fill((0, 0, 0, 128))
        display_surface.blit(overlay, (0, 0))

        if self.active_sub_page:
            self.active_sub_page.draw(display_surface)
            return

        title = self.game.game_font.render("PAUSED", True, (255, 255, 255))
        display_surface.blit(
            title, title.get_rect(center=(config.DISPLAY_WIDTH // 2, 50))
        )

        for i, button_name in enumerate(self.button_names):
            button_data = self.buttons[button_name]
            display_surface.blit(button_data["surface"], button_data["rect"].topleft)
            if i == self.selected_index:
                hl = pygame.Surface(
                    (self.button_width, self.button_height), pygame.SRCALPHA
                )
                hl.fill((255, 255, 255, 100))
                display_surface.blit(hl, button_data["rect"].topleft)

    def handle_click(self, event):
        if self.active_sub_page:
            result = self.active_sub_page.handle_click(event)
            if result == "back":
                self._close_sub_page()
            return True

        for name, data in self.buttons.items():
            if data["rect"].collidepoint(event.pos):
                if name == "resume":
                    self.game.set_state(GameState.PLAY)
                    return True
                elif name == "training":
                    self._open_sub_page("training")
                    return True
                elif name == "menu":
                    self.game.set_state(GameState.MENU)
                    return True
        return True

    def handle_key_press(self, event):
        if self.active_sub_page:
            result = self.active_sub_page.handle_key_press(event)
            if result == "back":
                self._close_sub_page()
            return True
        if event.key == pygame.K_ESCAPE:
            self.game.set_state(GameState.PLAY)
            return True
        return super().handle_key_press(event)

    def handle_mouse_motion(self, event):
        if self.active_sub_page:
            self.active_sub_page.handle_mouse_motion(event)
        else:
            super().handle_mouse_motion(event)


# ---------------------------------------------------------------------------
# Training sub-page (song selection, paginated)
# ---------------------------------------------------------------------------


class TrainingMenu(SubMenu):
    """
    Song selection sub-page, opened from the Pause Menu.
    Displays songs in fixed-size pages with Prev/Next navigation.

    Future hook: songs could carry an "unlocked" flag (e.g. SONGS[key]["unlocked"])
    and this menu could grey out / skip locked entries.
    """

    SONGS_PER_PAGE = 5

    def __init__(self, game):
        super().__init__(game, title="Training")
        self.button_width = 280
        self.song_keys = sorted(SONGS.keys())
        self.page = 0
        self._build_page_buttons()

    @property
    def total_pages(self):
        return max(1, (len(self.song_keys) - 1) // self.SONGS_PER_PAGE + 1)

    def on_open(self):
        super().on_open()
        self.page = 0
        self._build_page_buttons()

    def _build_page_buttons(self):
        """Rebuild song + navigation buttons for the current page."""
        self.buttons = {}
        self.button_names = []

        start = self.page * self.SONGS_PER_PAGE
        page_songs = self.song_keys[start : start + self.SONGS_PER_PAGE]

        y_offset = config.DISPLAY_HEIGHT // 4 - 40
        for i, song_key in enumerate(page_songs):
            display_name = f"Song: {song_key.replace('song', '').upper()}"
            color = (
                (100, 200, 100) if song_key == config.CURRENT_SONG else (80, 80, 150)
            )
            self.create_button(song_key, display_name, y_offset + i * 70, color=color)

        nav_y = y_offset + self.SONGS_PER_PAGE * 70 + 10
        if self.page > 0:
            self.create_button(
                "prev",
                "< Prev",
                nav_y,
                color=(90, 90, 90),
                x_center=config.DISPLAY_WIDTH // 3 - 160,
            )
        if self.page < self.total_pages - 1:
            self.create_button(
                "next",
                "Next >",
                nav_y,
                color=(90, 90, 90),
                x_center=2 * config.DISPLAY_WIDTH // 3 + 160,
            )

        self.create_button("back", "Back", nav_y + 80, color=(128, 128, 128))

    def draw(self, display_surface):
        # No fill/overlay here — PauseMenu already darkens the background.
        title_surf = self.game.game_font.render(self.title, True, (255, 255, 255))
        display_surface.blit(
            title_surf, title_surf.get_rect(center=(config.DISPLAY_WIDTH // 2, 50))
        )

        for i, button_name in enumerate(self.button_names):
            button_data = self.buttons[button_name]
            display_surface.blit(button_data["surface"], button_data["rect"].topleft)
            if i == self.selected_index:
                hl = pygame.Surface(
                    (button_data["rect"].width, button_data["rect"].height),
                    pygame.SRCALPHA,
                )
                hl.fill((255, 255, 255, 100))
                display_surface.blit(hl, button_data["rect"].topleft)

        # Page indicator
        nav_y = (config.DISPLAY_HEIGHT // 4 - 40) + self.SONGS_PER_PAGE * 70 + 10
        page_font = pygame.font.SysFont(config.GAME_FONT, 22)
        page_surf = page_font.render(
            f"Page {self.page + 1} / {self.total_pages}", True, (200, 200, 200)
        )
        display_surface.blit(
            page_surf,
            page_surf.get_rect(center=(config.DISPLAY_WIDTH // 2, nav_y + 20)),
        )

    def handle_click(self, event):
        for name, data in self.buttons.items():
            if data["rect"].collidepoint(event.pos):
                if name == "back":
                    return "back"
                elif name == "prev":
                    self.page -= 1
                    self._build_page_buttons()
                    self.selected_index = 0
                    return True
                elif name == "next":
                    self.page += 1
                    self._build_page_buttons()
                    self.selected_index = 0
                    return True
                elif name in SONGS:
                    config.CURRENT_SONG = name
                    self._build_page_buttons()  # refresh highlight color
                    return True
        return True

    def handle_key_press(self, event):
        if event.key == pygame.K_ESCAPE:
            return "back"
        elif event.key == pygame.K_LEFT and self.page > 0:
            self.page -= 1
            self._build_page_buttons()
            self.selected_index = 0
            return True
        elif event.key == pygame.K_RIGHT and self.page < self.total_pages - 1:
            self.page += 1
            self._build_page_buttons()
            self.selected_index = 0
            return True
        # UP/DOWN navigation and RETURN→handle_click are handled by the base class
        return super().handle_key_press(event)
