# Capítulo 2 - Introdução a gráficos de computador
# O termo 'Gráficos de computador' remete a um tempo em que a maioria dos
# computadores eram puramente textuais em termos de sua entrada e saída e
# muito poucos computadores podiam gerar exibições gráficas, sem mencionar
# lidar com entradas em exibições(displays) deste tipo. Entretanto, em
# termos deste livro tomamos o termo 'Gráficos de computador' para incluir
# a criação de Interfaces Gráficas de Usuários (GUIs), gráficos e quadros
# como gráficos de barra ou gráficos lineares de dados, gráficos em jogos
# de computador, assim como a geração de cenas ou imagens 2D e 3D. A arte
# gerada por computador também é incluída.
# -----------------------------------------------------
# Todo sistema de software interativo tem uma interface computador-humano,
# seja uma única linha de texto ou uma exibição gráfica avançada. É o veículo
# usado por desenvolvedores para obter informação do usuário e, por sua vez,
# todo usuário tem que encontrar alguma forma de interface computacional
# para realizar qualquer operação computacional.
# Historicamente, sistemas computacionais não tinham a Interface Gráfica
# do Usuário e raramente geravam uma visualização gráfica.
# -------------------------------------------------------
# A Era dos Gráficos de Computador
# Exibições de gráficos de computador e interfaces gráficas interativas
# se tornaram um meio comum de interação computador-humano durante os anos
# 80. Tais interfaces podem evitar que o usuário precise aprender comandos
# complexos. O grande uso de interfaces gráficas de alta qualidade levou
# muitos usuários a esperar tais interfaces de qualquer software que usam.
# De fato, esses sistemas pavimentaram o caminho para o tipo de interface
# hoje onipresente em PC's, Macs, Linux, tablets e smartphones, etc. Esta
# interface do usuário é baseada no paradigma WIMP(Winows, Icons, Menus,
# Pointers) que é, agora, o tipo predominante de interface gráfica de
# usuário em uso hoje.
# A principal vantagem de qualquer sistema baseado em janelas, e particularmente
# de um ambiente WIMP, é que requer apenas uma pequena quantidade de treino
# do usuário. Não há necessidade de se aprender comandos complexos, como a
# maioria das operações são disponíveis ou como ícones, ou como operações
# em ícones, ações do usuário ou de menu de opções, e são fáceis de usar.
# Este tipo de interface pode ser aumentada fornecendo a manipulação direta
# de gráficos. Estes são gráficos que podem ser 'pegos' e manipulados pelo
# usuário, usando um mouse, para realizar alguma operação ou ação. Ícones são
# uma versão simples disto, a 'abertura' de um ícone causa ou a aplicação
# associada ser executada ou a janela associada ser mostrada.
# -----------------------------------------------------
# Gráficos interativos e não-interativos
# Gráficos de computador podem ser, de modo amplo, subdivididos em duas categorias:
#   - Gráficos de computador não-interativos
#   - Gráficos de computados interativos
# Em Gráficos não-interativos (também chamados Gráficos de Computador Passivos)
# uma imagem é gerada por um computador tipucamente em um tela de computador;
# esta imagem pode ser vista pelo usuário (mas eles não podem interagir com
# a imagem). Exemplos de gráficos não-interativos apresentados mais tarde no livro
# incluem Arte Gerada Computacionalmente onde uma imagem é ferada usando a
# biblioteca do Python Turtle Graphics. Tal imagem pode ser vista pelo usuário
# mas não modificada. Outro exemplo poderia ser um gráfico de barras básico
# gerado usando MatPloLib que apresenta algum conjunto de dados.
# Gráficos interativos, em contraste, envolvem o usuário interagindo com a
# imagem mostrada na tela de algum modo, poderia ser para modificar os dados
# sendo mostrados ou mudar o modo em que a imagem está sendo renderizada etc.
# É tipificada por Interfaces Gráficas de Usuários (GUIs) nas quais um usuário
# interage com menus, botões, campos de entrada, deslizadores, barras de
# deslize etc. Entretanto, outras exibições visuais também podem ser interativas.
# Por exemplo, um deslizador poderia ser usado com um gráfico do MatPlotLib.
# Outro exemplo é representado por todos os jogos de computados que são
# inerentemente interativos e a maioria, se não todos, atualizado sua exibição
# visual em resposta a alguma entrada do usuário.
# --------------------------------------------------------------
# Pixels
# Um conceito chave para todos os sitemas de gráficos de computador é o pixel.
# Pixel era, originalmente, uma palavra formada por combinar e encurtar as
# palavras figura(picture, pix) e elemento. Um pixel é uma célula em uma tela
# de computador. Cada célula apresenta um ponto na tela. O tamanho deste ponto
# ou célula e o número de células disponíveis varia dependendo no tipo, tamanho
# e resolução da tela. Por exemplo, era comum para os computadores Windows
# iniciais terem um display com resolução 640 x 480. Isto se relaciona ao
# número de pixells em termos de largura e altura, ou seja, 640 pixels de lado
# a lado e 480 linhas de pixels de cima a baixo. Em contraste, telas de TV
# 4K atuais tem 4096 por 2160 pixels.
# O tamanho e número de pixels disponíveis afetam a qualidade de uma imagem
# como apresentada ao usuário, com resoluções menores fazendo a imagem parecer
# 'quadrada', ou menos definida e resoluções maiores mais afiada/clara.
# Cada pixel pode ser referenciado por sua localização na tela de exibição.
# Preenchendo os pixels de uma tela com diferentes cores várias imagens/exibições
# podem ser criadas.Uma sequência de pixels pode formar uma linha, um círculo
# ou qualquer tipo de formas diferentes. Entretanto, como a grade de pixels é
# baseada em pontos individuais, uma linha diagonal ou um círculo pode precisar
# usar multiplos pixels que, quando aproximados, podem ter bordas serrilhadas.
# Cada pixel pode ter uma cor e transparência associados com ele. O alcance de
# cores disponível depende no sistema de exibição sendo usado. Por exemplo,
# telas monocromáticas apenas permitem preto e branco, enqaunto uma tela de
# escala de cinza apenas permite diversos tons de cinza serem mostrados. Em
# sistemas modernos é geralmente possível representar uma ampla gama de cores
# usando os códigos de cores tradicionais RGB (Red, Green, Blue). Nesta codificação,
# vermelho sólido é representado por um código como [255, 0, 0], verde sólido
# como [0, 255, 0] e azul sólido [0, 0, 255]. Baseado nesta ideia, vários tons
# podem ser representados pela combinação desses códigos como Laranja que
# poderia ser representado por [255, 150, 50].
# Além disso, é possível aplicar uma transparência para um pixel. Isto é usado
# para indicar quão sólida a cor de preenchimento deveria ser. Uma biblioteca
# para aplicar a transparência em Python é a wxPython, onde a transparência
# é referida como o alpha opaque value. Pode ter valores na faixa 0-255 onde
# 0 é completamente transparente e 255 é completamente sólido.
# ---------------------------------------------------
# Bitmap(Mapa de bits) versus Vector Graphics(vetores gráficos)
# Há dois modos de gerar uma imagem/display nos pixels da tela. Uma abordagem
# é conhecida como gráficos mapeados por bits (ou raster) e a outra é
# conhecida como vetores gráficos. Na abosdagem de mapeação por bits cada
# pixel é mapeado aos valores a serem mostrados para criar a imagem. Na abordagem
# de vetores gráficos formas geométricas são descritas(como linhas e pontos) e
# estas são, então, renderizadas em um display. Gráficos raster são mais simples
# mas vetores gráficos fornecem muito mais flexibilidade e escalabilidade.
# -------------------------------------------------------
# Buffering
# Um problema para a exibição de gráficos interativos é a habilidade de mudar a
# exibiçãotão suavemente e precisamente quanto possível. Se uma exibição é
# irregular ou parece pular de uma imagem para outra, então os usuários
# acharão aquilo desconfortável. É, portanto, comum desenhar a próxima exibição
# em alguma em alguma estrutura na memória, comumente referida como buffer.
# Este buffer pode, então, ser renderizado na exibição quando a imagem inteira
# tenha sido criada. Por exemplo, Turtle Graphics permite que o usuário defina
# quantas mudanças deveriam ser feitas à exibição antes dela ser renderizada na
# tela. Isto pode acelerar significantemente a performance de uma aplicação gráfica.
# Em alguns casos, sistemas vão usar dois buffers; comumente referido como
# buffering duplo. Nesta abordagem, um buffer está sendo renderizado na tela
# enquanto o outro buffer está sendo atualizado. Isto pode significantemente
# melhorar o desempenho geral do sistema como computadores modernos podem realizar
# cálculos e gerar dados muito mais rápido do que pode ser tipicamente visto
# na tela.
# ------------------------------------------------------------
# Python e gráficos computacionais
# No resto dessa seção vamos lidar com a geração de imagens computacionais usando
# a biblioteca do Python Turtle Graphics. Também vamos discutir usar esta
# biblioteca para criar Arte Gerada por Compitador. Em seguida, vamos explorar
# a biblioteca MatPlotLib usada para gerar gráficos e gráficos de dados como
# gráficos de barras, gráficos de espalhamento, de linha, mapas de calor, etc.
# Vamos então explorar a utilização de bibliotecas Python para criar GUIs usando
# campos, menus, tabelas etc.
