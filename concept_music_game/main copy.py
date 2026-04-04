import pygame
from pathlib import Path
from math import sqrt

ROOT_PATH = Path(__file__).parent

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
MENU_BACKGROUND = (0, 0, 0)

FRAME_REFRESH_RATE = 60
PLAYER_SPEED = 5


class Game:

    def __init__(self):
        print("Inicializing PyGame")
        pygame.init()
        self.display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption("Concept of Music Game")
        self.game_font = pygame.font.SysFont("Bauhaus 93", 30)

        # Sets a background image
        BACKGROUND = pygame.image.load(ROOT_PATH / "images/background1.png").convert()
        self.BACKGROUND = pygame.transform.scale(BACKGROUND, (1280, 720))

        self.clock = pygame.time.Clock()
        self.player = Player(self)

    def _pause(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False
                        break

    def menu(self):
        running = True
        draw_start_game = pygame.Surface((200, 60))
        draw_end_game = pygame.Surface((200, 60))
        draw_start_game.fill((0, 0, 255))

        draw_end_game.fill((255, 0, 0))
        start_game = pygame.Rect(DISPLAY_WIDTH // 10, DISPLAY_HEIGHT // 4, 200, 60)
        end_game = pygame.Rect(DISPLAY_WIDTH // 10, DISPLAY_HEIGHT // 3, 200, 60)
        while running:
            self.display_surface.fill(MENU_BACKGROUND)
            self.display_surface.blit(
                draw_start_game,
                (DISPLAY_WIDTH // 10, DISPLAY_HEIGHT // 4),
            )
            self.display_surface.blit(
                draw_end_game, (DISPLAY_WIDTH // 10, DISPLAY_HEIGHT // 3)
            )
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start_game.collidepoint(event.pos):
                        self.play()
                    elif end_game.collidepoint(event.pos):
                        running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                    running = False

    def play(self):
        running = True
        cycle_count = 0
        while running:

            # Player Movement block
            self.player.move()

            # Other key pressed events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    # Checks which key was pressed
                    if event.key == pygame.K_q:
                        running = False
                    elif event.key == pygame.K_p:
                        self._pause()

            # Get pressed key to change the character image
            keys = pygame.key.get_pressed()
            right = keys[pygame.K_RIGHT]
            left = keys[pygame.K_LEFT]
            up = keys[pygame.K_UP]
            down = keys[pygame.K_DOWN]
            # Changes sprite if appropriate
            if right:
                self.player.load_image(ROOT_PATH / "images/player/player_right.png")
            if left:
                self.player.load_image(ROOT_PATH / "images/player/player_left.png")
            if up:
                self.player.load_image(ROOT_PATH / "images/player/player_up.png")
            if down:
                self.player.load_image(ROOT_PATH / "images/player/player.png")
            self.display_surface.blit(
                self.BACKGROUND, (0, 0)
            )  # draw the background picture
            self.player.draw()
            pygame.display.update()
            self.clock.tick(FRAME_REFRESH_RATE)


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
        self.position = pygame.Vector2(DISPLAY_WIDTH / 10, DISPLAY_HEIGHT / 10)
        self.load_image(ROOT_PATH / "images/botao.png")


class Button(Staff):
    def __init__(self, game):
        self.game = game


class Battle_event: ...


# Criar 7 blocos fixos na tela

# Criar blocos que se movimentam de um determinado local em direção aos blocos fixos

# Checar se o jogador aperta o botão correto dentro da janela de colisão dos blocos
# class Staff(GameObject):
#     def __init__(self, game):
#         self.game = game
#         self.position = pygame.Vector2(DISPLAY_WIDTH / 10, DISPLAY_HEIGHT / 2)
#         self.load_image(ROOT_PATH / "images/staff.png")
#         self.buttons = []
#         # Create 7 fixed buttons
#         for i in range(7):
#             button = Button(self.game, i)
#             button.position = pygame.Vector2(self.position.x + i * 100, self.position.y)
#             self.buttons.append(button)

#     def draw(self):
#         super().draw()
#         for button in self.buttons:
#             button.draw()


# class Button(GameObject):
#     def __init__(self, game, index):
#         self.game = game
#         self.index = index
#         self.key = [pygame.K_a, pygame.K_s, pygame.K_d, pygame.K_f, pygame.K_g, pygame.K_h, pygame.K_j][index]
#         self.load_image(ROOT_PATH / f"images/button{index}.png")


# class MovingBlock(GameObject):
#     def __init__(self, game, target_button):
#         self.game = game
#         self.target = target_button
#         self.position = pygame.Vector2(DISPLAY_WIDTH - 100, DISPLAY_HEIGHT / 2)
#         self.speed = 2
#         self.load_image(ROOT_PATH / "images/moving_block.png")

#     def update(self):
#         direction = self.target.position - self.position
#         if direction.length() > 0:
#             direction.normalize_ip()
#             self.position += direction * self.speed

#     def is_colliding(self):
#         return self.rect().colliderect(self.target.rect())


# class Battle_event:
#     def __init__(self, game):
#         self.game = game
#         self.staff = Staff(game)
#         self.moving_blocks = []
#         self.spawn_timer = 0
#         self.score = 0

#     def update(self):
#         self.spawn_timer += 1
#         if self.spawn_timer > 120:  # Spawn every 2 seconds at 60 FPS
#             target = self.staff.buttons[pygame.time.get_ticks() % 7]
#             self.moving_blocks.append(MovingBlock(self.game, target))
#             self.spawn_timer = 0

#         for block in self.moving_blocks[:]:
#             block.update()
#             if block.position.x < 0:
#                 self.moving_blocks.remove(block)
#             elif block.is_colliding():
#                 keys = pygame.key.get_pressed()
#                 if keys[block.target.key]:
#                     self.score += 1
#                     self.moving_blocks.remove(block)

#     def draw(self):
#         self.staff.draw()
#         for block in self.moving_blocks:
#             block.draw()


def main():

    print("Iniciando o jogo")

    game = Game()
    game.menu()
    print("Fim de jogo")


if __name__ == "__main__":
    main()
