# Capítulo 11 - Introdução a programação de jogos

# A programação de jogos é realizada por desenvolvedores/programadores que
# implementam a lógica que comanda um jogo.
# Historicamente, desenvolvedores de jogos faziam tudo: escreviam o
# código, desenhavam os sprites e ícones, cuidavam da jogabilidade(gameplay),
# lidavam cim sons e música, geravam quaisquer animações necessárias, etc.
# Entretanto, com o crescimento da indústria de jogos, as companhias criaram
# papeis específicos incluindo animadores de Gráficos de Computador (CG),
# artistas, desenvolvedores de jogos, desenvolvedores do motor de jogo
# (game engine), desenvolvedor da física dos jogos etc.
# Aqueles envolvidos com o desenvolvimento do código podem desenvolver
# um motor de física, um motor de jogo, o jogo em si, etc. Esses desenvolvedores
# focam em diferentes aspectos de um jogo. Por exemplo, um desenvolvedor
# do motor do jogo foca em criar a estrutura (framework) dentro da qual o
# jogo executará. Por sua vez, um desenvolvedor do motor da física foca em
# implementar a matemática por trás da física do mundo dos jogos simulados
# (como o efeito da gravidade em personagens e componentes dentro do mundo).
# Em muitos casos, também existem desenvolvedores trabalhando no motor de
# IA para um jogo. Esses desenvolvedores focarão em fornecer instalações que
# permitem que o jogo ou personagens no jogo operem inteligentemente.
# Aqueles desenvolvimento a jogabilidade em si usarão esses motores e
# estruturas para criar o resultado final geral. São eles que dão vida ao
# jogo e o tornam uma experiência divertida(e jogável).
# -----------------------------------------------
# Estruturas e bibliotecas de jogos
# Existem várias estruturas e bibliotecas disponíveis que permitem-lhe
# criar qualquer coisa de jogos simples até rpgs complexos com mundos
# infinitos. Um exemplo é a estrutura Unity que pode ser usada com a
# linguagem de programação C#. Outra estrutura é a Unreal Engine usada
# com a linguagem C++.
# Python também é usada para o desenvolvimento de jogos com vários jogos
# bem conhecidos dependendo da linguagem de uma forma ou otra, com alguns exemplos
# sendo Battlefield 2, Civilisation IV, Overwatch.
# Python também é integrada como um motor de script dentro de ferramentas
# como Autodesk's Maya que é um conjunto de ferramentas de animação usada
# frequentemente em jogos.
# -------------------------------------------------
# Desenvolvimento de jogos em Python
# As estruturas/bibliotecas disponíveis para o desenvolvimento de jogos
# em Python incluem:
#   * Arcade: Biblioteca em Python para criar videogames em estilo 2D
#   * pyglet: biblioteca de janelamento e multimídia que também pode ser
#       usada para desenvolvimento de jogos
#   * Cocos2d: é uma estrutura para construir jogos 2D que é construída
#       sobre o pyglet.
#   * pygame: é, provavelmente, a biblioteca mais usada para criar jogos dentro
#       do mundo Python. Também existem muitas extensões disponíveis para
#       o pygame que ajudam a criar uma ampla gama de tipos de jogos diferentes.
# Outras bibliotecas de interesse para desenvolvedores de jogos incluem:
#   * PyODE: Conexão de código aberto do Python para o Open Dynamics Engine,
#       que é um motor da física de código aberto.
#   * pymunk: É uma biblioteca fácil de usar de física 2D que pode ser usada
#       sempre que precisa de física 2d de corpos rígidos com Python. é muito
#       útil quando precisa da física 2D em seu jogo, demo ou outra aplicação.
#       É construída sobre a biblioteca de física 2D Chipmunk.
#   * pyBox2D: biblioteca de física 2D para jogos e simulações simples. É
#       baseada na biblioteca Box2D escrita em C++. Suporta vários tipos de formas
#       (círculo, polígono, segmentos finos de linhas) assim como diversos
#       tipos de juntas(joint types) (revolute, prismatic, wheel).
#   * Blender: é um software de código aberto de gráficos de computador 3D
#       usado para criar filmes animados, efeitos visuais, arte, modelos 3D,
#       aplicações 3D interativas e video games. Os recursos do Blender incluem
#       modelagem 3D, texturização, edição de gráficos raster, rigging e skinning etc.
#       Python pode ser usada como uma ferramenta de script para criação,
#       prototipagem, lógica do jogo e mais.
#   * Quake Army Knife: é um ambiente para desenvolver mapas 3D para jogos
#       baseados no motor Quake. É escrito em Delphi e Python.
# -----------------------------------------------
# Usando pygame
# Nos próximos dois capítulos exploraremos o cerne da biblioteca pygame e
# como ela pode ser usada para desenvolver jogos de computador interativos.
# O próximo capítulo explora o pygame em si e as instalações que ele fornece.
# O capítulo na sequência desenvolve um jogo interativo simples no qual o
# usuário move uma espaçonave evitando meteoros que caem verticalmente na tela.
#
