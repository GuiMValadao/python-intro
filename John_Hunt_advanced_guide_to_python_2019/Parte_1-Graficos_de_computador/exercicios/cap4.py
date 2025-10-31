# Exercício Capítulo 4
# O objetivo deste exercício é criar uma Árvore Fractal.
# Uma Árvore Fractal é uma árvore em que a estrutura geral é replicada
# em níveis cada vez mais finos pela árvore até um conjunto de elementos
# folha são alcançados.
# Para desenhar a árvore fractal é necessário:
#   - Desenhar o tronco
#   - No fim do tronco, dividir o tronco em dois com o tronco esquerdo e o
#       tronco direito estando 30 ° à esquerda/direita do tronco original.
#       Por questões estéticas, o tronco pode ser tornar mais fino cada vez
#       que é dividido. O tronco pode ser desenhado com uma cor particular
#       como marrom.
#   - Continue isto até um número máximo de divisões ocorreu (ou o tamannho
#       do tronco se reduz a um mínimo particular). Agora você alcançou as
#       folhas (pode desenhar as folhas com uma cor diferente, como verde).

import turtle


def preparacao():
    """Configurações da tela"""
    turtle.title("Octógonos e hexágonos")
    turtle.setup(500, 500, 0, 0)
    turtle.setworldcoordinates(-250, 0, 500, 500)
    # turtle.hideturtle()


def arvore_fractal(altura, angulo, profundidade):
    if profundidade == 4:
        turtle.pencolor("green")
        # turtle.dot(15, "red")
        turtle.penup()
    elif profundidade > 4:
        turtle.pencolor("brown")
    else:
        return
    turtle.pendown()
    turtle.pensize(profundidade // 2)
    turtle.forward(altura)
    turtle.right(angulo)
    arvore_fractal(altura * 0.7, angulo, profundidade - 1)

    turtle.left(2 * angulo)
    arvore_fractal(altura * 0.7, angulo, profundidade - 1)

    turtle.right(angulo)
    turtle.penup()
    turtle.backward(altura)


preparacao()
turtle.speed(0)
turtle.penup()
turtle.left(90)
turtle.pendown()
arvore_fractal(100, 30, 12)
turtle.update()
print("Pronto!")
turtle.exitonclick()
