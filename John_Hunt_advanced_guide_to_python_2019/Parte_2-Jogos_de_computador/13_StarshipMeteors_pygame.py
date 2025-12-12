# Capítulo 13 - StarshipMeteors pygame
# Neste capítulo criaremos um jogo no qual você pilotará uma nave espacial através de
# um campo de meteoros. Quando mais tempo jogar, maior será o número de meteoros que
# encontrará. Vamos implementar várias classes para representar as entidades dentro do
# jogo. Usar classes não é mandatório para implementar um jogo e deveria ser notado
# que muitos desenvolvedores evitam o uso de classes. Entretanto, usar uma classe
# permite que dados associados com um objeto dentro do jogo sejam mantidos em um lugar;
# também simplifica a criação de múltiplas instâncias do mesmo objeto (como meteoros)
# dentro do jogo. As classes e sua relação são:

#               1|--Espaçonave------|
# Jogo -1--------|                  |--herdam----|--ObjetoJogo
#          varios|--Meteoros--------|

# O diagrama mostra que as classes Espaçonave e Meteoros estenderão uma classe chamada
# ObjetoJogo. Também mostra que o Jogo tem uma relação 1:1 com a classe Espaçonave.
# Isto é, o Jogo gurada a referência de uma Espaçonave, e, por sua vez, a espaçonave
# guarda uma única referência do Jogo. Em contraste, o Jogo tem uma relação 1:muitos com
# a classe Meteoros.
# --------------------------------------------
# A classe principal do jogo
# A primeira classe que criaremos é a classe Jogo. Ela guardará uma lista dos meteoros
# e da Espaçonave, assim como o loop de jogo principal. Também inicializará a exibição
# da janela principal(por exemplo, definindo o tamanho e o título da janela). Neste caso,
# vamos guardar a superfície de exibição retornada pela função pygame.display.set_mode()
# em um atributo do objeto Jogo chamado superficie_exibicao. Isto pois precisaremos
# usá-lo posteriormente para exibir a espaçonave e os meteoros.
# Também vamos guardar uma instância da classe pygame.time.Clock() que usaremos para
# definir a taxa de quadros cada vez que o jogo completar uma volta do loop while.
# A estrutura básica do jogo é mostrada abaixo; esta listagem fornece a classe Jogo básica
# e o método principal que lançará o jogo. O jogo também define três constantes globais
# que serão usadas para definir a taxa de atualização de quadros e o tamanho da tela.
import pygame, random
from pathlib import Path

ROOT_PATH = Path(__file__).parent
FRAME_REFRESH_RATE = 30
DISPLAY_WIDTH = 600
DISPLAY_HEIGHT = 400

ESPACONAVE_VELOCIDADE = 10
BACKGROUND = (0, 0, 0)

INITIAL_METEOR_Y_LOCATION = 10
MAX_METEOR_SPEED = 5
INITIAL_NUMBER_OF_METEORS = 8
NEW_METEOR_CYCLE_INTERVAL = 40

MAX_NUMBER_OF_CYCLES = 1000

GREEN = (0, 255, 0)
WHITE = (255, 255, 255)


class Game:
    """Representa o jogo em si e o loop do jogo"""

    def __init__(self):
        print("Inicializando PyGame")
        pygame.init()
        self.display_surface = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
        pygame.display.set_caption("Starship Meteors")
        self.relogio = pygame.time.Clock()
        self.espaconave = Espaconave(self)
        self.meteoros = [Meteoros(self) for _ in range(0, INITIAL_NUMBER_OF_METEORS)]
        self.estrelas = []
        self.pontos = 0

    def _checar_colisao(self):
        result = False
        for meteoro in self.meteoros:
            if self.espaconave.rect().colliderect(meteoro.rect()):
                result = True
                break
        for estrela in self.estrelas:
            if self.espaconave.rect().colliderect(estrela.rect()):
                result = True
                break

        return result

    def _pause(self):
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        paused = False
                        break

    def _display_message(self, message):
        print(message)
        text_font = pygame.font.Font("freesansbold.ttf", 48)
        text_surface = text_font.render(message, True, GREEN, WHITE)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
        self.display_surface.fill(WHITE)
        self.display_surface.blit(text_surface, text_rectangle)

    def pontuacao(self):
        score = self.pontos
        text_font = pygame.font.Font("freesansbold.ttf", 20)
        text_surface = text_font.render(str(score), True, GREEN, None)
        text_rectangle = text_surface.get_rect()
        text_rectangle.center = (60, 30)
        self.display_surface.blit(text_surface, text_rectangle)

    def play(self):
        esta_executando = True
        espaconave_colidiu = False
        cycle_count = 0
        while esta_executando and not espaconave_colidiu:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esta_executando = False
                elif event.type == pygame.KEYDOWN:
                    # Checa qual tecla foi pressionada
                    if event.key == pygame.K_RIGHT:
                        # Tecla direita foi pressionada; move para direita
                        self.espaconave.move_direita()
                    elif event.key == pygame.K_LEFT:
                        self.espaconave.move_esquerda()
                    elif event.key == pygame.K_UP:
                        self.espaconave.move_cima()
                    elif event.key == pygame.K_DOWN:
                        self.espaconave.move_baixo()
                    elif event.key == pygame.K_q:
                        esta_executando = False
                    elif event.key == pygame.K_p:
                        self._pause()
            self.display_surface.fill(BACKGROUND)
            self.espaconave.draw()
            for meteoro in self.meteoros:
                meteoro.draw()
            for meteoro in self.meteoros:
                meteoro.move_baixo()
            if not self.estrelas == None:
                for estrela in self.estrelas:
                    estrela.draw()
                for estrela in self.estrelas:
                    estrela.move_direita()

            if self._checar_colisao():
                espaconave_colidiu = True
                self._display_message("Colisão: Fom de jogo!")
            if cycle_count == MAX_NUMBER_OF_CYCLES:
                print("WINNER!")
                self._display_message("Vencedor!")
                break
            if cycle_count % NEW_METEOR_CYCLE_INTERVAL == 0:
                self.meteoros.append(Meteoros(self))
                self.pontos += 1
            if cycle_count % 80 == 0:
                self.estrelas.append(Estrela(self))
                self.pontos += 10
            cycle_count += 1
            self.pontuacao()
            pygame.display.update()
            self.relogio.tick(FRAME_REFRESH_RATE)
        pygame.quit()


# -------------------------------
# A classe ObjetoJogo
# A classe ObjetoJogo define três métodos:
# O método load_image() pode ser usado para carregar uma imagem a ser usada para representar
# visualmente o tipo específico do objeto do jogo. O método usa, então, a largura e altura
# da imagem para definir a largura e altura do objeto do jogo.
# O método rect() retorna um retângulo representando a área atual usada pelo objeto
# jogo na superfície de desenho subjacente. Ele difere de rect() da própria imagem
# que não é relacionada ao local do objeto do jogo na superfície. Rects são bastante
# úteis para comparar o local de um objeto com outro (por exemplo, ao determinar se
# uma colisão ocorreu).
# O método draw() desenha a imagem do ObjetoJogo na display_surface guardada pelo jogo
# usando as coordenadas x e y atuais do ObjetoJogo. Pode ser sobrescrito por subclasses
# se quiser desenhá-las de outro modo.
class ObjetoJogo:
    def load_image(self, filename):
        self.image = pygame.image.load(filename).convert()
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.game.display_surface.blit(self.image, (self.x, self.y))


# A classe ObjetoJogo é diretamente estendida pelas classes Espaçonave e Meteoros.
# ------------------------------------------------------------
# Exibindo a Espaçonave
# O jogador humano deste jogo controlará uma espaçonave que pode ser movida pela tela.
# A espaçonave será representada por uma instância da classe Espaconave. Esta classe
# estenderá a classe ObjetoJogo que armazena comportamentos em comum apra qualquer tipo
# de elemento que é representado dentro daquele jogo.
# A classe Espaconave define seu proprio __init__() que pega uma referência ao jogo
# do qual a espaçonave faz parte. Este método de inicialização define a posição inicial
# da Espaconave como metade da tela de exibição para a coordenada x e a altura de exibição
# menos 40 para a coordenada y. Então usa o método carregar imagem da classe pai ObjetoJogo
# para carregar a imagem a ser usada para representar a Espaconave. Ela é armazenada em
# um arquivo chamado starship.png.
class Espaconave(ObjetoJogo):

    def __init__(self, game):
        self.game = game
        self.x = DISPLAY_WIDTH / 2
        self.y = DISPLAY_HEIGHT - 40
        self.load_image(ROOT_PATH / "starship.png")

    def move_direita(self):
        """Move a espaçonave para a direita na tela"""
        self.x = self.x + ESPACONAVE_VELOCIDADE
        if self.x + self.width > DISPLAY_WIDTH:
            self.x = DISPLAY_WIDTH - self.width

    def move_esquerda(self):
        """Move a espaçonave para a esquerda na tela"""
        self.x = self.x - ESPACONAVE_VELOCIDADE
        if self.x + self.width < 0:
            self.x = 0

    def move_cima(self):
        """Move a espaçonave para cima na tela"""
        self.y = self.y - ESPACONAVE_VELOCIDADE
        if self.y + self.width < 0:
            self.y = 0

    def move_baixo(self):
        """Move a espaçonave para a baixo na tela"""
        self.y = self.y + ESPACONAVE_VELOCIDADE
        if self.y + self.width > DISPLAY_HEIGHT:
            self.y = DISPLAY_HEIGHT - self.width

    def __str__(self):
        return "Espaconave(" + str(self.x) + ", " + str(self.y) + ")"


# Na classe Jogo agora adicionaremos uma linha no método __init__() para inicializar
# o objeto Espaconave. Esta linha é:
# self.espaconave = Espaconave(self)
# Também adicionamos uma linha ao loop principal dentro do método play() logo antes
# de atualizar a exibição. Esta linha chamará o método draw() no objeto espaconave.
# self.espaconave.draw()
# Isto terá o efeito de desenhar a nave nas superfície de desenho da janela no fundo,
# antes da tela ser atualizada.

# --------------------------------------------
# Movendo a espaçonave
# Para mover a espaçonave, mudamos as coordenadas x e y em resposta ao usuário apertando
# diversas teclas. Vamos usar as teclas de direção para mover para cima, baixo, esquerda ou direita.
# Para fazer isso, vamos definir 4 métodos dentro da classe Espaconave; estes métodos
# moverão a Espaconave.
# -----------------------------
# Adicionando a classe Meteoros
# A classe Meteoro também será uma subclasse da classe ObjetoJogo. Entretanto, apenas
# terá um método move_baixo() em vez dos diversos da Espaconave. Também precisará
# ter uma coordenada aleatória inicial x, de modo que quando um meteoro é acrescentado
# ao jogo, sua posição inicial variará. Esta posição aleatória será gerada usando a
# função random.randint() usando um valor entre 0 e a largura da superfície. O meteoro
# também iniciará no topo da tela. Por fim, também queremos que os meteoros tenham velocidades
# diferentes; isto pode ser outro número aleatório entre 1 e algum valor máximo especificado.


class Meteoros(ObjetoJogo):

    def __init__(self, game):
        self.game = game
        self.x = random.randint(0, DISPLAY_WIDTH)
        self.y = INITIAL_METEOR_Y_LOCATION
        self.speed = random.randint(1, MAX_METEOR_SPEED)
        self.load_image(ROOT_PATH / "meteor.png")

    def move_baixo(self):
        self.y = self.y + self.speed
        if self.y > DISPLAY_HEIGHT:
            self.y = 5

    def __str__(self):
        return "Meteor(" + str(self.x) + ", " + str(self.x) + ")"


# O método __init__() para a classe Meteoro tam os mesmos passos da Espaconave;
# a diferença é que a coordenada x e a velocidade são geradas aleatoriamente.
# A imagem usada para o Meteoro também é diferente, 'meteor.png'.

# ----------------------------------------------
# Identificando uma colisão
# Podemos acrescentar uma detecção de colisão usando PyGame Rects.


class Estrela(ObjetoJogo):

    def __init__(self, game):
        self.game = game
        self.x = 10
        self.y = random.randint(50, DISPLAY_WIDTH)
        self.speed = random.randint(3, MAX_METEOR_SPEED)
        self.load_image(ROOT_PATH / "star.png")

    def move_direita(self):
        """Move a espaçonave para a direita na tela"""
        self.x = self.x + self.speed
        if self.x > DISPLAY_WIDTH:
            self.x = 10

    def __str__(self):
        return "Star(" + str(self.x) + ", " + str(self.x) + ")"


def main():

    print("Iniciando o jogo")

    game = Game()
    game.play()
    print("Fim de jogo")


if __name__ == "__main__":
    main()
