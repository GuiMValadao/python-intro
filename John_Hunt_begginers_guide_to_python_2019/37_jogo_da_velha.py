# Capítulo 31 - Jogo da Velha
# A classe símbolo abaixo; é uma classe orientada a dados, referida às vezes
# como tipo valor(value). Isto é pois ela armazena valores, mas não inclui métodos.
from abc import ABCMeta, abstractmethod
import random


class Simbolo:
    """Representa o símbolo a ser usado no tabuleiro."""

    def __init__(self, string):
        self.etiqueta = string

    def __str__(self):
        return self.etiqueta


# Define Símbolos globais:
X = Simbolo("X")
O = Simbolo("O")


class Jogada:
    """Representa uma jogada feita por um jogador"""

    def __init__(self, simbolo, x, y):
        self.x = x
        self.y = y
        self.simbolo = simbolo


class Tabuleiro:
    """Tabuleiro do jogo da velha"""

    def __init__(self):
        self.posicoes = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        self.separador = "\n" + ("-" * 11) + "\n"

    def __str__(self):
        linha1 = (
            " "
            + str(self.posicoes[0][0])
            + " | "
            + str(self.posicoes[0][1])
            + " | "
            + str(self.posicoes[0][2])
        )
        linha2 = (
            " "
            + str(self.posicoes[1][0])
            + " | "
            + str(self.posicoes[1][1])
            + " | "
            + str(self.posicoes[1][2])
        )
        linha3 = (
            " "
            + str(self.posicoes[2][0])
            + " | "
            + str(self.posicoes[2][1])
            + " | "
            + str(self.posicoes[2][2])
        )
        return linha1 + self.separador + linha2 + self.separador + linha3

    def nova_jogada(self, jogada):
        linha = self.posicoes[jogada.x]
        linha[jogada.y] = jogada.simbolo

    def e_posicao_vazia(self, linha, coluna):
        return self.posicoes[linha][coluna] == " "

    def posicao_contem(self, simbolo, linha, coluna):
        return self.posicoes[linha][coluna] == simbolo

    def e_cheio(self):
        for linha in range(0, 3):
            for coluna in range(0, 3):
                if self.e_posicao_vazia(linha, coluna):
                    return False
        return True

    def checa_vencedor(self, jogador):
        c = jogador.simbolo
        return (
            (
                self.posicao_contem(c, 0, 0)
                and self.posicao_contem(c, 0, 1)
                and self.posicao_contem(c, 0, 2)
            )
            or (
                self.posicao_contem(c, 1, 0)
                and self.posicao_contem(c, 1, 1)
                and self.posicao_contem(c, 1, 2)
            )
            or (
                self.posicao_contem(c, 2, 0)
                and self.posicao_contem(c, 2, 1)
                and self.posicao_contem(c, 2, 2)
            )
            or (
                self.posicao_contem(c, 0, 0)
                and self.posicao_contem(c, 1, 0)
                and self.posicao_contem(c, 2, 0)
            )
            or (
                self.posicao_contem(c, 0, 1)
                and self.posicao_contem(c, 1, 1)
                and self.posicao_contem(c, 2, 1)
            )
            or (
                self.posicao_contem(c, 0, 2)
                and self.posicao_contem(c, 1, 2)
                and self.posicao_contem(c, 2, 2)
            )
            or (
                self.posicao_contem(c, 0, 0)
                and self.posicao_contem(c, 1, 1)
                and self.posicao_contem(c, 2, 2)
            )
            or (
                self.posicao_contem(c, 0, 2)
                and self.posicao_contem(c, 1, 1)
                and self.posicao_contem(c, 2, 0)
            )
        )


class Jogador(metaclass=ABCMeta):
    """Classe abstrata representando um Jogador e seu simbolo"""

    def __init__(self, quadro):
        self.quadro = quadro
        self._simbolo = None

    @property
    def simbolo(self):
        """Representa Símbolo do Jogador - X or O"""
        return self._simbolo

    @simbolo.setter
    def simbolo(self, valor):
        self._simbolo = valor

    @abstractmethod
    def pegar_jogada(self):
        pass

    def __str__(self):
        return self.__class__.__name__ + "[" + str(self.simbolo) + "]"


class JogadorHumano(Jogador):
    """Representa um Jogador Humano e seu comportamento"""

    def __init__(self, quadro):
        super().__init__(quadro)

    def _pegar_entrada_usuario(self, prompt):
        entrada_invalida = True
        while entrada_invalida:
            print(prompt, end="")
            entrada_usuario = input()
            if not entrada_usuario.isdigit():
                print("Entrada tem que ser um número")
            else:
                entrada_usuario_int = int(entrada_usuario)
                if entrada_usuario_int < 1 or entrada_usuario_int > 3:
                    print("Escolha deve ser um número de 1 a 3")
                else:
                    entrada_invalida = False
        return entrada_usuario_int - 1

    def pegar_jogada(self):
        """Permite o jogador humano a escolher sua jogada"""
        while True:
            linha = self._pegar_entrada_usuario("Escolha a linha: ")
            coluna = self._pegar_entrada_usuario("Escolha a coluna: ")
            if self.quadro.e_posicao_vazia(linha, coluna):
                return Jogada(self.simbolo, linha, coluna)
            else:
                print("A posição escolhida já está ocupada")
                print("Escolha outra")


class JogadorComputador(Jogador):

    def __init__(self, quadro):
        super().__init__(quadro)

    def posicao_escolhida_aleatoriamente(self):
        """Usa um algoritmo de seleção aleatória simples para
        encontrar uma posição para preencher
        """
        while True:
            linha = random.randint(0, 2)
            coluna = random.randint(0, 2)
            if self.quadro.e_posicao_vazia(linha, coluna):
                return Jogada(self.simbolo, linha, coluna)

    def pegar_jogada(self):
        if self.quadro.e_posicao_vazia(1, 1):
            return Jogada(self.simbolo, 1, 1)
        elif self.quadro.e_posicao_vazia(0, 0):
            return Jogada(self.simbolo, 0, 0)
        elif self.quadro.e_posicao_vazia(2, 2):
            return Jogada(self.simbolo, 2, 2)
        elif self.quadro.e_posicao_vazia(0, 2):
            return Jogada(self.simbolo, 0, 2)
        elif self.quadro.e_posicao_vazia(2, 0):
            return Jogada(self.simbolo, 2, 0)
        else:
            return self.posicao_escolhida_aleatoriamente()


class Game:

    def __init__(self):
        self.quadro = Tabuleiro()
        self.humano = JogadorHumano(self.quadro)
        self.computador = JogadorComputador(self.quadro)
        self.proximo_jogador = None
        self.vencedor = None

    def selecionar_simbolo_jogador(self):
        simbolo = ""
        while not (simbolo == "X" or simbolo == "O"):
            print("Você quer escolher X ou O?")
            simbolo = input().upper()
            if simbolo != "X" and simbolo != "O":
                print("Escolha deve ser X ou O")
        if simbolo == "X":
            self.humano.simbolo = X
            self.computador.simbolo = O
        else:
            self.humano.simbolo = O
            self.computador.simbolo = X

    def escolhe_jogador_para_comecar(self):
        if random.randint(0, 1) == 0:
            self.proximo_jogador = self.humano
        else:
            self.proximo_jogador = self.computador

    def jogar(self):
        print("Bem vindo ao Jogo da Velha!")
        self.selecionar_simbolo_jogador()
        self.escolhe_jogador_para_comecar()
        print(self.proximo_jogador, "vai jogar primeiro.")
        while self.vencedor is None:
            if self.proximo_jogador == self.humano:
                print(self.quadro)
                print("Sua vez")
                jogada = self.humano.pegar_jogada()
                self.quadro.nova_jogada(jogada)
                if self.quadro.checa_vencedor(self.humano):
                    self.vencedor = self.humano
                else:
                    self.proximo_jogador = self.computador
            else:
                print("Jogada do computador")
                jogada = self.computador.pegar_jogada()
                self.quadro.nova_jogada(jogada)
                # print(self.quadro)
                if self.quadro.checa_vencedor(self.computador):
                    self.vencedor = self.computador
                else:
                    self.proximo_jogador = self.humano
            if self.vencedor is not None:
                print("O vencedor é " + str(self.vencedor))
            elif self.quadro.e_cheio():
                print("O jogo deu velha!")
                break
        print(self.quadro)


def main():
    game = Game()
    game.jogar()


if __name__ == "__main__":
    main()
