# Capítulo 12 - Construindo jogos com pygame
# pygame é uma biblioteca Python multiplatforma, gratuita e de código aberto
# projetada para tornar a construção de aplocativos multimídia como jogos fácil.
# O desenvolvemtno de pygame iniciou em Outubro de 2000 com a versão 1.0
# lançada seis meses depois. A versão discutida no livro é 1.9.6. Se
# usar uma versão posterior, verifique se as alterações tem algum impacto
# nos exemplos do livro.
# Esta biblioteca é construída sobre a biblioteca SDL (Simple Directmedia Layer).
# A SDL é uma biblioteca de desenvolvimento multiplataforma projetada para
# fornecer acesso a hardware de audio, teclados, mouse, joystick e gráficos
# por OpenGL e Direct3D. Para promover portabilidade, pygame também oferece
# suporte a uma variedade de backends adicionais incluindo WinDIB, Linux,
# Frame Buffer etc.
# SDL oficialmente suporta Windows, MacOS, Linux, iOS e Android (com outras
# plataformas sendo suportadas não-oficialmente). SDL em si é escrita em C e
# pygame fornece uma embalagem em torno da SDL. Entretanto, pygame acrescenta
# funcionalidades não encontradas em SDL para tornar a criação de gráficos
# ou video games mais fácil. Estas funções incluem matemática vetorial,
# detecção de colisões, gerenciamento de cenas gráficas de sprite 2D, suporte
# a MIDI, camera, manipulação de matrizes de pixel, transformações, filtragem,
# suporte a fontes de tipo livre (freetype font) e desenho.
# --------------------------------------------------------
# A superfície de exibição
# A Superfície de Exibição (Display Surface, ou display) é a parte mais
# importante de um jogo pygame. É a janela de exibição principal do seu jogo
# e pode ter qualquer tamanho, entretanto você pode apenas ter uma Superfície
# de exibição.
# De muitas formas, a Superfície de exibição é como um pedaço de papel em branco
# na qual você pode desenhar. A superfície em si é feita de pixels que podem ser
# enumerados de 0,0 no canto superior esquerdo com os locais dos pixels sendo
# indexados nos eixos x e y.
# Uma superfície pode ser usada para desenhar linhas, formas (como retângulos,
# quadrados, círculos e elipses), exibir imagens, manipular pixels individuais etc.
# Linhas são desenhadas de uma posição de pixel até outra (por exemplo, de
# 0,0 até 9,0).
# A Superfície de Exibição é criada pela função pygame.desplay.set_mode().
# Esta função pega uma tupla que pode ser usada para especificar o tamanho
# da tela de exibição a ser retornada. Por exemplo:
# display_surface = pygame.display.set_mode((400,300))
# Isto criará uma tela(janela) de 400 x 300 pixels.
# Após criada, pode-se preencher a Superfície de Exibição com uma cor de fundo
# apropriada(a padrão é preta), mas se quiser uma cor diferente ou quiser
# limpar tudo que foi desenhado anteriormente na superfície, pode usa o
# método fill():
# WHITE = (255,255,255)
# display_surface.fill(WHITE)
# O método pega uma tupla usada para definir uma cor em termos de RGB. Para ajudar
# na performance, quaisquer mudanças feita à superfície de exibição acontecem
# por baixo dos panos, não sendo renderizada na tela atual até chamar os
# métodos update() ou flip(). Por exemplo:
# pygame.display.update()
# pygame.display.flip()
# O método update() redesenha a tela com todas as alterações feitas no fundo.
# Tem um parâmetro opcional que permite especificar apenas uma parte da tela
# para ser atualizada(definido usando um Rect, que representa uma área retangular
# na tela). O método flip() sempre atualiza a tela inteira(fazendo o mesmo que
# update() sem parametros).
# Outro método, que não é um método específico de uma superfície de exibição,
# mas é usado frequentemente quando a superfície de exibição é criada, fornece uma
# legenda ou título para a janela de maior nível:
# pygame.display.set_caption('Hello World')
# ------------------------------------------
# Eventos
# Assim como sistemas de interface gráfica de usuários descritas em capítulos
# anteriores tem um loop de evento que permite ao programador perceber o que o
# usuário está fazendo (como escolher um item de menu, clicar um botão ou
# entrar um dado, etc) pygame tem um loop de evento que permite ao jogo
# perceber o que o usuário está fazendo. Por exemplo, o usuário pode apertar
# a tecla esquerda ou direita. Isto é representado por um evento.
# -------------------------------------------
# Tipos de eventos
# Cada evento que ocorre tem associada uma informação como o tipo daquele
# evento. Por exemplo:
#   * Apertar uma tecla resulta em um evento do tipo KEYDOWN, enquanto soltar
#       a tecla resultará em um evento do tipo KEYUP.
#   * Selecionar o botão para fechar a janela irá gerar um evento do tipo QUIT
#   * Usar o mouse pode gerar eventos MOUSEMOTION assim como MOUSEBUTTONDOWN
#       e MOUSEBUTTONUP.
#   * Usar um Joystick pode gerar vários tipos diferentes de eventso
#       incluindo JOYAXISMOTION, JOYBALLMOTION, JOYBUTTONDOWN e JOYBUTTONUP.
# ----------------------------------------------
# Informação do evento
# Cada tipo de objeto evento fornece informação associada com aquele evento.
# Por exemplo, um objeto de evento orientado a tecla(KET) fornecerá a tecla
# pressionada enquanto um objeto orientado a mouse fornecerá informação da
# posição do mouse, qual botão foi apertado etc. Se tentar acessar um atributo
# em um evento que não suporta aquele atributo, um erro será gerado.
# Em seguida, são listados alguns dos atributos disponíveis para diferentes
# tipos de eventos:
#   * KEYDOWN e KEYUP, o evento tem um atributo key e um atributo mod(indicando
#       se qualquer outras teclas modificadoras como Shift também foram apertadas).
#   * MOUSEBUTTONUP e MOUSEBUTTONDOWN tem um atributo pos que guarda uma tupla
#       indicando a posição do mouse  em termos das coordenadas x e y na superfície.
#       também tem um atributo button indicando qual botão do mouse foi apertado.
#   * MOUSEMOTION tem atributos pos, rel e buttons. pos é uma tupla indicando
#       a posição x e y do cursor do mouse. O atributo rel indica a quantidade
#       de movimento do mouse e buttons indica o estado dos botões do mouse.
# Como um exemplo, se quisermos checar por evento do tipo teclado e então checar
# que a tecla apertada foi a barra de espaço, podemos escrever:
# if event.type == pygame.KEYDOWN:
#   if event.key == pygame.K_SPACE:
#       print('space')
# Isto indica que se é um evento de aperto de tecla e a tecla apertada foi a
# barra de espaço, então exibe a string 'space'. Há várias constantes de teclado
# que são usadas para representar as teclas do teclado e pygame.K_SPACE usada
# acima é apenas uma delas. Todas as constantes de teclado são prefixadas com 'K_'
# seguido pela tecla ou o nome da tecla, por exemplo: K_TAB, K_SPACE, K_PLUS,
# K_0, K_1, K_AT, K_a, K_b, K_z, K_DELETE, K_DOWN, K_LEFT, K_RIGHT, K_LEFT etc.
# Outras constantes de teclado são fornecidas para modificadores de estados que
# podem ser combinados com as acima como KMOD_SHIFT, KMOD_CAPS, KMOD_CTRL e KMOD_ALT.
# ------------------------------------------------
# A fila de eventos
# Eventos são fornecidos a uma aplicação pygame pela fila de eventos. A Fila
# de Eventos é usada para coletar eventos assim que eles ocorrem. Por exemplo,
# assuma que um usuário clica com o mouse duas vezes e uma tecla duas vezes antes
# de um programa ter chance de processá-los; então haverão 4 eventos na fila.
# A aplicação pode, então, obter um iterável da fila de evento e processar
# pelos eventos na sequência. Enquanto o programa está processando estes eventos,
# outros eventos podem ocorrer e serão adicionados à fila. Quando o programa
# finalizou o processamento da coleção inicial de eventos, pode obter o próximo
# conjunto de eventos a serem processados.
# Uma grande vantagem desta abordagem é que nenhum evento é perdido; isto é,
# se o usuário clicar com o mouse duas vezes enquanto o programa está processando
# um conjunto anterior de eventos, isso será salvo e acrescentado à fila de eventos.
# Outra vantagem é que eventos serão apresentados ao programa na ordem em que
# ocorreram. A função pygame.event.get() lerá todos os eventos atualmente na
# fila de eventos(removendo-os da fila). O método retorna uma EventList que é
# uma lista iterável dos eventos lidos. Cada evento pode, então, ser processado
# na sequência. Por exemplo:
# for event in pygame.event.get():
#   if event.type == pygame.QUIT:
#       print('Recebido um evento de Saída')
#   elif event.type == pygame.MOUSEBUTTONDOWN:
#       print('Recebido um evento de Mouse')
#   elif event.type == pygame.KEYDOWN:
#       print('Recebido um evento do tipo Tecla pressionada')
# Nessa seção de código, uma EventList é obtida da fila de evento contendo
# o conjunto atual de eventos. O loop for, então, processa cada evento na
# sequência checando o tipo e exibindo uma mensagem apropriada.
# Você pode usar esta abordagem para ativar comportamentos apropriados como
# mover uma imagem na tela ou calcular a pontuação do jogador etc. Entretanto,
# tome cuidado que se este comportamento levar tempo demais pode fazer com que
# seja difícil jogar o jogo.
# -------------------------------------------
# Um primeiro aplicativo pygame
# Agora estamos em um ponto onde podemos juntar tudo que olhamos até aqui e
# criar um aplicativo pygame simples. É comum criar um programa no estilo
# hello world quando usando uma nova linguagem de programação ou usando uma
# nova estrutura(framework) de aplicativo etc. A intenção é que os elementos
# centrais da linguagem ou estrutura são explorados para poder gerar a forma
# mais básica de um aplicativo usando a linguagem ou framework. Portanto, vamos
# implementar o aplicativo mais básico possível com pygame.
# Vamos criar um aplicativo em que será exibida uma janela pygame com um
# título 'Hello world'. Então poderemos sair do jogo, apesar de, tecnicamente
# não ser um jogo, ainda possuirá a arquitetura básica de um aplicativo pygame.
# O jogo simples HelloWorld inicializará pygame e a exibição gráfica. Então
# terá um loop principal de jogo que continuará até o usuário escolher sair
# do aplicativo. Então desligará o aplicativo.
####################################
# import pygame


# def main():
#     print("Iniciando o jogo")

#     print("Inicializando pygame")
#     pygame.init()  # Exigido por toda aplicação pygame

#     print("Inicializando HelloWorldGame")
#     pygame.display.set_mode((200, 100))
#     pygame.display.set_caption("Hello World")

#     print("Atualizar exibição")
#     pygame.display.update()

#     print("Iniciando o loop principal do jogo")
#     running = True
#     while running:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 print("Recebido evento de saída:", event)
#                 running = False
#     print("Fim de jogo")
#     pygame.quit()


# if __name__ == "__main__":
#     main()

###################################################
# Há vários passos importantes destacados neste exemplo:
#   1. Import pygame: trocar por pygame-ce, mantido com atualizações mais frequentes?
#       Também é comum adicionar from pygame.locals import * para importar várias
#       constantes e funções para o espaço de nomes do programa.
#   2. Inicializar pygame: Quase todo módulo pygame precisa ser inicializado de algum
#       modo e o jeito mais simples de fazer isso é chamar pygame.init(). Isto fará
#       o necessário para preparar o ambiente pygame para uso. Se esquecer de chamar
#       esta função você geralmente obterá um erro como pygame.error:video system
#       not initialised. Se receber este tipo de erro cheque para garantir que chamou
#       pygame.init(). Note que você pode inicializar módulos pygame individuais
#       (por exemplo, pygame.font.init()) se necessário. Entretanto, pygame.init()
#       é a abordagem mais comumente usada para preparar o jogo.
#   3. Prepara a exibição: Após inicializar a estrutura pygame pode preparar a exibição.
#       No código acima, a exibição é preparada usando a função pygame.display.set_mode().
#       Esta função pega uma tupla especificando o tamanho da janela a ser criada. Note
#       que se tentar invocar esta função passando dois parâmetros em vez da tupla obterá
#       um erro. Esta função retorna a superfície de exibição ou tela/janela que pode ser usada
#       para exibir items dentro do jogo como ícones, mensagens, formas etc. Assim como nosso
#       exemplo é tão simples não tivemos de nos preocupar com salvar em uma variável.
#       Entretanto, qualquer coisa mais complexa que isto precisará fazer isso. Também
#       preparamos o título da janela, que é exibido na barra de título da janela.
#   4. Renderizar a exibição: Agora chamamos a função pygame.display.update(). Esta função
#       causa os detalhes atuais da exibição serem desenhados. No momento isto é uma tela
#       vazia. Entretanto, é comum em jogos realizar uma série de atualizações à exibição
#       no fundo e então, quando o programa está pronto para atualizar a exibição, chamá-lo.
#       Isto agrupa uma série de atualizações e causa com que a exibição seja atualizada.
#       Em uma exibição complexa, é possível indicar quais partes da exibição precisam
#       ser redesenhadas em vez da janela inteira. Isto é feito passando um parâmetro
#       à função update() para indicar o retângulo a ser redesenhado.
#   5. Loop principal para jogar: é comum ter um loop principal para jogar que dirige o
#       processamento das entradas do usuário, modifica o estado do jogo e atualiza a
#       exibição. Isto é representado acima pelo loop while running:. A variável local
#       running é inicializada como True. Isto significa que o loop while garante
#       que o jogo continua até o usuário escolher sair do jogo, ponto no qual a variável
#       running é trocada para False. Em vários casos, este loop chamará update() para atualizar
#       a tela.
#   6. Procurar eventos que conduzem o jogo.
#   7. Sair do pygame ao terminar: em pygame qualquer módulo que tem uma função init()
#       também tem uma equivalente quit() que pode ser usada para realizar quaisquer
#       operações de limpeza. Como é chamada init() no inicio do programa, deve-se chamar
#       pygame.quit() ao final.
# -----------------------------------------------
# Conceitos adicionais
# Há diversos recursos em pygame que vão além do que será cobrido no livro,
# alguns deles serão discutidos na sequência.
#   * Superfícies(Surfaces) são uma hierarquia: A Superfície de exibição de nivel
#       maior pode conter outras superfícies que podem ser usadas para desenhar
#       imagens ou texto. Por sua vez, recipientes como Paineis podem renderizar
#       superfícies para exibir imagens ou texto etc.
#   * Outros tipos de superfície: A superfície de exibição primária não é a única
#       superfície em pygame. Por exemplo, quando uma imagem, como um PNG ou JPEG,
#       é carregada em um jogo, então é renderizada em uma superfície. Esta superfície
#       pode, então, ser exibida dentro de outra como a Superfície de Exibição.
#       Isto significa que qualquer coisa que você pode fazer à Superfície de
#       Exibição pode ser feita com qualquer outra superfície, como desenhar nela,
#       colocar texto, colori-la, acrescentar um ícone etc.
#   * Fontes: O objeto pygame.font.Font é usado para criar uma fonte que pode ser
#       usada para renderizar texto na superfície. O método renderizador retorna
#       uma superfície com o texto renderizado nela que pode ser exibida dentro
#       de outra superfície como a Superfície de Exibição. Note que você não pode
#       escrever texto em uma superfície existente, sempre será necessário obter uma
#       superfície nova (usando render) e então acrescentá-la à superfície existente.
#       O texto pode apenas ser exibido em uma única linha e a superfície com o texto
#       terá as dimensões necessárias para renderizar o texto. Por exemplo:
# text_font = pygame.font.Font('freesansbold.ttf', 18)
# text_surface = text_font.render('Hello World', antialias=True, color=BLUE)
#       Isto cria um novo objeto Font usando a fonte especificada com o tamanho indicado
#       (neste caso, 18). Então renderizará a string 'Hello World' na nova superfície
#       usando a fonte e tamanho especificado na cor azul. Especificar que antialias é
#       True indica que gostaríamos de suavizar as bordas do texto na tela.
#   * Retângulos (ou Rects): A classe pygame.Rect é um objeto usado para representar
#       coordenadas retangulars. Um Rect pode ser criado de uma combinação das coordenadas
#       do canto superior esquerdo junto com uma altura e largura. Por flexibilidade,
#       muitas funções que esperam um objeto Rect também podem ser dadas uma lista
#       'tipo retangular', isto é, uma lista que contém informações necessárias para
#       criar um objeto Rect. Rects são muito úteis em um pygame Game pois podem ser
#       usados para definir as bordas de um objeto do jogo. Isto significa que podem
#       ser usados dentro do jogo para detectar se dois objetos colidiram. Isto é
#       particularmente fácil pois a classe Rect tem vários métodos de detecção de
#       colisão:
#           * pygame.Rect.contains(): testa se um retângulo está dentro de outro
#           * pygame.Rect.collidepoint(): testa se um ponto está dentro de um retângulo
#           * pygame.Rect.colliderect(): testa se dois retângulos se sobrepõe
#           * pygame.Rect.collidelist(): teste se um retângulo em uma lista interseciona
#           * pygame.Rect.collidelistall(): testa se todos os retângulos em uma lista intersecionam
#           * pygame.Rect.collidedict(): testa se um retângulo em um dicionário interseciona
#           * pygame.Rect.collidedictall(): testa se todos os retângulos em um dicionário intersecionam
#       A classe também fornece vários outros métodos de utilidade como move() que
#       move o retângulo e inflate() que pode aumentar ou diminuir o tamanho do
#       retângulo.
#   * Desenhar formas: o módulo pygame.draw tem várias funções que podem ser usadas
#       para desenhar linhas e formas em uma superfície, por exemplo:
# pygame.draw.rect(display_surface, BLUE, [x, y, WIDTH, HEIGHT])
#       Isto desenhará um retângulo preenchido com a cor azul (a padrão) na superfície.
#       O retângulo estará localizado no local indicado por x e y (na superfície).
#       Isto indica o canto superior esquerdo do retângulo. A largura e comprimento
#       indicam o tamanho. Note que essas dimensões são definidas dentro de uma lista
#       que é uma estrutura referida como sendo 'tipo retangular'. Se não quer
#       um retângulo preenchido, pode usar o parâmetro opcional de largura para
#       indicar a espessura da borda. outros métodos disponíveis incluem:
#           * pygame.draw.polygon(): desenha uma forma com qualquer número de lados
#           * pygame.draw.circle(): desenha um círculo em torno de um ponto
#           * pygame.draw.ellipse(): desenha uma forma redonda dentro de um retângulo
#           * pygame.draw.arc(): desenha uma seção parcial de uma elipse
#           * pygame.draw.line(): desenha um segmento de linha reta
#           * pygame.draw.lines(): desenha múltiplos segmentos de linha contínua
#           * pygame.draw.aaline(): desenha linhas finas com antialiasing
#           * pygame.draw.aalines(): desenha uma sequência conectadas de linhas com antialiasing.
#   * Imagens: o módulo pygame.image contém funções para carregar, slavar e transformar
#       imagens. Quando uma imagem é carregada em pygame, é representada por um
#       objeto Surface. Isto significa que é possível desenhar, manipular e processar
#       uma imagem exatamente da mesma forma que qualquer outra superfície, o que
#       permite um alto nível de flexibilidade. No mínimo, o módulo suporta apenas
#       carregar imagens BMP não comprimidas, mas geralmente também suporta JPEG, PNG,
#       GIF(não-animado), BMP, TIFF assim como outros formatos. Entretanto, apenas
#       suporta um conjunto limitado de formatos ao salvar imagens; sendo eles BMP,
#       TGA, PNG e JPEG. Uma imagem pode ser carregada de um arquivo usando:
# image_surface = pygame.image.load(filename).convert()
#       Isto carregará a imagem do arquivo especificado em uma superfície.
#       Uma coisa que você poderia se perguntar é sobre o uso do método convert() no
#       objeto retornado da função pygame.image.load(). Esta função retorna
#       uma superfície que é usada para exibir a imagem contida no arquivo. Chamamos
#       o método convert() nesta superfície, não para converter a imagem de um
#       formato de arquivo particular (como PnG ou JPEG), mas para converter o
#       formato pixelado usado pela superfície. Se o formato de pixels usado pela
#       superfície não é o mesmo que o formato de exibição, então precisará ser convertido
#       durante execução toda vez que a imagem é exibida na tela; isto pode ser
#       um processo consideravelmente demorado(e desnecessário). Portanto, fazemos isso
#       apenas uma vez quando a imagem é carregada, o que significa que não
#       deveria prejudicar a performance da execução e pode melhorar a performance
#       significativamente em alguns sistemas. Uma vez que tem-se uma superfície
#       contendo uma imagem, ela pode ser renderizada em outra superfície, como a
#       superfície de exibição usando o método Surface.blit(). Por exemplo:
# display_surface.blit(image_surface, (x, y))
#       Note que o argumento de posição é uma tupla especificando as coordenadas
#       x e y para exibir a imagem na superfície. Estritamente falando, o método
#       blit() desenha uma superfície (a superfície fonte) em outra na coordenada
#       de destino. Assim, a superfície alvo não precisa ser a superfície de exibição
#       de nível topo.
#   * Relógio: Um objeto Clock pode ser usado para rastrear tempo. Em particular,
#       pode ser usado para definir a taxa de quadros para o jogo. Isto é, o
#       número de quadros renderizados por segundo. Isto é feito usando o método
#       Clock.tick(). Este método deve ser chamado uma (e apenas uma) vez por quadro.
#       Se passar o argumento opcional framerate para a função tick(), então
#       pygame garantirá que a taxa de atualização do jogo é menor que as marcações
#       por segundo informadas. Isto pode ser usado para ajudar a limitar a velocidade
#       de execução de um jogo. Chamando clock.tick(30) uma vez por quadro, o programa
#       nunca executará em mais de 30 quadros por segundo.
# -----------------------------------------------------------
# Um aplicativo pygame mais interativo
# O próximo aplicativo adicionará resolução de eventos de mouse. Isto nos permitirá
# pegar a posição do mouse quando o usuário clicar na janela e desenhar uma pequena caixa
# azul naquele ponto. Se o usuário clicar o mouse múltiplas vezes múltiplas caixas
# serão desenhadas.
##########################################################
import pygame

FRAME_REFRESH_RATE = 30
COLOR = (0, 0, 255)
BACKGROUND = (255, 255, 255)
WIDTH = 10
HEIGHT = 10


def main():
    print("Inicializando pygame")
    pygame.init()

    print("Inicializando o Jogo de Caixas")
    display_surface = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Jogo de Caixas")
    print("Atualizar a exibição")
    pygame.display.update()
    print("Preparando o relógio")
    relogio = pygame.time.Clock()
    display_surface.fill(BACKGROUND)

    print("Iniciando o Loop de Jogo principal")
    executando = True
    while executando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Recebido evento de saída: ", event)
                executando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print("Recebido evento de mouse: ", event)
                x, y = event.pos
                pygame.draw.rect(display_surface, COLOR, [x, y, WIDTH, HEIGHT])
        pygame.display.update()
        relogio.tick(FRAME_REFRESH_RATE)
    print("Fim de jogo")
    pygame.quit()


if __name__ == "__main__":
    main()

##################################################
# Note que agora precisamos guardar a superfície de exibição em uma variável local para
# podermos usá-la para desenhar os retângulos. Também precisamos chamar pygame.display.update()
# toda vez que o loop while principal é executado para que os novos retângulos sejam
# exibidos. Também definimos a taxa de quadros a cada loop while. Isto deveria acontecer
# uma vez por quadro (mas apenas uma vez) e usar o objeto relógio inicializado no início
# do programa.
# ----------------------------------------------------------
# Abordagem alternativa para processar dispositivos de entrada
# Existem dois modos no qual entradas de um dispositivo como um mouse, joystick ou
# teclado podem ser processadas. Uma abordagem é o modelo baseado em eventos descrito
# acima. A outra é uma abordagem baseada em estado.
# Apesar da abordagem baseada em eventos ter várias vantagens, tem duas desvantagens:
#   * Cada evento representa uma única ação e ações contínuas não são explicitamente
#       representadas. Assim, se o usuário apertar tanto a tecla X quanto a Z, isto
#       gerará dois eventos e caberá ao programa determinar que elas foram apertadas ao
#       mesmo tempo.
#   * Também caberá ao programa determinar que o usuário ainda está apertando uma
#       tecla(notando que o evento KEYUP não ocorreu)
#   * Ambas são possíveis, mas podem ser suscetíveis a erros.
# Uma abordagem alternativa é usar a abordagem baseada em estado. Nesta abordagem
# o programa pode diretamente checar o estado de um dispositivo de entrada. Por exemplo,
# você pode usar pygame.key.get_pressed() que retornao estado de todas as teclas.
# Isto pode ser usado para determinar se uma tecla específica está sendo apertada nesse
# momento no tempo. Por exemplo, pygame.key.get_pressed()[pygame.K_SPACE] pode ser usado
# pra checar se a barra de espaço está sendo apertada. Entretanto, se o usuário
# aperta uma tecla e então a solta antes do programa checar o estado do teclado então
# aquela entrada será perdida.
# ----------------------------------------------------
# Módulos pygame
# Há diversos módulos fornecidos como parte do pygame assim como bibliotecas associadas.
# Alguns dos módulos principais são listados abaixo:
#   * pygame.display: É usado para controlar a janela ou tela de exibição. Fornece
#       instalações para inicializar e desligar o módulo de exibição. Pode ser usado
#       para inicializar uma janela ou tela. Também pode ser usado para causar uma janela
#       ou tela para atualizar.
#   * pygame.event: gerencia eventos e a fila de eventos. Por exemplo:
#       pygame.event,get() receve eventos da fila
#       pygame.event.poll() recebe um único evento da fila e
#       pygame.event.peek() testa para ver se há qualquer tipo de evento na fila
#   * pygame.draw: O módulo draw é usado para desenhar formas simples em uma superfície.
#       Por exemplo, fornece funções para desenhar um retângulo (pygame.draw.rect), um
#       polígono, um círculo, uma elipse, uma linha, etc.
#   * pygame.font: O módulo fonte é usado para criar e renderizar fontes TrueType
#       em um novo objeto superfície. A maioria dos recursos associados com fontes
#       são suportados pela classe pygame.font.FONT. Funções de módulo livre permitem
#       o módulo ser inicializado e desligado, além de funções para acessar fontes
#       como pygame.font.get_fonts() que fornece uma lista das fontes atualmente disponíveis.
#   * pygame.image: Este módulo permite imagens serem salvas e carregadas. Note que
#       as imagens são carregadas em um objeto superfície(não há classes images, ao contrário de outras estruturas para GUIs).
#   * pygame.joystick: O módulo joystick fornece o objeto Joystick e muitas funções
#       suporte. Elas podem ser usadas para interagir com joysticks, gamepads e trackballs.
#   * pygame.key: Este módulo fornece suporte para trabalhar com entradas do teclado.
#       Isto permite as teclas de entrada serem obtidas e teclas de modificadores(como
#       control e shift) serem identificadas. Também permite a abordagem de teclas repetidas
#       ser especificada.
#   * pygame.mouse: Este módulo fornece recursos para trabalhar com a entrada de mouse
#       como obter a posição atual do mouse, o estado dos botões do mouse assim como
#       a imagem a ser usada para o mouse.
#   * pygame.time: Este é o módulo pygame para gerenciar o tempo dentro de um jogo.
#       Fornece a classe pygame.time.Clock que pode ser usada para rastrear o tempo.
#
