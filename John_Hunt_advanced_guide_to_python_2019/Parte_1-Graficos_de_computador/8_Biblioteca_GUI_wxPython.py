# Capítulo 8 - A biblioteca GUI wxPython
# A biblioteca wxPython é uma biblioteca GUI multiplataforma para Python.
# Ela permite que programadores desenvolvam interfaces de usuário altamente
# gráficas para seus programas usando conceitos comuns como barras de menu,
# botões, campos, paineis e quadros.
# Em wxPython, todos os elementos de uma GUI são contidas dentro de janelas
# de alto nível como wx.Frame ou wx.Dialog. Estas janelas contem componentes
# gráficos conhecidos como dispositivos(widgets) ou controles. Estes dispositivos
# podem ser agrupados junto em Paineis (Panels)(que podem ou não ter uma
# representação visível).
# Assim, em wxPython poderíamos construir um GUI de:
#   * Quadros(Frames) que fornecem a estrutura básica para uma janela: bordas,
#       um rótulo e alguma funcionalidade básica (como redimensionamento).
#   * Diálogos que são como quadros mas fornecem menos controles de borda.
#   * Dispositivos/Controles que são objetos gráficos mostrados em um quadro.
#       Algumas outras linguagens chamam-nos de componentes UI(interface do usuário).
#       Exemplos de dispositivos são botões, caixas de seleção, listas de
#       seleção, rótulos e campos de textos.
#   * Recipientes(Containers) são componentes que são feitos por um ou mais
#       componentes(ou recipientes). Todos os componentes dentro de um recipiente
#       (como um painel) podem ser tratados como uma única entidade.
# Assim, uma GUI é construída hierarquicamente de um conjunto de dispositivos,
# recipientes e um ou mais Quadros (ou, no caso de diálogo de pop-up, Diálogos).
# Isto é ilustrado no quadro 'GUI_hierarquia.png' para uma janela contendo diversos
# paineis e dispositivos.
# Janelas como Quadros e Diálogos tem uma hierarquia de componentes que é usada
# (entre outras coisas) para determinar como e quando elementos da janela são
# desenhadas e redesenhadas. A hierarquia de componentes é enraizada com
# o quadro, dentro do qual componentes e recipientes podem ser adicionados.
# -------------------------------------------------------
# Módulos de wxPython
# A biblioteca wxPython é composta por diversos módulos diferentes. Estes módulos
# fornecem recursos diferentes desde o módulo central wx até os módulos
# orientados a html wx.html e wx.html2. Eles incluem:
#   * wx que armazena os dispositivos e classes centrais na biblioteca wx.
#   * wx.adv que fornece dispositivos e classes menos comumente usados ou mais avançados.
#   * wx.grid contem dispositivos e classes que suportam a exibição e edição de dados tabulares.
#   * wx.richtext consiste em dispositivos e classes usadas para mostrar múltiplos estilos de textos e imagens.
#   * wx.html é composto de dispositivos e classes de suporte para um renderizador html genérico.
#   * wx.html2 fornece mais dispositivos e classes para um renderizador nativo do html, com suporte a CSS e javascript.
# ----------------------------------------------
# Janelas como objetos
# Em wxPython, Quadros e Diálogos, assim como seus conteúdos, são instâncias
# de classes apropriadas(Como Frame, Dialog, Panel, Button ou Static Text).
# Assim, quando você cria uma janela, você cria um objeto que sabe como exibir si
# próprio na tela do computador. Você precisa dizê-lo o que exibir e e então
# dizê-lo para mostrar seu conteúdo ao usuário.
# Deve-se ter os seguintes pontos em mente durante a leitura deste capítulo:
#   * Você cria uma janela instanciando um objeto Quadro(Frame) ou Diálogo(Dialog).
#   * Você define o que a janela exibe criando um dispositivo que tem um
#       componente pai apropriado. Isto adiciona o dispositivo ao recipiente,
#       como um tipo de painel ou quadro.
#   * Você pode enviar mensagens à janela para mudar seu estado, realizar uma
#       operação e exibir um objeto gráfico.
#   * A janela, ou componentes dentro da janela, podem enviar mensagens a outros
#       objetos em resposta a ações do usuário(ou programa).
#   * Tudo que é mostrado por uma janela é uma instância de uma classe e é,
#       potencialmente, sujeito a todos os items acima.
#   * wx.App cuida do loop de evento principal da aplicação GUI.
# ------------------------------------------------
# Um exemplo simples
# Um exemplo de criação de uma janela muito simples usando wxPython é dado abaixo.
# Este programa cria uma janela de alto nível (wx.Frame) e lhe dá um título.
# Também cria um rótulo(objeto wx.StaticText) a ser exibido dentro do quadro.
#############################################
# import wx

# # Cria o Objeto Aplicativo
# app = wx.App()
# # Agora cria um Quadro (representando a Janela)
# frame = wx.Frame(parent=None, title="Simples Olá Mundo")
# # Adiciona um texto de rótulo a ele
# text = wx.StaticText(parent=frame, label="Olá Python")
# # Exibe a janela (quadro)
# frame.Show()
# # Inicia o loop de evento
# app.MainLoop()
##############################################
# O programa também cria uma nova instância do objeto Aplicativo chamado wx.App()
# Todo programa wxPython GUI precisa tem um Objeto Aplicativo. É o equivalente
# da função main() em muitos aplicativos não-GUI pois executará o aplicativo
# GUI para você. Também fornece instalações padrão para definir operações de
# inicializar(startup) e desligar(shutdowm) e pode ser 'subclassed' para criar
# comportamento customizado.
# A classe wx.StaticText é usada para criar um único(ou múltiplos) rótulo de linha (label).
# Neste caso, o rótulo exibe a string 'Olá Python'. O objeto StaticText é construído
# com referência ao recipiente pai(parent). Isto é, o recipiente dentro do qual o texto
# será exibido. Neste caso, StaticText está sendo exibido diretamente de dentro
# do Quadro e, assim, o objeto quadro é o obejto recipiente pai. Em contraste,
# o Quadro que é uma janela de nível máximo(top) não tem um recipiente pai.
# Note, também, que o quadro deve ser mostrado para que o usuário o veja.
# Isto ocorre pois poderia haver múltiplas janelas diferentes que precisam
# ser mostradas (ou escondidas) em diferentes situações para um aplicativo.
# Por fim, o programa inicia o loop 'main event' do aplicativo; dentro deste
# loop, o programa escuta por qualquer entrada do usuário (como pedir que a
# janela seja fechada).
# ----------------------------------
# A classe wx.App
# A classe wx.App representa o aplicativo e é usada para:
#   * iniciar o sistema wx.Python e inicializar  o toolkit GUI;
#   * definir e pegar propriedades de alcance do aplicativo;
#   * implementar a mensagem principal ou loop de evento do sistema de janelamento
#       nativo, e enviar eventos para instâncias de janelas.
# Todo aplicativo wxPython deve ter uma instância única de wx.App. A criação
# de todos os objetos da UI deveriam ser atrasadas para depois da criação do
# objeto wx.App para garantir que a plataforma GUI e wxWidgets foram
# inicializados completamente.
# É comum subclassear a classe wx.App e sobrescrever métodos como
# OnPreInit e OnExit para criar comportamento customizado. Isto garante que
# o comportamento exigido é executado em momentos apropriados. Os métodos
# que podem ser sobrescritos para este propósito são:
#   * OnPreInit: pode ser sobrescrito para definir comportamento que deve
#       ser executado quando o objeto do aplicativo é criado, mas antes do
#       método OnInit ser chamado.
#   * OnInit: É esperado que crie a janela principal do aplicativo, mostrar a janela etc.
#   * OnRun: É o método usado para iniciar a execução do programa principal.
#   * OnExit: Pode ser sobrescrito para fornecer comportamento que deveria ser
#       chamado logo antes do aplicativo fechar.
# Como um exemplo, se quisermos definir um aplicativo GUI de modo que o
# quadro principal é inicializado e mostrado após o wx.App ter sido instanciado
# então o modo mais seguro é sobrescrever o método OnInit() da classe wx.App
# com uma classe apropriada. O método deveria, então, retornar True ou False;
# onde True é usado para indicar que o processamento do aplicativo deveria
# continuar e False indica que o aplicativo deveria terminar imediatamente(
# geralmente como resultado de algum problema inerperado).
# Um exemplo de uma subclasse do wx.App é:
##############################################
# import wx


# class MainApp(wx.App):
#     def OnInit(self):
#         """Inicializa o aplicativo GUI principal"""
#         frame = wx.Frame(parent=None, title="Simples Olá Mundo")
#         frame.Show()
#         # Indica se o processamento deveria continuar ou não
#         return True

# # Esta classe pode agora ser instanciada e o MainLoop iniciado, por exemplo:
# app = MainApp()
# app.MainLoop()
##############################################
# Também é possível sobrescrever OnExit() para limpar qualquer coisa inicializada
# no método OnInit().
# -----------------------------------------------------
# Classes de Janelas
# As classes recipiente da janela ou dispositivo que são comumente usadas
# dentro de um aplicativo wxPython são:
#   * wx.Dialog: É uma janela de nível topo usada para popups onde o usuário
#       tem habilidade limitada para interagir com a janela. Em muitos casos,
#       o usuário pode apenas entrar algum dado e/ou aceitar ou recusar uma opção.
#   * wx.Frame: Um Frame pe uma janela de nível topo cujo tamanho e posição
#       podem ser definidos e podem(normalmente) ser controlado pelo usuário.
#   * wx.Panel: É um recipiente(não é janela de nível topo) no qual controles/
#       dispositivos podem ser colocados. Isto é comumente usado em conjunção com
#       um Dialor ou Frame para gerenciar a posição de dispositivos dentro da GUI.
# A hierarquia de herança para essas classes é:
# wx.Object       wx.Trackable
#      ^                ^
#      |                |
#       ----------------
#         wx.EvtHandler
#               ^
#               |
#         --------------------
#         |                   |
# --------------          ----------
# wx.NonOwnedWindow       wx.Panel
#         ^
#         |
# ----------------
# wx.TopLevelWindow
#         ^
#         |
# ---------------------
#     |                |
# ---------        ----------
# wx.Dialog        wx.Frame

# Como um exemplo de utilização de um Frame e um Panel, o seguinte aplicativo
# cria dois Paineis e exibe-os dentro de um Frame de nivel topo. A cor de
# fundo do Frame é o padrão cinza; enquanto a cor de fundo para o primeiro
# painel é azul e para o segundo painel é vermelho.

# #########################################
# import wx


# class SampleFrame(wx.Frame):
#     def __init__(self):
#         super().__init__(parent=None, title="App de amostra", size=(300, 300))
#         # Define a posição do primeiro painel como 1, 1 e tamanho (padrão
#         # de 300 por 100) com um fundo azul
#         self.panel1 = wx.Panel(self)
#         button1 = wx.Button(parent=self.panel1, label="OK", pos=[150, 70])
#         caixa_texto = wx.TextCtrl(self.panel1, value="Digite algo aqui", pos=[0, 30])
#         self.panel1.SetSize(300, 100)
#         self.panel1.SetBackgroundColour(wx.Colour(0, 0, 255))

#         # Define o segundo painel na posição 1, 110 e de tamanho 300 por 100
#         # com um fundo vermelho
#         self.panel2 = wx.Panel(self)
#         self.panel2.SetSize(1, 110, 300, 100)
#         self.panel2.SetBackgroundColour(wx.Colour(255, 0, 0))


# class MainApp(wx.App):
#     def OnInit(self):
#         frame = SampleFrame()
#         frame.Show()
#         return True


# app = MainApp()
# app.MainLoop()
#########################################
# SampleFrame é uma subclasse de wx.Frame; portanto, herda toda a funcionalidade
# de um Top Level Frame (janela). Dentro do método __init__() dA SampleFrame
# o __init__() da superclasse é chamado. Isto é usado para definir o tamanho
# do Frame e dar-lhe um título.
# Quando o Panel é criado, é necessário especificar a janela (ou, neste caso,
# Frame) dentro do qual será mostrado. Isto é um padrão comum em wxPython.
# -----------------------------------------------------------
# Classes Dispositivo/Controle
# Existem muitos dispositivos/controles disponíveis aos desenvolvedores, com
# os mais comumente usados sendo:
#   * wx.Button/wx.ToggleButton/wx.RadioButton: São dispositivos que fornecem
#       comportamento similar a botões dentro de uma GUI.
#   * wx.TextCtrl: Permite que texto seja exibido e editado. Pode ser uma única
#       linha ou múltiplas linhas dependendo da configuração.
#   * wx.StaticText: Usado para exibir uma ou mais linhas de texto apenas em
#       modo leitura. Em diversas bibliotecas, este dispositivo é chamada rótulo (label).
#   * wx.StaticLine: Uma linha usada em diálogos para separar grupos de dispositivos.
#       A linha pode ser vertical ou horizontal.
#   * wx.ListBox: Este dispositivo é usado para permitir que um usuário selecione
#       uma opção de uma lista de opções.
#   * wx.MenuBar/wx.Menu/wx.MenuItem: Os componentes que podem ser usados para
#       construir um conjunto de menus para uma interface de Usuário.
#   * wx.ToolBar: Este dispositivo é usado para exibir uma barra de botões e/ou
#       outros dispositivos geralmente colocados abaixo da barra de menu em um wx.Frame.
# Sempre que um dispositivo é criado, é necessário fornecer a classe de janela
# recipiente que o guardará, como um Frame ou Panel, por exemplo:
# enter_button = ex.Button(panel, label='Enter')
# ----------------------------------------------------------
# Diálogos
# A classe genérica wx.Dialog pode ser usada para construir qualquer diálogo
# personalizado que você requira. Pode ser usado para criar diálogos modais(modal)
# e não-modais(modeless).
#   * Um diálogo modal bloqueia o fluxo do programa e entrada do usuário em outras
#       janelas até ser resolvido.
#   * Um diálogo não-modal se comporta mais como um quadro, pois o fluxo do programa
#       continua, e entrada do usuário em outras janelas ainda é possível.
#   * A classe wx.Dialog fornece duas versões do método show() para suportar
#       diálogos modais e não-modais. O método ShowModal() é usado para exibir
#       o primeiro, e Show() para exibir o segundo.
# Assim como a classe genérica wx.Dialog, a biblioteca wxPython fornece diversos
# diálogos pre-construídos para situações comuns. Eles incluem:
#   * wx.ColourDialog: Para gerar um diálogo de escolha de cores.
#   * wx.DirDialog: diálogo para escolha de pasta/diretório.
#   * wx.FileDialog: diálogo para escolha de arquivo.
#   * wx.FontDialog: diálogo para escolha de fonte.
#   * wx.MessageDialog: esta classe pode ser usada para gerar uma mensagem de
#       linha única ou multi-linhas ou diálogo e informação. Permite opções
#       Sim, Não e Cancelar. Pode ser usada para mensagens genéricas ou de erro.
#   * wx.MultiChoiceDialog: Pode ser usada para exibir uma lista de strings
#       e permite o usuário selecionar um ou mais valores para ela.
#   * wx.PasswordEntryDialog: Representa um diálogo que permite que um usuário
#       digite uma senha de uma linha.
#   * wx.ProgressDialog: Se suportado pela plataforma GUI, esta classe fornecerá
#       o diálogo de progresso nativo da plataforma, se não usará wx.GenericProgressDialog
#       puramente do Python. Este exibe uma mensagem curta e uma barra de progresso.
#   * ex.TextEntryDialog: Esta classe fornece um diálogo que pede uma string de texto
#       de uma linha do usuário.
# A maioria dos diálogos que retornam um valor seguem o mesmo padrão. Este padrão
# retorna um valor do método ShowModel() que indica se o usuário selecionou
# OK ou CANCEL (usando o valor de retorno wx.ID_OK ou wx.ID_CANCEL). O valor
# selecionado/entrado pode, então, ser obtido de um método get apropriado
# como GetColourData() para ColourDialog ou GetPath() para DirDialog.
# ----------------------------------------------
# Arranjando dispositivos dentro de um recipiente
# Dispositivos podem ser colocados dentro de uma janela usando coordenadas
# específicas(como 10 pixeis para baixo e 5 pixeis lateralmente). Entretanto,
# isto pode ser um problema se você estiver considerando aplicações multiplataforma,
# pois um botão é renderizado de maneiras diferentes em um Mac, Windows ou Linux.
# Isto significa que diferente quantidades de espaçamento devem ser definidas
# em diferentes plataformas. Além disso, as fontes usadas para as caixas de texto
# e rótulos diferem entre diferentes plataformas, também exigindo diferenças na
# organização dos dispositivos.
# Para superar isto, wxPython fornece 'Sizers'. Eles funcionam com um recipiente
# como um Frame ou Panel para determinar como os dispositivos contidos devem
# ser dispostos. Os dispositivos também são adicionados a um Sizer que é, então,
# definido em um recipiente como um Panel.
# Portanto, um Sizer é um objeto que funciona com um recipiente e a plataforma
# de janelamento do hospedeiro para determinar o melhor modo de exibir os objetos
# na janela. O desenvolvedor não precisa se preocupar sobre o que acontece se um
# usuário redimensionar uma janela ou se o programa é executado em uma plataforma
# diferente.
# Além disso, um Sizer pode ser aninhado dentro de outro Sizer para criar
# exibições complexas. Existem diversos Sizers, incluindo:
#   * wx.BoxSizer: Pode ser usado para colocar vários dispositivos em uma linha
#       ou coluna dependendo da orientação. Quando o BoxSizer é criado, a
#       orientação pode ser especificada usando wx.VERTICAL ou wx.HORIZONTAL.
#   * wx.GridSizer: Arruma dispositivos em uma grade bidimensional. Cada célula
#       dentro da grade tem o mesmo tamanho. Quando o objeto GridSizer é criado,
#       é possível especificar o número de linhas e colunas que a grade tem.
#       Também é possível especificar o espaçamento entre as células tanto
#       horizontalmente quanto verticalmente.
#   * wx.FlexGridSizer: Este Sizer é uma versão um pouco mais flexível do
#       GridSizer. Nesta versão, nem todas as colunas e linhas precisam ter o
#       mesmo tamanho(apesar de todas as células na mesma coluna terem mesma
#       largura e todas as células em uma mesma linha a mesma altura).
#   * wx.GridBagSizer: É o Sizer mais flexível. Permite que dispositivos sejam
#       posicionados relativo à grade e também permite dispositivos ocupem
#       múltiplas linhas e/ou colunas.
# Para usar um Sizer, ele deve, primeiro, ser instanciado. Quando os dispositivos
# são criados, deveriam ser acrescentados ao sizer e então o sizer acrescentado
# ao recipiente.
# Por exemplo, o seguinte código usa um GridSizer com um Panel para arrumar quatro
# dispositivos compostos de dois botões, um rótulo StaticText e um campo de
# entrada TextCtrl:
####################################
# # Cria o painel:
# import wx

# app = wx.App()  # Essa linha não está colocada no livro.
# panel = wx.Frame(
#     parent=None, title="Painel de exemplo"
# )  # No livro, é usado wx.Panel, mas não funcionou, portanto troquei para Frame

# # Cria o sizer para usar 4 linhas e 1 coluna, com espaçamento 5 em torno de cada célula
# grid = wx.GridSizer(4, 1, 5, 5)

# # Cria os dispositivos
# text = wx.TextCtrl(panel, size=(150, -1))
# enter_button = wx.Button(panel, label="Enter")
# label = wx.StaticText(panel, label="Bem vindo!")
# message_button = wx.Button(panel, label="Mostrar mensagem")

# # Coloca os dispositivos no sizer de grade:
# grid.AddMany((text, enter_button, label, message_button))

# # Coloca o sizer no painel:
# panel.SetSizer(grid)
# panel.Show()  # Não estava no livro. Mostra a janela.
# app.MainLoop()
####################################
# Desenhando gráficos
# Em capítulos anteriores, vimos a API Turtle Graphics para gerar gráficos
# vetores e raster com Python. A biblioteca wxPython fornece seus próprios
# recursos para gerar exibições gráficas multiplataformas usando linhas,
# quadrados, círculos, texto, etc. Isto é fornecido pelo Device Context (DC).
# Um Device Context é um objeto no qual gráficos e texto podem ser desenhados.
# Seu objetivo é permitir que diferentes dispositivos de saída todos tenham um
# API de gráficos em comum (também conhecido como GDI ou Graphics Device Interface).
# Device Contexts específicos podem ser instanciados dependendo em se um programa
# deve usar uma janela em uma tela de computador ou em algum outro meio de saída(como uma impressora).
# Existem vários tipos de Device Context disponíveis como wx.WindowDC, wx.PaintDC e
# wx.ClientDC:
#   * O wx.WindowDC é usado se queremos pintar na tela inteira (apenas Windows).
#       Isto inclui decorações de janela.
#   * O wx.ClientDC é usado para desenhar na área do cliente de uma janela. A área do
#       cliente é a área de uma janela sem suas decorações (título e borda).
#   * O wx.PaintDC também é usado para desenhar na área do cliente mas é projetado para
#       para suportar o mecanismo para cuidar do evento de pintura da atualização da janela.
# Note que wx.PaintSC deveria ser usado apenas de um manipulador wx.PaintEvent
# enquanto wx.ClientDC não deve nunca ser usado de um manipulador wx.PaintEvent.
# Qualquer seja o DC usado, todos suportam um conjunto similar de métodos que
# são usados para gerar gráficos, como:
#   * DrawCircle(x, y, radius): Desenha um circulo cmo o centro e raio informados.
#   * DrawElipse(x, y, width, height): Desenha uma elipse contida no retângulo
#       especificado seja com o canto superior esquerdo e tamanho dados ou diretamente.
#   * DrawPoint(x, y): Desenha um ponto usando a cor atual da caneta.
#   * DrawRectangle(x, y, width, height): Desenha um retângulo com a coordenada
#       do canto e tamanho informados.
#   * DrawText(text, x, y): Desenha uma string de texto no ponto especificado,
#       usando a cor da fonte de texto atual, e as cores de frente e fundo do texto
#       atuais.
#   * DrawLine(pt1, pt2)/DrawLine(x1, y1, x2, y2): Este método desenha uma linha
#       do primeiro ponto para o segundo.
# Também é importante entender quando o DC é atualizado/redesenhado. Por exemplo,
# se você redimensionar uma janela, maximizá-la, minimizá-la, movê-la ou modificar
# seus conteúdos a janela é redesenhada. Isto gera um evento, um PaintEvent.
# Você pode prender um método ao PaintEvent(using wx.EVT_PAINT) que pode ser chamado
# toda vez que a janela é atualizada.
# Este método pode ser usado para desenhar quaisquer os conteúdos da janela deveriam
# ser. Se você não redesenhar os conteúdos do DC em tal método, então o que havia
# sido desenhado antes será exibido quando a janela é atualizada.
# O seguinte programa simples ilustra o uso de algum dos métodos Draw listados
# acima e como um método pode ser preso ao evento de pintura de forma que a
# exibição é atualizada apropriadamente quando usando um device context:
##########################################3
# import wx


# class DrawingFrame(wx.Frame):
#     def __init__(self, titulo):
#         super().__init__(None, title=titulo, size=(300, 200))
#         self.Bind(wx.EVT_PAINT, self.on_paint)

#     def on_paint(self, event):
#         """define o device context(DC) para pintura"""
#         dc = wx.PaintDC(self)
#         dc.DrawLine(10, 10, 60, 20)
#         dc.DrawRectangle(20, 40, 40, 20)
#         dc.DrawText("Olá Mundo!", 30, 70)
#         dc.DrawCircle(130, 40, radius=15)


# class GraphicApp(wx.App):
#     def OnInit(self):
#         """Inicializa a exibição da GUI"""
#         frame = DrawingFrame(titulo="PyDesenho")
#         frame.Show()
#         return True


# app = GraphicApp()
# app.MainLoop()
##############################################3
