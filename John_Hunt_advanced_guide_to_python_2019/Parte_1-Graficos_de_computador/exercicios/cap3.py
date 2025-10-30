# Exercício Capítulo 3
# O objetivo deste exercício é criar uma imagem gráfica usando Turtle Graphics.
# Crie um programa simples para desenhar octógonos na tela do Turtle Graphics.
# Modifique o programa para que exista uma função para desenhar hexágonos.
# Esta função deve pegar 3 parâmetros, as coordenadas x e y e o tamanho
# de cada lado do octógono.
# Modifique o programa para desenhar o hexágono em múltiplos locais para
# criar uma figura com 7 hexágonos em um círculo fechado.

import turtle
import math


def preparacao():
    """Configurações da tela"""
    turtle.title("Octógonos e hexágonos")
    turtle.setup(500, 500, 0, 0)
    # turtle.hideturtle()


def formas_geometricas(x, y, lado, entrada):
    # entrada = input(
    #     """Qual forma quer desenhar?
    #                 Digite 'o' para octógono e 'h' para hexágono:\n=> """
    # )
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    if entrada == "o":
        preparacao()
        octogono(lado)
    elif entrada == "h":
        preparacao()
        hexagono(lado)


def octogono(lado):
    for i in range(8):
        turtle.forward(lado)
        turtle.left(45)


def hexagono(lado):
    for i in range(6):
        turtle.forward(lado)
        turtle.left(60)


diagonal_hexagono = 100 * math.sin(math.pi * 2 / 6)
altura_peq = 50 * math.cos(math.pi * 2 / 6)
formas_geometricas(0, 0, 50, "h")
formas_geometricas(0, diagonal_hexagono, 50, "h")
formas_geometricas(50 + altura_peq, diagonal_hexagono + diagonal_hexagono / 2, 50, "h")
formas_geometricas(2 * (50 + altura_peq), diagonal_hexagono, 50, "h")
formas_geometricas(2 * (50 + altura_peq), 0, 50, "h")
formas_geometricas(50 + altura_peq, -diagonal_hexagono + diagonal_hexagono / 2, 50, "h")
turtle.exitonclick()
