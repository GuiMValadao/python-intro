import pygame
from pathlib import Path
from math import sqrt

ROOT_PATH = Path(__file__).parent

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
BACKGROUND = (0, 0, 124)
FRAME_REFRESH_RATE = 60


class Game:

    def __init__(self):
        print("Inicializing PyGame")
        pygame.init()
        self.display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption("Concept of Music Game")
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

            self.display_surface.fill(BACKGROUND)
            self.player.draw()
            pygame.display.update()
            self.clock.tick(FRAME_REFRESH_RATE)


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
        self.position = pygame.Vector2(DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2)
        self.load_image(ROOT_PATH / "images/player/player2.png")
        self.PLAYER_SPEED = 5

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
        keys = pygame.key.get_pressed()
        right = keys[pygame.K_RIGHT]
        left = keys[pygame.K_LEFT]
        up = keys[pygame.K_UP]
        down = keys[pygame.K_DOWN]

        # Calculate if moving diagonally
        is_diagonal = (right or left) and (up or down)
        self.PLAYER_SPEED = 5 / sqrt(2) if is_diagonal else 5

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


# Criar blocos fixos na tela (pode ser 5 pra começar)

# Criar blocos que se movimentam de um determinado local em direção aos blocos fixos

# Checar se o jogador aperta o botão correto dentro da janela de colisão dos blocos


def main():

    print("Iniciando o jogo")

    game = Game()
    game.play()
    print("Fim de jogo")


if __name__ == "__main__":
    main()
