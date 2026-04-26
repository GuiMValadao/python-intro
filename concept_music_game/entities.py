import config
import pygame

from math import sqrt


class GameObject:
    def load_image(self, filename):
        self.image = pygame.image.load(filename).convert()
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
        self.position = pygame.Vector2(
            config.DISPLAY_WIDTH // 2, config.DISPLAY_HEIGHT // 2
        )
        self.load_image(config.ROOT_PATH / "images/player/player.png")
        self.PLAYER_SPEED = config.PLAYER_SPEED

    def move(self):
        keys = pygame.key.get_pressed()
        right = keys[pygame.K_RIGHT]
        left = keys[pygame.K_LEFT]
        up = keys[pygame.K_UP]
        down = keys[pygame.K_DOWN]

        is_diagonal = (right or left) and (up or down)
        self.PLAYER_SPEED = (
            config.PLAYER_SPEED / sqrt(2) if is_diagonal else config.PLAYER_SPEED
        )

        if right:
            self.position.x += self.PLAYER_SPEED
        if left:
            self.position.x -= self.PLAYER_SPEED
        if up:
            self.position.y = self.position.y - self.PLAYER_SPEED
        if down:
            self.position.y = self.position.y + self.PLAYER_SPEED

        # Clamp to map bounds instead of screen bounds
        map_w = self.game.current_map.width
        map_h = self.game.current_map.height
        self.position.x = max(0, min(self.position.x, map_w - self.width))
        self.position.y = max(0, min(self.position.y, map_h - self.height))


class Staff(GameObject):
    def __init__(self, game):
        self.game = game
        self.position = pygame.Vector2(50, config.DISPLAY_HEIGHT / 2)
        self.load_image(config.ROOT_PATH / "images/staff.png")
        self.buttons = []
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
            config.NOTES_TO_KEYS["A"],
            config.NOTES_TO_KEYS["B"],
            config.NOTES_TO_KEYS["C"],
            config.NOTES_TO_KEYS["D"],
            config.NOTES_TO_KEYS["E"],
            config.NOTES_TO_KEYS["F"],
            config.NOTES_TO_KEYS["G"],
        ][index]
        self.load_image(config.ROOT_PATH / f"images/buttons/button{index+1}.png")


class MovingBlock(GameObject):
    def __init__(self, game, target_button, note_key=None):
        self.game = game
        self.target = target_button
        self.note_key = note_key

        self.modifier = 0
        if isinstance(note_key, tuple):
            _, self.modifier = note_key

        base_speed = 3
        if config.DIFFICULTY == "Easy":
            self.speed = base_speed * 0.7
        elif config.DIFFICULTY == "Hard":
            self.speed = base_speed
        else:
            self.speed = base_speed

        self.load_image(config.ROOT_PATH / "images/moving_block.png")
        self.position = pygame.Vector2(
            config.DISPLAY_WIDTH - self.width, self.target.position.y
        )
        direction = self.target.position - self.position
        if direction.length() > 0:
            self.direction = direction.normalize()
        else:
            self.direction = pygame.Vector2(-1, 0)

        colors = [
            (255, 255, 0),
            (0, 0, 255),
            (0, 255, 255),
            (255, 0, 0),
            (0, 255, 0),
            (255, 125, 0),
            (255, 255, 255),
        ]
        color = colors[self.target.index]
        self.image = self.image.copy()
        self.image.fill(color, special_flags=pygame.BLEND_MULT)
        self._apply_modifier_overlay()

    def update(self):
        self.position += self.direction * self.speed

    def _apply_modifier_overlay(self):
        """Apply a color overlay and symbol based on the note modifier."""
        from events import get_modifier_color_overlay

        result = get_modifier_color_overlay(self.modifier)
        if result is None:
            return

        overlay_color, symbol_text = result
        if overlay_color:
            self.image.fill(overlay_color, special_flags=pygame.BLEND_ADD)

        font = pygame.font.SysFont(config.GAME_FONT, 32)
        symbol_surface = font.render(symbol_text, True, (0, 0, 0))
        symbol_rect = symbol_surface.get_rect(
            center=(self.image.get_width() // 2, self.image.get_height() // 2)
        )
        self.image.blit(symbol_surface, symbol_rect)

    def is_colliding(self):
        return self.rect().colliderect(self.target.rect())


class KeyChangeMarker(GameObject):
    """
    A purely visual object that travels from the right edge of the screen toward
    the staff, arriving exactly when the key signature changes.  It serves as an
    advance warning for Easy and Medium players.

    It does not interact with input or scoring — it is removed once it reaches
    x < 0 just like a MovingBlock.
    """

    # Height of the marker bar — spans the full staff vertically
    BAR_HEIGHT = 7 * 30 + 32  # 7 buttons × 30 px spacing + one button height

    def __init__(self, game, incoming_key):
        self.game = game
        self.incoming_key = incoming_key

        # Match speed to MovingBlock for the current difficulty
        base_speed = 3
        if config.DIFFICULTY == "Easy":
            self.speed = base_speed * 0.7
        else:
            self.speed = base_speed  # Medium (Hard never spawns markers)

        # Build the marker surface: a vertical bar with the key name
        bar_width = 6
        self.width = bar_width + 80  # extra width for the label
        self.height = self.BAR_HEIGHT

        self.image = pygame.Surface((self.width, self.height), pygame.SRCALPHA)
        self._build_image()

        # Start just off the right edge, vertically aligned with the staff
        staff_top_y = config.DISPLAY_HEIGHT / 2  # matches Staff.__init__
        self.position = pygame.Vector2(config.DISPLAY_WIDTH, staff_top_y)

        self.direction = pygame.Vector2(-1, 0)

    def _build_image(self):
        """Render the marker bar and key name label onto self.image."""
        self.image.fill((0, 0, 0, 0))  # transparent

        display_name = config.KEY_SIGNATURE_DISPLAY.get(
            self.incoming_key, self.incoming_key
        )

        # Colour: gold for sharp keys, steel-blue for flat keys, white for C/A minor
        key_sig = config.KEY_SIGNATURES.get(self.incoming_key, {})
        if any(v.endswith("#") for v in key_sig.values()):
            bar_color = (255, 200, 50, 220)  # gold — sharp key
            text_color = (255, 230, 100)
        elif any(v.endswith("b") for v in key_sig.values()):
            bar_color = (100, 180, 255, 220)  # steel-blue — flat key
            text_color = (150, 210, 255)
        else:
            bar_color = (220, 220, 220, 200)  # light grey — C major / natural
            text_color = (255, 255, 255)

        # Draw vertical bar
        pygame.draw.rect(self.image, bar_color, (0, 0, 6, self.height))

        # Draw rotated key label alongside the bar
        font = pygame.font.SysFont(config.GAME_FONT, 18)
        label = font.render(display_name, True, text_color)

        # Rotate 90° so text reads upward along the bar
        rotated = pygame.transform.rotate(label, 90)
        label_x = 10
        label_y = max(0, (self.height - rotated.get_height()) // 2)
        self.image.blit(rotated, (label_x, label_y))

    def update(self):
        self.position += self.direction * self.speed

    def draw(self):
        self.game.display_surface.blit(self.image, (self.position.x, self.position.y))

    def rect(self):
        return pygame.Rect(self.position.x, self.position.y, self.width, self.height)


class NPCGeneric(GameObject):
    def __init__(
        self,
        game,
        name,
        sprite_path,
        dialogues,
        song_key,
        health=100,
        battle_intro=None,
        battle_outro=None,
    ):
        self.game = game
        self.name = name
        self.dialogues = dialogues
        self.song_key = song_key
        self.health = health
        self.battle_intro = battle_intro
        self.battle_outro = battle_outro
        self.load_image(sprite_path)
        self.position = pygame.Vector2(0, 0)

    def interact(self):
        """Trigger dialogue then battle."""
        # TODO - Perhaps keep this method abstract to each type of NPC implement their own interaction;
        # Some might have few lines of dialogue before battle, other might offer a option to battle
        # and others might require quest completion or, perhaps some kind of reputation or fame before facing off
        # config.CURRENT_SONG = self.song_key
        # self.game.battle_event = BattleEvent(self.game, npc=self)

    def on_battle_update(self, battle_event):
        """
        Called every frame during battle. Default behaviour: do nothing.
        Subclasses override this to add interference.
        """
        pass

    # TODO - revise these to implement behavior during battle.
    #   For example, instead of on_player_hit, eb certain scores threshold

    def on_player_miss(self, battle_event):
        """Called when the player misses a note. Default: no reaction."""
        pass

    def on_player_hit(self, battle_event):
        """Called when the player hits a note. Default: no reaction."""
        pass
