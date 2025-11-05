# Capítulo 6 - Criação de gráficos com pyplot do Matplotlib
# O propósito do módulo pyplot e a API que ele apresenta é simplificar a geração
# e manipulação de gráficos do Matplotlib. Por si só, a biblioteca Matplotlib inteira
# tenta tornar as coisas simples fáceis e coisas complexas possíveis. O modo
# primário em que ela consegue o primeiro desses objetivos é pela API pyplot pois
# esta API tem funções de alto nível como bar(), plot(), scatter() e pie() que
# tornam fácil a criação de gráficos de barra, linha, dispersão e pizza.
# Um ponto para tomar cuidado sobre as funções do pyplot é que elas podem, muitas
# vezes, pegar muitos parâmetros; entretanto, a maioria desses parâmetros terão
# valores padrão que, em muitas situações, lhe darão um comportamento padrão ou
# representação visual razoáveis. Você pode, portanto, ignorar a maioria dos parâmetros
# disponíveis até a hora em que você queira mudar algo, quando, então, deverá olhar
# a documentação do Matplotlib.
# A API pyplot pode ser usada para:
#   - construir o gráfico
#   - configurar rótulos e eixos
#   - gerenciar estilos de cor e linha
#   - lidar com eventos/permitir gráficos interativos
#   - mostrar o gráfico.
# -----------------------------------------------------
# Gráficos de Linha
# Um gráfico de linha é um gráfico onde os pontos (às vezes chamados marcadores)
# são conectados com linhas para mostrar como alguma coisa muda de valor conforme
# um conjunto de valores (normalmente o eixo x) muda; por exemplo, sobre um série
# em intervalos de tempo (Séries temporais). Gráficos de linha de séries temporais
# são tipicamente desenhados em ordem cronológica; tais gráficos são conhecidos
# como gráficos de execução (run chart).
# O exemplo abaixo cria um gráfico de execução

##########################################
# import matplotlib.pyplot as pyplot

# # Prepara os dados
# x = [0, 1, 2, 3, 4, 5, 6]
# y = [0, 2, 6, 14, 30, 43, 75]

# # Define os nomes dos eixos
# pyplot.ylabel("Velocidade", fontsize=12)
# pyplot.xlabel("Tempo", fontsize=12)

# # Define o título
# pyplot.title("Velocidade v Tempo")

# # Plota a mostra o gráfico usando círculos azuis como marcadores ('bo') e uma linha sólida ('-')
# pyplot.plot(x, y, "bo-")
# pyplot.show()

##########################################

# Strings codificadas de formato (Coded Format Strings)
# Há diversas opções que podem ser fornecidas pela string de formatação, as seguintes
# tabelas sumariza algumas:
#
#
# Caractere      Cor
#   'b'         azul
#   'g'         verde
#   'r'         vermelho
#   'c'         ciano
#   'm'         magenta
#   'y'         amarelo
#   'k'         preto
#   'w'         branco

# Diferentes formas de representar como os marcadores (pontos do gráfico)
# também podem ser escolhidos:
# Caractere          Descrição
# '.'           ponto
# ','           pixel
# 'o'           circulo
# 'v'           triangulo para baixo (triangle_down)
# '^'           triangulo para cima (triangle_up)
# '<'           triangulo para esquerda (triangle_left)
# '>'           triangulo para direita (triangle_right)
# 's'           quadrado
# 'p'           pentagono
# '*'           estrela
# 'h'           hexagono
# '+'           mais
# 'x'           x
# 'D'           diamante

# Por fim, a string de formatação permite diferentes estilos de linha

# Caractere         Descrição
#   '-'             Linha sólida
#   '--'            linha tracejada
#   '-.'            linha-ponto
#   ':'             pinha pontilhada

# ------------------------------
# Gráfico de dispersão
# É um tipo de gráfico onde valores individuais são indicados usando coordenadas
# cartesianas (ou x e y) para mostrar valores. Cada valor é indicado por uma
# marcação (como círculo ou triângulo) no gráfico.
# O programa abaixo ilustra um exemplo de gráfico de dispersão:
##########################################3

# import matplotlib.pyplot as pyplot

# # Cria os dados
# dirigindo = (
#     (17, 18, 21, 22, 19, 21, 25, 22, 25, 24),
#     (3, 6, 3.5, 4, 5, 6.3, 4.5, 5, 4.5, 4),
# )
# nadando = (
#     (17, 18, 20, 19, 22, 21, 23, 19, 21, 24),
#     (8, 9, 7, 10, 7.5, 9, 8, 7, 8.5, 9),
# )
# navegando = (
#     (31, 28, 29, 36, 27, 32, 34, 35, 33, 39),
#     (4, 6.3, 6, 3, 5, 7.5, 2, 5, 7, 4),
# )

# pyplot.scatter(
#     x=dirigindo[0],
#     y=dirigindo[1],
#     c="red",
#     marker="o",
#     label="dirigindo",
#     linewidths=3,
#     edgecolors="black",
# )
# pyplot.scatter(x=nadando[0], y=nadando[1], c="green", marker="^", label="nadando")
# pyplot.scatter(x=navegando[0], y=navegando[1], c="blue", marker="*", label="navegando")

# pyplot.xlabel("Idade")
# pyplot.ylabel("Horas")
# pyplot.title("Gráfico de dispersão de atividades")
# pyplot.legend()
# pyplot.show()

######################################
# Outras opções disponíveis na função pyplot.scatter() incluem:
#   * alpha: indica o valor de transparência, entre 0(transparente) e 1(opaco).
#   * linewidths: é usado para indicar a largura da linha do contorno dos marcadores.
#   * edgecolors: indica a cor a ser usada para o contorno dos marcadores se diferente
#               da cor de preenchimento (indicada pelo parâmetro 'c')
# --------------------------------------------------
# Quando usar gráficos de dispersão
# Em geral, são usados quando é necessário mostrar a relação entre duas variáveis.
# Gráficos de dispersão são, às vezes, chamados de gráficos de correlação pois
# mostram como duas variáveis são correlacionadas.
# Em muitos casos, uma tendência pode ser observada entre os pontos plotados em
# um gráfico de dispersão. Para ajudar a visualizar a tendência, pode ser útil
# desenhar uma linha de tendência na direção do gráfico de espalhamento. Ela ajuda a
# tornar a relação entre os gráficos de espalhamento ainda mais clara.
# A linha pode ser criada usando a função donumpy polyfit(). Ela realiza um ajuste polinomial
# de mínimos quadrados para os dados que são dados. Uma classe poly1d é, então, criada
# baseada na matriz retornada por polyfit(). Esta classe é uma classe polinomial
# unidimensional. Ela é usada para encapsular operações 'naturais' de polinômios.
# O objeto poly1D é, então, usado para gerar um grupo de valores para uso com o
# conjunto de valores x para a função pyplot.plot().

#####################################
# import numpy as np
# import matplotlib.pyplot as pyplot

# x = (5, 5.5, 6, 6.5, 7, 8, 9, 10)
# y = (120, 115, 100, 112, 80, 85, 69, 65)

# pyplot.scatter(x, y)

# z = np.polyfit(x, y, 1)
# p = np.poly1d(z)
# pyplot.plot(x, p(x), "r")

# pyplot.show()
#####################################
# Gráficos de pizza
# É umtipo de gráfico no qual um círculo é dividido em setores, cada um representando
# uma proporção do total. Uma fatia do círculo representa a contribuição de uma categoria
# para o total geral. Tipicamente, os diferentes setores do gráfico de pizza são apresentados
# em cores diferentes e são arranjados no sentido horário pelo gráfico em ordem de magnitude.
# Entretanto, se houver uma fatia que não contem uma categoria única de dados mas
# sumariza muitas, por exemplo 'outros tipos' ou 'outras respostas', então mesmo que
# não seja a menor categoria, é comum colocá-la por último. é criado com a função
# pyplot.pie()
# ##############################
# import matplotlib.pyplot as pyplot

# labels = ("Python", "Java", "Scala", "C#")
# sizes = [45, 30, 15, 10]

# pyplot.pie(sizes, labels=labels, autopct="%1.f%%", counterclock=False, startangle=90)

# pyplot.show()

########################################3
# O único parâmetro obrigatório de pyplot.pie é o primeiro que fornece os valores
# a serem usados para as fatias. Os seguintes parâmetros são usados no exemplo acima:
#   * labels: parâmetro opcional que pega uma sequência de strings que são
#           usadas para fornecer rótulos para cada fatia.
#   * autopct: parâmetro que pega uma string (ou função) para ser usada para formatar
#           os valores numéricos usados com cada fatia.
#   * counterclockwise: Por padrão, as fatias são plotadas no sentido antihorário
#           pelo pyplot, então colocando este parâmetro como False respeita o padrão do sentido horário.
#   * startangle: O ângulo inicial foi movido para 90° usando este parâmetro de modo que
#           o primeiro segmento inicia no topo do gráfico.
# ----------------------------------------
# Expandindo segmentos
# Pode ser útil enfatizar um segmento em particular do gráfico de pizza
# através da 'explosão' dele; isto é, separá-lo do resto do gráfico.
# Isto pode ser feito usando o parâmetro explode da função pie() que pega uma
# sequência de valores indicando por quanto um segmento deve ser explodido.
# O umpacto visual do gráfico também pode ser aumentado adicionando uma
# sombra aos segmentos usando o parâmetro booleano nomeado 'shadow'.

#######################################
# import matplotlib.pyplot as pyplot

# labels = ("Python", "Java", "Scala", "C#")
# sizes = [45, 30, 15, 10]
# # only "explode" the 1st slice (i.e. 'Python')
# explode = (0.1, 0, 0, 0)
# pyplot.pie(
#     sizes,
#     explode=explode,
#     labels=labels,
#     autopct="%1.f%%",
#     shadow=True,
#     counterclock=False,
#     startangle=90,
# )
# pyplot.show()
########################################
# Quando usar gráficos de pizza
# É útil considerar quais dados podem/devem ser apresentados usando
# este tipo de gráfico. Em geral, eles são úteis para mostrar dados
# que podem ser classificados em categorais nominais ou ordinais.
# Dados nominais são categorizados de acordo com informação descritiva
# ou qualitativa como linguagens de programação, tipo de carro, país
# de nascimento etc. Dados ordinais são similares, mas as categorias
# também podem ser classificadas, por exemplo, em um questionário
# pessoas poderiam ser perguntadas se elas classificam algo como muito
# ruim, ruim, normal, bom ou muito bom.
# Gráficos de pizza também podem ser usados para mostrar porcentagens ou
# dados proporcionais e geralmente a porcentagem representada por cada
# categoria é fornecida próxima à fatia correspondente. Também costuma-se
# limitar sua apresentação quando existem até 6 categorias, pois categorias
# demais dificultam sua visualização e intepretação.
# ------------------------------------------------
# Gráficos de barras
# Um gráfico de barra é um tipo de gráfico que é usado para apresentar categorias
# discretas de dados. Os dados são, geralmente, apresentados verticalmente,
# mas em alguns casos pode-se utilizar barras laterais. Cada categoria é
# representada por uma barra cuja altura (ou largura) representa o dado
# daquela categoria.
# Como é fácil interpretar gráficos de barras, e como cada categoria se
# relaciona com a outra, eles são um dos tipos de gráficos mais comuns.

#############################################
# import matplotlib.pyplot as pyplot

# # Set up the data
# labels = ("Python", "Scala", "C#", "Java", "PHP")
# index = (1, 2, 3, 4, 5)  # provides locations on x axis
# sizes = [45, 10, 15, 30, 22]
# # Set up the bar chart
# pyplot.bar(index, sizes, tick_label=labels)
# # Configure the layout
# pyplot.ylabel("Usage")
# pyplot.xlabel("Programming Languages")
# # Display the chart
# pyplot.show()
#############################################
# Gráficos de barras horizontais
# Apesar da representação com as barras verticais ser mais comumente utilizada,
# também é possível criar gráficos com as barras horizontais. Isto é um
# modo efetivo de apresentar diversas categorias quando há espaço insuficiente
# para preencher todas as colunas necessárias na página.
# A função pyplot.barh() é usada para gerar este tipo de gráficos. Para
# isso, basta substituir pyplot.bar(...) no código acima por pyplot.barh(...).
# ----------------------------------------------
# Barras coloridas
# Também é comum colorir barras diferentes com cores diferentes ou usando
# tons diferentes. Isto ajuda a distinguir uma barra da outra.
# A cor a ser usada em cada categoria pode ser indicada pelo parâmetro
# 'color' para a função bar() (ou barh()). Esta é a sequência de cores
# a serem aplicadas. Por exemplo, pode-se colocar o seguinte na linha
# equivalente do código acima:
# pyplot.bar(x_values, sizes, tick_label=labels, color=('red','green', 'blue', 'yellow', 'orange'))
# --------------------------------------------
# Gráficos de barras também podem ser empilhados. Isto pode ser um
# modo de mostrar valores totais (e quais são as contribuições para aqueles
# valores) em diversas categorias. Isto é, um jeito de visualizar totais
# gerais, para diferentes categorias baseado em como diferentes elementos
# contribuem para os totais.
# Diferentes cores são usadas para os diferentes subgrupos que contribuem
# para a barra geral. Nestes casos, uma legenda é geralmente fornecida
# para indicar a qual subgrupo cada tom/cor representa.
# Por exemplo, o seguinte exemplo ilustra este tipo de gráfico:

#############################################3
# import matplotlib.pyplot as pyplot

# # Set up the data
# labels = ("Python", "Scala", "C#", "Java", "PHP")
# index = (1, 2, 3, 4, 5)
# web_usage = [20, 2, 5, 10, 14]
# data_science_usage = [15, 8, 5, 15, 2]
# games_usage = [10, 1, 5, 5, 4]
# # Set up the bar chart
# pyplot.bar(index, web_usage, tick_label=labels, label="web")
# pyplot.bar(
#     index, data_science_usage, tick_label=labels, label="data science", bottom=web_usage
# )
# web_and_games_usage = [
#     web_usage[i] + data_science_usage[i] for i in range(0, len(web_usage))
# ]
# pyplot.bar(
#     index, games_usage, tick_label=labels, label="games", bottom=web_and_games_usage
# )
# # Configure the layout
# pyplot.ylabel("Usage")
# pyplot.xlabel("Programming Languages")
# pyplot.legend()
# # Display the chart
# pyplot.show()
############################################
# Uma coisa para se notar neste exemplo é que após o primeiro conjunto de valores
# ser adicionado usando pyplot.bar(), é necessário especificar o local
# inferior para o próximo gruoi de barras usando o parâmetro bottom.
# -----------------------------------------------
# Gráficos de barras agrupados
# Por fim, Gráficos de barras agrupados são um jeito de mostrar informação
# sobre diferentes subgrupos das principais categorias. Nestes casos, uma
# legenda é geralmente apresentada para indicar qual subgrupo de cada tom/
# cor representa.
# Para uma categoria particular, gráficos de barras separados são desenhados
# para cada um dos subgrupos. Por exemplo, no seguinte gráfico, os
# resultados obtidos para dois conjuntos de times através de uma série
# de exercícios de laboratórios são mostrados. Assim, cada time tem uma barra
# para lab1, lab2, lab3, etc.

#####################################
# import matplotlib.pyplot as pyplot

# BAR_WIDTH = 0.35
# # set up grouped bar charts
# teama_results = (60, 75, 56, 62, 58)
# teamb_results = (55, 68, 80, 73, 55)
# # Set up the index for each bar
# index_teama = (1, 2, 3, 4, 5)
# index_teamb = [i + BAR_WIDTH for i in index_teama]
# # Determine the mid point for the ticks
# ticks = [i + BAR_WIDTH / 2 for i in index_teama]
# tick_labels = ("Lab 1", "Lab 2", "Lab 3", "Lab 4", "Lab 5")
# # Plot the bar charts
# pyplot.bar(index_teama, teama_results, BAR_WIDTH, color="b", label="Team A")
# pyplot.bar(index_teamb, teamb_results, BAR_WIDTH, color="g", label="Team B")
# # Set up the graph
# pyplot.xlabel("Labs")
# pyplot.ylabel("Scores")
# pyplot.title("Scores by Lab")
# pyplot.xticks(ticks, tick_labels)
# pyplot.legend()
# # Display the graph
# pyplot.show()
#####################################
# Figuras e subgráficos
# Uma figura do Matplotlib é um objeto que contém todos os elementos gráficos
# mostrados em um gráfico. Isto é, os eixos, a legenda, o título assim como
# os dados do gráfico, seja um gráfico de linha, dispersão, barras ou outro.
# Assim, representa a janela, ou página, total e é o principal componente
# gráfico.
# Em muitos casos, a figura é implícita conforme o desenvolvedor interage com
# a API pyplot; entretanto, a figura pode ser acessada diretamente se
# necessário.
# A função matplotlib.pyplot.figure() gera um objeto figura. Esta função
# retorna um objeto matplotlib.figure.Figure. É, então, possível interagir
# diretamente com o objeto figura. Por exemplo, é possível acrescentar eixos
# à figura, adicionar subgráficos etc.
# Trabalhar diretamente com a figura é necessário se você quer acrescentar
# múltiplos subgráficos a ela. Isto pode ser útil se quiser comparar diferentes
# visualizações do mesmo dado lado a lado.
# Um ou mais subgráficos podem ser acrescentados a uma figura pelo método
# figure.add_subplot(). Ele acrescenta um Eixo(Axes) à figura como um
# de um conjunto de um ou mais subgráficos. Um subgráfico pode ser acrescentado
# usando um número inteiro de 3 dígitos (ou três inteiros separados)
# indicando a posição do subgráfico. Os dígitos representam o número de
# linhas, colunas e o índice do subgráfico dentro da matriz resultante.
# Portanto, 2, 2, 1(e 221) indicam que o subgráfico irá assumir o primeiro
# índice dentro de uma grade de gráficos 2 x 2. 2, 2, 3 (223) indica que
# o subgráfico estará no índice 3 que será a linha 2 e coluna 1 dentro
# da grade de gráficos. Por exemplo, o seguinte código ilustra esse tipo:

#########################################
# Atenção: No livro, as posições(position) estão dadas como argumento para
# figure.add_subplot(x) na forma de strings, mas devem ser inteiros.
# # No código abaixo, os argumentos já estão transformados para int.
# import matplotlib.pyplot as pyplot

# t = range(0, 20)
# s = range(30, 10, -1)
# # Set up the grid of subplots to be 2 by 2
# grid_size = "22"
# # Initialize a Figure
# figure = pyplot.figure()
# # Add first subplot
# position = grid_size + "1"
# print("Adding first subplot to position", position)
# axis1 = figure.add_subplot(int(position))
# axis1.set(title="subplot(2,2,1)")
# axis1.plot(t, s)
# # Add second subplot
# position = grid_size + "2"
# print("Adding second subplot to position", position)
# axis2 = figure.add_subplot(int(position))
# axis2.set(title="subplot(2,2,2)")
# axis2.plot(t, s, "r-")
# # Add third subplot
# position = grid_size + "3"
# print("Adding third subplot to position", position)
# axis3 = figure.add_subplot(int(position))
# axis3.set(title="subplot(2,2,3)")
# axis3.plot(t, s, "g-")
# # Add fourth subplot
# position = grid_size + "4"
# print("Adding fourth subplot to position", position)
# axis4 = figure.add_subplot(int(position))
# axis4.set(title="subplot(2,2,4)")
# axis4.plot(t, s, "y-")
# # Display the chart
# pyplot.show()

#########################################################
# Gráficos 3D
# Este tipo de gráfico é usado para plotar relações entre três conjuntos
# de valores ( em vez de dois, como os exemplos acima), sendo utilizados
# os eixos x, y e z.
# O seguinte programa cria um gráfico 3D simples usando dois conjuntos
# de valores gerados usando a função do numpy 'range()'. Os valores do
# eixo z são criados usando a função do numpy 'sin()'. O gráfico de superfície
# 3D é plotado usando a função plot_surface() do objeto eixos futuros.
# Ele, então, pega as coordenadas x, y, e z.
#

###################################
# Atenção: no livro, é usado axes = figure.gca(projection='3d') para obter
# os eixos 3D, mas isso é incorreto. O correto é usar a seguinte linha:
# axes = figure.add_subplot(111, projection="3d")

# import matplotlib.pyplot as pyplot

# # Import matplotlib colour map
# from matplotlib import cm as colourmap

# # Required for £D Projections
# from mpl_toolkits.mplot3d import Axes3D

# # Provide access to numpy functions
# import numpy as np

# # Make the data to be displayed
# x_values = np.arange(-6, 6, 0.3)
# y_values = np.arange(-6, 6, 0.3)
# # Generate coordinate matrices from coordinate vectors
# x_values, y_values = np.meshgrid(x_values, y_values)
# # Generate Z values as sin of x plus y values
# z_values = np.sin(x_values + y_values)
# # Obtain the figure object
# figure = pyplot.figure()
# # Get the axes object for the 3D graph
# axes = figure.add_subplot(111, projection="3d")
# # Plot the surface.
# surf = axes.plot_surface(x_values, y_values, z_values, cmap=colourmap.coolwarm)
# # Add a color bar which maps values to colors.
# figure.colorbar(surf)
# # Add labels to the graph
# pyplot.title("3D Graph")
# axes.set_ylabel("y values", fontsize=8)
# axes.set_xlabel("x values", fontsize=8)
# axes.set_zlabel("z values", fontsize=8)
# # Display the graph
# pyplot.show()
###########################################3
