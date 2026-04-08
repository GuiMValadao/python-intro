import config
import pygame
from math import sqrt


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
        self.position = pygame.Vector2(
            config.DISPLAY_WIDTH // 2, config.DISPLAY_HEIGHT // 2
        )
        self.load_image(config.ROOT_PATH / "images/player/player.png")
        self.PLAYER_SPEED = config.PLAYER_SPEED

    def move_right(self, right):
        if right:
            self.position.x += self.PLAYER_SPEED
        if self.position.x + self.width > config.DISPLAY_WIDTH:
            self.position.x = config.DISPLAY_WIDTH - self.width

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
        if self.position.y + self.height > config.DISPLAY_HEIGHT:
            self.position.y = config.DISPLAY_HEIGHT - self.height

    def move(self):
        keys = pygame.key.get_pressed()
        right = keys[pygame.K_RIGHT]
        left = keys[pygame.K_LEFT]
        up = keys[pygame.K_UP]
        down = keys[pygame.K_DOWN]

        # Calculate if moving diagonally
        is_diagonal = (right or left) and (up or down)
        self.PLAYER_SPEED = (
            config.PLAYER_SPEED / sqrt(2) if is_diagonal else config.PLAYER_SPEED
        )

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
        self.position = pygame.Vector2(50, config.DISPLAY_HEIGHT / 2)
        self.load_image(config.ROOT_PATH / "images/staff.png")
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
        self.load_image(config.ROOT_PATH / f"images/buttons/button{index+1}.png")


class MovingBlock(GameObject):
    def __init__(self, game, target_button):
        self.game = game
        self.target = target_button
        # Adjust speed based on config.DIFFICULTY
        base_speed = 3
        if config.DIFFICULTY == "Easy":
            self.speed = base_speed * 0.7  # Slower for Easy
        elif config.DIFFICULTY == "Medium":
            self.speed = base_speed
        elif config.DIFFICULTY == "Hard":
            self.speed = base_speed  # Normal speed, but intervals are shorter
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


class NPCGeneric(GameObject): ...
