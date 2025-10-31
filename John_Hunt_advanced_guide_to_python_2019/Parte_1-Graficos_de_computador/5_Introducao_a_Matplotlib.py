# Capítulo 5 - Introdução ao Matplotlib
# Matplotlib é uma biblioteca do Python para criação de gráficos que pode gerar
# uma grande variedade de tipos de gráficos diferentes em diversos formatos.
# Pode ser usada para gerar gráficos de linha, de dispersão, mapas de calor,
# gráficos de barras, gráficos de pizzas e gráficos 3D. Possui até suporte
# para animações e exibições interativas.
# Matplotlib pode ser usado por si só ou em conjunto com outras bibliotecas
# para fornecer uma ampla variedade de recursos. Uma biblioteca comumente
# usada em conjunto com Matplotlib é Numpy, que é frequentemente usada em
# aplicações de ciência de dados que fornece uma variedade de funções e
# estruturas de dados (como matrizes n-dimensionais).
# Neste capítulo serão introduzidos a biblioteca Matplotlib, sua arquitetura,
# os componentes que compreendem um gráfico e a API pyplot. A API pyplot é
# o modo mais simples e comum no qual um programador interage com Matplotlib.
# --------------------------------------------------------
# import matplotlib.pyplot as pyplot

# pyplot.plot([1, 0.25, 0.5, 2, 3, 3.75, 3.5])
# pyplot.show()

# ---------------------------------------------
# Componentes do gráfico
# Apesar de parecer simples, há vários elementos que compoem um gráfico no
# Matplotlib. Todos esses elementos podem ser manipulados ou modificados
# independentemente. É, portanto, útil se tornar familiar com a terminologia
# do Matplotlib associada a esses elementos, como ticks, legends, labels, etc.
# O diagrama no arquivo 'matplotlibelements.png' ilustra os seguinte
# elementos:
#   - Eixos(Axes): um eixo é definido pela classe matplotlib.axes.Axes.
#                  são usados para manter a maioria dos elementos de uma
#                  figura, em particular os eixos X e Y, Ticks, gráficos
#                  de linha, qualquer texto q quaisquer formas poligonais.
#   - Título : É o título da figura.
#   - Marcações (Ticks; Major e Minor): são representados pela classe matplotlib.axis.Tick.
#                           Um 'Tick' é uma marca no eixo indicando um novo valor.
#                           Podem haver marcações maiores(Major) que são maiores e podem ser
#                           rotulados. Também podem existir marcações menores(Minor) que também podem ser rotulados.
#   - Eixos(Axis): A classe matplotlib.axis.Axis define um objeto Axis (como eixos X ou Y)
#                   dentro de uma instância da classe pai 'Axes'. Pode ter formatadores
#                   usados para formatar os rótulos usados para as marcações maiores e menores.
#                   Também é possível definir o lugar para os locais das marcações.
#   - Rótulos dos eixos:(X, Y e em alguns casos Z): Descrevem os eixos
#   - Gráfico(Plot): tipos de gráficos como linha ou dispersão. Vários tipos de
#               gráficos são suportados por Matplotlib incluindo gráficos de linha,
#               de dispersão, de barras e de pizza.
#   - Grade(Grid): É uma grade opcional exibida por trás de um gráfico. Pode ser mostrada
#               com uma variedade de estilos de linha, cores e largura de linha diferentes.
# ---------------------------------------------------------
# Arquitetura do Matplotlib
# A biblioteca Matplotlib tem uma arquitetura em camadas que esconde grande parte
# da complexidade associada com diferentes sistemas de janelas e saídas de
# gráficos. Esta arquitetura tem três camadas principais: a Camada de Sripting,
# a Camada Artista e a Camada de Backend. Cada uma tem responsabilidades e
# componentes específicos. Por exemplo, o Backend é responsável por ler e interagir
# com o gráfico sendo gerado. A Camada Artista é responsável por criar os objetos
# do gráfico que serão renderizados pela camada Backend. Por fim, a camada de Scripting
# é usada pelo desenvolvedor para criar os gráficos.
# -------------------------------------------------
# Camada Backend
# Cuida da geração da saída para diferentes formatos alvo. O próprio Matplotlib
# pode ser usado de muitos modos diferentes para gerar muitas saídas diferentes.
# Pode ser usado interativamente, acoplado em uma aplicação (ou interface gráfica
# do usuário), usado como parte de um grupo de aplicação com grãficos sendo
# armazenados como PNG, SVG, PDF ou outros formatos de imagem etc.
# Para dar suporte a todos esses casos, Matplotlib pode buscar diferentes saídas,
# e cada uma dessas capacidades é chamada backend; o 'frontend' é o código
# mostrado ao usuário. A Camada Backend mantem todos os diferentes backend e o
# programador pode usar ou o backend padrão ou selecionar um diferente se preciso.
# O backend para ser usado pode ser definido pela função matplotlib,use(). Por
# exemplo, para definir que o backend renderize o uso de Postscript: matplotlib.use('PS'):
# import sys
# import matplotlib
# if 'matplotlib.backends' not in sys.modules:
#     matplotlib.use('PS')
# import matplotlib.pyplot as pyplot

# Deve-se notar que se for usar matplotlib.use(), isso deve ser feito antes de importar
# matplotlib.pyplot. Chamà-la depois que pyplot foi importado não terá efeito.
# O renderizador padrão é o 'Agg' que usa a biblioteca do C++ Anti-Grain Geometry
# para fazer uma imagem raster (pixel) dos gráficos de dados.
# O backend 'Agg' foi escolhido como padrão pois funciona em uma ampla seleção de
# sistemas Linux pois seus requisitos necessários são bem pequenos; outros backend
# podem funcionar em um sistema em particular, mas não em outro.
# A camada Backend pode ser dividida em duas categorias:
#   - Backends da interface do usuário (interativo) que oferecem suporte a vários
#       sistemas de janela do Python comowxWidgets, Qt, TK etc.
#   - Backends Hardcopy (não-interativo) que oferecem suporte a saídas raster e vetor gráfico.
# Ambos backend são construídos sobre abstrações em comum, referidas como Classes base Backend.
# --------------------------------------------
# A Camada Artista
# A camada artista fornece a maioria da funcionalidade que você poderia pensar
# ser o que Matplotlib faz, de fato; isto é, a geração dos gráficos que são
# renderizados/ mostrados ao usuário (ou saída em um formato em particular).
# Esta camada é responsável com coisas como as linhas, formas, eixos, texto, etc
# que fazem parte de um gráfico.
# As classes usadas pela Camada Artista podem ser classificadas em um dos seguintes
# três grupos: primitivas, recipientes e coleções:
#   - Primitivas são classes usadas para representar objetos gráficos que
#       serão desenhados em uma tela de figuras.
#   - Recipientes são objetos que guardam primitivas. Por exemplo, tipicamente
#       uma figura seria instanciada e usada para criar um ou mais eixos etc.
#   - Coleções são usadas para lidar eficientemente com grandes números de objetos
#       de tipos similares.
# Apesar de ser útil estar ciente dessas três classes, em muitos casos você não
# precisará trabalhar diretamente com elas pois a API pyplot esconde muitos
# detalhes. Entretanto, é possível trabalhar no nível de figuras, eixos, etc conforme necessário.
# ---------------------------------------------
# A camada de Scripting
# Esta camada é a interface mostrada ao desenvolvedor que simplifica a tarefa
# de trabalhar com as outras camadas.
# Note que, do ponto de vista de programadores, a Camada de Scripting é representada
# pelo módulo pyplot. Debaixo da tampa, pyplot usaa objetos no nível do módulo
# para rastrear o estado dos dados, desenhar os gráficos etc.
# Quando importado, pyplot seleciona ou o backend padrão para o sistema ou o que
# foi configurado; por exemplo, pela função matplotlib.use().
# Então chama a função setup() que:
#   - cria um função fabricadora de gerenciadores de imagens, que quando chamada irá
#       criar um novo gerenciador de imagens apropriado para o backend em uso;
#   - prepara a função de desenho que deveria ser usada pelo backend selecionado;
#   - identifica a função chamável que integra com a função mainloop do backend;
#   - fornece o módulo para o backend selecionado.
# A interface pyplot simplifica interações com os empacotadores internos ao
# fornecer métodos como plot(), pie(), bar(), title(), savefig(), draw() e figure() etc.
# A maioria dos exemplo do próximo capítulo usarão funções fornecidas pelo moódulo pyplot
# para criar os gráficos requisitados, escondendo os detalhes de nivel mais baixo.
