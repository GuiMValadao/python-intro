# Capítulo 4 - CGA (Arte gerada por computador)
# Arte de computador é definida como qualquer arte que usa um computador.
# Entretanto, no contexto deste livro, é usada como arte que é gerada
# por um computador, ou, mais especificamente, programa de computador.
# A seguinte seção de código gera uma imagem através de uma função recursiva
# que desenha um círculo em um determinada posição x, y de um tamanho
# especificao. A função chama a si própria recursivamente modificando seus
# parâmetros para desenhar círculos cada vez menores até terem menos de 20 pixels.

##############################
# import turtle

# WIDTH = 640
# HEIGHT = 360


# def setup_window():
#     # Set up the window
#     turtle.title("Circles in My Mind")
#     turtle.setup(WIDTH, HEIGHT, 0, 0)
#     turtle.colormode(255)  # Indicates RGB numbers will be in
#     # the range 0 to 255
#     turtle.hideturtle()
#     # Batch drawing to the screen for faster rendering
#     turtle.tracer(2000)
#     # Speed up drawing process
#     turtle.speed(10)
#     turtle.penup()


# def draw_circle(x, y, radius, red=50, green=255, blue=10, width=7):
#     """Draw a circle at a specific x, y location.
#     Then draw four smaller circles recursively"""
#     colour = (red, green, blue)
#     # Recursively drawn smaller circles
#     if radius > 50:
#         # Calculate colours and line width for smaller circles
#         if red < 216:
#             red = red + 33
#             green = green - 42
#             blue = blue + 10
#             width -= 1
#         else:
#             red = 0
#             green = 255
#         # Calculate the radius for the smaller circles
#         new_radius = int(radius / 1.3)
#         # Drawn four circles
#         draw_circle(int(x + new_radius), y, new_radius, red, green, blue, width)
#         draw_circle(x - new_radius, y, new_radius, red, green, blue, width)
#         draw_circle(x, int(y + new_radius), new_radius, red, green, blue, width)
#         draw_circle(x, int(y - new_radius), new_radius, red, green, blue, width)
#     # Draw the original circle
#     turtle.goto(x, y)
#     turtle.color(colour)
#     turtle.width(width)
#     turtle.pendown()
#     turtle.circle(radius)
#     turtle.penup()


# # Run the program
# print("Starting")
# setup_window()
# draw_circle(25, -100, 200)
# # Ensure that all the drawing is rendered
# turtle.update()
# print("Done")
# turtle.done()
##############################

# Alguns pontos para se notar sobre este programa: Ele usa recursão para
# desenhar os círculos até eles chegarem a um determinado tamanho(o ponto
# de término); ele também usa turtle.tracer() para acelerar o desenho
# pois usa o buffer para preparar 2000 mudanças antes de atualizar a tela;
# por fim, as cores dos círculos são alteradas em cada nível de recessão.
# -----------------------------------------
# Um Gerador de arte de computador
# Como outro exemplo de como pode-se usar Turtle Graphics para criar arte
# de computador, o seguinte programa gera cores RGB aleatoriamente para
# usar para as linhas sendo desenhadas, o que dá mais interesse à figura.
# Também permite o usuário fornecer um ângulo para usar quando alterar a
# direção em qua a linha é desenhada. Como o desenho é feito dentro de um
# loop, mesmo esta mudança simples ao ângulo usado para desenhar as linhas
# pode criar imagens bastante diferentes.

#############################################
# import turtle
# from random import randint


# def get_input_angle():
#     """Obtain input from user and convert to an int"""
#     message = "Please provide an angle:"
#     value_as_string = input(message)
#     while not value_as_string.isnumeric():
#         print("The input must be an integer!")
#         value_as_string = input(message)
#     return int(value_as_string)


# def generate_random_colour():
#     """Generates an R,G,B values randomly in range
#     0 to 255"""
#     r = randint(0, 255)
#     g = randint(0, 255)
#     b = randint(0, 255)
#     return r, g, b


# print("Set up Screen")
# turtle.title("Colourful pattern")
# turtle.setup(640, 600)
# turtle.hideturtle()
# turtle.bgcolor("black")  # Set the background colour of the screen
# turtle.colormode(255)  # Indicates RGB numbers will be in the range 0 to 255
# turtle.speed(10)
# angle = get_input_angle()
# print("Start the drawing")
# for i in range(0, 200):
#     turtle.color(generate_random_colour())
#     turtle.forward(i)
#     turtle.right(angle)
# print("Done")
# turtle.done()

###########################################
# Fractais em Python
# Dentro da área de arte de Computadores, Fractais são uma forma de arte
# bem conhecida. Fractais são padrões recorrentes que são calculados ou
# usando uma abordagem iterativa (como um loop for) ou uma abordagem
# recursiva (quando uma função chama si própria mas com parâmetros
# alterados). Uma das características interessantes de fractais é que eles
# exibem o mesmo padrão (ou quase o mesmo padrão) em niveis sucessivos de
# granularidade. Isto é, se expandir a imagem se encontraria o mesmo padrão
# sendo repetido em níveis cada vez menores. Isto é conhecido como simetria
# expansiva ou simetria de desdobramento; se esta replicação é exatamente a
# mesma em todas as escalas, então é chamada auto-similar.
# Fractais tem suas raízes no mundo da matemática do século XVII, com o termo
# 'fractal' sendo criado no século XX pelo matemático Benoit Mandelbrot.
# Uma descrição amplamente citada que Mandelbrot publicou descreve que a
# geometria fractal é:
#   uma forma geométrica grosseira ou fragmentada que pode ser dividida
#   em partes, cada qual é (pelo menos aproximadamente), uma cópia em tamanho
#   reduzido da forma inteira.
# Desde o fim do século XX, fractais tem sido um método comumente usado de
# criar arte de computador.
# Um exemplo de fractal frequentemente usado na arte de computador é o
# floco de neve de Koch, e outro é o conjunto de Mandelbrot.
# ------------------------------------------
# Floco de neve de Koch
# É um fractal que inicia com um triângulo equilátero e então substitui o meio
# de cada segmento de linha com um par de segmentos de linha que formam
# uma lombada equilátera. Esta substituição pode ser feita com qualquer
# profundidade, gerando triângulos cada vez menores até a forma geral lembrar
# um floco de neve.
#
##################################################
import turtle

# # Set up Constants
# ANGLES = [60, -120, 60, 0]
# SIZE_OF_SNOWFLAKE = 300


# def get_input_depth():
#     """Obtain input from user and convert to an int"""
#     message = "Please provide the depth (0 or a positive interger):"
#     value_as_string = input(message)
#     while not value_as_string.isnumeric():
#         print("The input must be an integer!")
#         value_as_string = input(message)
#     return int(value_as_string)


# def setup_screen(
#     title, background="white", screen_size_x=640, screen_size_y=320, tracer_size=800
# ):
#     print("Set up Screen")
#     turtle.title(title)
#     turtle.setup(screen_size_x, screen_size_y)
#     turtle.hideturtle()
#     turtle.penup()
#     turtle.backward(240)
#     # Batch drawing to the screen for faster rendering
#     turtle.tracer(tracer_size)
#     turtle.bgcolor(background)  # Set the background colour of the screen


# def draw_koch(size, depth):
#     if depth > 0:
#         for angle in ANGLES:
#             draw_koch(size / 3, depth - 1)
#             turtle.left(angle)
#     else:
#         turtle.forward(size)


# depth = get_input_depth()
# setup_screen(
#     "Koch Snowflake (depth " + str(depth) + ")",
#     background="black",
#     screen_size_x=420,
#     screen_size_y=420,
# )
# # Set foreground colours
# turtle.color("sky blue")
# # Ensure snowflake is centred
# turtle.penup()
# turtle.setposition(-180, 0)
# turtle.left(30)
# turtle.pendown()
# # Draw three sides of snowflake
# for _ in range(3):
#     draw_koch(SIZE_OF_SNOWFLAKE, depth)
#     turtle.right(120)
# # Ensure that all the drawing is rendered
# turtle.update()
# print("Done")
# turtle.done()

####################################
# Conjunto de Mandelbrot
# Uma das imagens de fractais mais famosas é baseada no conjunto de Mandelbrot.
# Ele é o conjunto de números complexos c para os quais a função z*z+c não
# diverge quando iterada de z = 0 para o qual a sequência de funções
# (func(0), func(func(0)), etc) permanece ligada a um valor absoluto.
# A definição do conjunto de Mandelbrot e seu nome são devidos ao matemático
# francês Adrien Douady, que os nomeou em homenagem a Benoit Mandelbrot.
# Essas imagens podem ser criadas por amostragem dos números complexos e
# teste, para cada ponto de amostra c, se a sequência func(0), func(func(0))
# etc se direciona ao infinito (na prática, isto significa que um teste é feito
# para ver se ela deixa alguma vizinhaça predeterminada próxima de 0 após um
# número predeterminado de ações).


# IMAGE_SIZE_Y = 60
# MAX_Y = 1.5
# MIN_Y = -1.5
# IMAGE_SIZE_X = 80
# MAX_X = 1.0
# MIN_X = -2.0
# MAX_ITERATIONS = 100
# SCREEN_OFFSET_X = 0
# SCREEN_OFFSET_Y = 0
# turtle.Screen().colormode(255)

# for y in range(IMAGE_SIZE_Y):
#     zy = y * (MAX_Y - MIN_Y) / (IMAGE_SIZE_Y - 1) + MIN_Y
#     for x in range(IMAGE_SIZE_X):
#         zx = x * (MAX_X - MIN_X) / (IMAGE_SIZE_Y - 1) + MIN_X
#         z = zx + zy * 1j
#         c = z
#         for i in range(MAX_ITERATIONS):

#             if abs(z) > 2.0:

#                 break

#             z = z * z + c
#         turtle.color(i % 4 * 64, i % 8 * 32, i % 16 * 16)
#         turtle.setposition(x - SCREEN_OFFSET_X, y - SCREEN_OFFSET_Y)
#         turtle.pendown()
#         turtle.dot(i)
#         turtle.penup()
