# Capítulo 3 - Python Turtle Graphics
# Python tem bastante suporte em termos de bibliotecas gráficas. Uma das
# mais usadas é a biblioteca Turtle Graphics introduzida neste capítulo.
# Isto se deve, parcialmente, pois é simples de usar e parcialmente
# pois é fornecida junto com o ambiente Python padrão(ou seja, não
# requer instalação).
# ----------------------------------------------
# O módulo Turtle
# Este módulo fornece uma biblioteca com recursos que permitem a criação
# do que são conhecidos como vetores gráficos. Vetores gráficos são
# linhas que podem ser desenhadas na tela. A área de desenho é comumente
# chamada plano de desenho ou quadro de desenho e tem a ideia de coordenadas
# x, y.
# A biblioteca Turtle Graphics é planejada como apenas uma ferramenta
# de desenho básica; outras bibliotecas podem ser usadas para desenhar
# gráficos de duas e três dimensões (Como MatPlotLib), mas elas
# costumam focar em tipos específicos de telas(displays) gráficas.
# A ideia por trás do módulo Turtle surge da linguagem de programação
# Logo dos anos 60 e 70 que foi desenvolvida para introduzir programação
# para crianças. Ela tinha uma tartaruga na tela que podia ser controlada
# por comandos como 'para frente', 'para direita', 'para esquerda' etc.
# Esta ideia foi mantida na biblioteca Turtle Graphis do Python onde
# comandos como turtle.forward(10) move a tartaruga(agora trocada por um cursor)
# 10 pixels para a frente.
# ------------------------------------------------
# Gráficos básicos de Turtle
# Apesar de fazer parte de Python 3, a biblioteca Turtle precisa ser
# importada antes de usada:
# import turtle

# Existem dois modos de trabalhar com o módulo turtle; um é usar as
# classes disponíveis com a biblioteca e o outro é usar um conjunto
# mais simples de funções que escondem as classes e objetos. Neste capítulo
# vamos focar no conjunto de funções que podem ser usadas para desenhar
# coisas com a bilbioteca Turtle Graphics.
# A primeira coisa que faremos é preparar a janela que vamos usar para os
# desenhos; a classe TurtleScreen é pai de todas as implementações de tela
# usadas para o sistema operacional que você está usando.
# Se estiver usando as funções fornecidas pelo módulo turtle, então o objeto
# tela é inicializado conforme for apropriado para o seu sistema operacional.
# Isto significa que você pode apenas focar nas seguintes funções para
# configurar o arranjo/exibição:
#   -   setup(width, height, startx, starty)
#           Define o tamanho e posição da tela/janela principal. Os
#           parâmetros são:
#           - width - se um inteiro, um tamanho em pixels, se float, uma
#               fração da tela; o default é 50% da tela.
#           - height - se um inteiro, a altura em pixels, se float, uma
#               fração da tela; default é 75%.
#           - startx - se positivo, a posição inicial em pixels da borda
#               esquerda da tela, se negativo da borda direita, se None, centraliza horizontalmente
#           - starty - se positivo, posição inicial em pixels da borda superior
#               da tela, se negativo da borda inferior, se None, centraliza verticalmente.
#   -   title(titlestring)
#           Define o título da tela/janela.
#   -   exitonclick()
#           Desliga a tela/janela do módulo turtle quando usar cliques com o botão.
#   -   bye()
#           Desliga a tela/janela do módulo turtle.
#   -   done()
#           Inicia o loop do evento principal; este deve ser a última declaração
#           em um programa do turtle graphics.
#   -   speed(speed)
#           A velocidade de desenho a ser usada, padrão é 3. Quanto maior
#           o valor, mais rápido o desenho é feito, aceita valores de 0 a 10.
#   -   turtle.tracer(n = None)
#           Isto pode ser usado para agrupar atualizações à tela de gráficos do turtle.
#           É bastante útil quando um desenho se torna grande e complexo.
#           Definindo um número (n) para um valor grande(por exemplo, 600)
#           então 600 elementos serão desenhados na memória antes da tela
#           de fato ser atualizada de uma vez; isto pode agilizar a geração
#           de, por exemplo, uma figura fractal. Quando chamado sem argumentos,
#           retorna o valor salvo de n.
#   -   turtle.update()
#           Realiza uma atualização da tela do turtle; isto deveria ser
#           chamado no fim de um programa quando tracer() foi usado pois
#           garantirá que todos os elementos foram desenhados mesmo se
#           o valor de corte de tracer não tenha sido atingida.
#   -   pencolor(color)
#           usado para definir a cor usada para desenhar linhas na tela;
#           a cor pode ser especificada de diversos modos, incluindo
#           usando conjunto de cores nomeadas como 'red', 'blue', 'green'
#           ou usando códigos de cores RGB ou especificando a cor usando
#           números hexadecimais. Para mais informação das cores nomeadas
#           e códigos RGB para usar consultar  https://www.tcl.tk/man/tcl/TkCmd/colors.htm.
#           Note que todos os métodos de cores usam soletrações americanas (por exemplo, o método é pencoLOR e não pencoLOUR)
#   -   fillcolor(color)
#           usado para definir a cor para usar para preencher áreas fechadas
#           dentro de linhas desenhadas.
# A seguinte seção de código ilustra algumas destas funções:
# Definir um tótulo para a janela de tela de pintura:
# turtle.title("Meu desenho com Turtle")

# Define o tamanho da tela e o ponto inicial (0, 0)
# turtle.setup(width=200, height=200, startx=0, starty=0)

# Define a cor da caneta como vermelha
# turtle.pencolor("red")
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)

# Acrescente isso para fechar a janela quando clicar nela
# turtle.exitonclick()

# Agora podemos olhar em como, de fato, desenhar uma forma na tela.
# O cursor na tela tem diversas propriedades; elas incluem a cor de desenho
# atual da caneta que move o cursor, mas também sua posição atual
# (nas coordenadas x, y da tela) e a direção para a qual está virado.
# Já vimos que você pode controlar uma dessas propriedades usando o
# método pencolor(), outros métodos são usados para controlar o cursor
# e são apresentados abaixo. A direção em que o cursor está apontando pode
# ser alterada usando diversas funções incluindo:
#   - right(angle) : Vira o cursor à direita por unidades de ângulo.
#   - left(angle) : Vira o cursor à esquerda por unidades de ângulo.
#   - setheading(to_angle) : Define a orientação do cursor para to_angle.
#       Onde 0 é leste, 90 é norte, 180 é oeste e 270 é sul.
# Você pode mover o cursor (e, se a caneta está para baixo, irá
# desenhar uma linha) usando:
#   - forward(distance) : move o cursor para a frente pela distância
#       especificada na direção que o cursor está apontando. Se a caneta
#       está para baixo, então desenha uma linha.
#   - backward(distance) : move o cursor para trás pela distância na direção
#       oposta que o cursor está apontando.
# Você também pode explicitamente posicionar o cursor:
#   - goto(x, y) : move o cursor para a posição x, y. Se a caneta está para
#       baixo, desenha uma linha, Você também pode usar passos e definir
#       posição para fazer a mesma coisa.
#   - setx(x) : define a coordenada x do cursor, deixa a coordenada y inalterada.
#   - sety(y) : define a coordenada y do cursor, deixa a coordenada x inalterada.
# Também é possível mover o cursor sem desenhar modificando se a caneta está
# erguida ou não:
#   - penup() : ergue a caneta - mover o cursor não desenhará mais uma linha.
#   - pendown() : abaixa a caneta - mover o cursor desenhará uma linha.
# Também pode-se controlar o tamanho da caneta:
#   - pensize(width) : define a espessura da linha como width. O método
#       width() é um pseudônimo deste método.
# Também pode-se desenhar um círculo ou um ponto:
#   - circle(radius, extent, steps) : desenha um círculo usando o raio dado.
#       A extensão(extent) determina quanto do círculo é desenhado; se a
#       extensão não é dada, então o círculo inteiro é desenhado. Steps
#       indica o número de passos a serem usados para desenhar o círculo (pode ser usado para desenhar polígonos regulares).
#   - dot(size, color) : desenha um círculo preenchido com o diâmetro de size com a cor especificada.
# para não mostrar o cursor enquanto o desenho está sendo feito, pode-se usar
# turtle.hideturtle().
# ----------------------------------------------------
# Desenhar formas
# Obviamente, você não precisa usar apenas valores fixos para as formas
# que você desenha, pode-se usar variáveis ou calcular posições baseado
# em expressões etc.
# Por exemplo, o seguinte programa cria uma sequência de quadrados
# rotacionados em torno de um lugar central para criar uma imagem envolvente:
import turtle


def setup():
    """Provide the config for the screen"""
    turtle.title("Multiple Squares Animation")
    turtle.setup(300, 300, 0, 0)
    turtle.hideturtle()


def draw_square(size):
    """Draw a square in the current direction"""
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)


# setup()
# for _ in range(0, 12):
#     draw_square(50)
#     # Rotate the starting direction
#     turtle.right(120)
# # Add this so that the window will close when clicked on
# turtle.exitonclick()

# Neste programa, duas funções foram definidas, uma para preparar a tela ou
# janela com um título e um tamanho e para esconder o cursor. A segunda função
# pega um parâmetro de tamanho e o usa para desenhar um quadrado. O corpo
# principal do programa, então, prepara a janela e usa um loop for para
# desenhar 12 quadrados de 50 pixels cada continuamente rotacionando 120° entre
# cada quadrado. Note que, como não precisamos referenciar o a variável do
# loop estamos usando o formato '_' que é considerado um loop com variável
# anônima em Python.
# ------------------------------------------------
# Também é possível preencher a área dentro de uma forma desenhada. Por
# exemplo, você poderia querer preencher um dos quadrados que desenhamos.
# Para fazer isto, podemos usar as funções begin_fill() e end_fill().
#   - begin_fill() indica que formas deveriam ser preenchidas com a
#       cor de preenchimento atual, esta função deve ser chamada antes
#       desenhar a forma a ser preenchida.
#   - end_fill() chamada após a forma a ser preenchida é terminada. Isto
#       causará, então, a forma desenhada após a última chamada de begin_fill()
#       a ser preenchida usando a cor de preenchimento atual.
#   - filling() Retorna o estado do preenchimento atual (True se preenchendo e False se não)
# O seguinte programa usa isto (e a função anterior draw_square()) para desenhar
# um quadrado preenchido:
# turtle.title("Filled Square Example")
# turtle.setup(300, 300, 0, 0)
# turtle.hideturtle()
# turtle.pencolor("red")
# turtle.fillcolor("yellow")
# for x in range(0, 12):
#     turtle.begin_fill()
#     draw_square(60)
#     turtle.end_fill()
#     # Rotate the starting direction
#     turtle.right(120)
#     if x % 3 == 0:
#         turtle.fillcolor("red")
#     elif x % 3 == 1 :
#         turtle.fillcolor("green")
#     else:
#         turtle.fillcolor("orange")
# # Add this so that the window will close when clicked on

# turtle.done()

# --------------------------------
# Outras bibliotecas gráficas
# Essas bibliotecas precisam ser baixadas via anaconda, pip ou pycharm
# para poderem ser usadas:
#   - PyQtGraph : É uma biblioteca em Python puro orientada a aplicações
#                   gráficas matemáticas, científicas e de engenharia, assim
#                   como aplicações GUI. <http://www.pyqtgraph.org>
#   - Pillow : É uma biblioteca de criação de imagens (baseada na biblioteca
#                   Python Imaging PIL).<https://pillow.readthedocs.io/en/stable>
#   - Pyglet : É outra biblioteca de ciração de janelas e biblioteca multimídia
#               para Python.<https://bitbucket.org/pyglet/pyglet/wiki/Home>
# ---------------------------------
# Gráficos 3D
# Apesra de possível criar boas imagens 3D com Turtle Graphics, essa não
# é o objetivo principal da biblioteca; existem outras especializadas em
# imagens 3d, algumas delas sendo: Panda3d(https://www.panda3d.org),
# VPython (https://vpython.org), pi3d (https://pypi.org/project/pi3d) e
# PyOpenGL.
