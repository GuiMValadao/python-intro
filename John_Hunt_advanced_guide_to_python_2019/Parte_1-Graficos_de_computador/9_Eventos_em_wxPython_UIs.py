# Capítulo 9 - Eventos em Interfaces de Usuário do wxPython
# Eventos são uma parte integral de qualquer GUI; eles representam interações
# dos usuários com a interface, como cliques em um botão, digitar texto em
# um campo, selecionar uma opção de menu etc.
# O loop de evento principal espera por um evento; quando um ocorre, ele
# processa aquele evento (que geralmente resulta na chamada de uma função
# ou método) e então espera pelo próximo evento. Este loop é iniciado em
# wxPython pela chamada ao método  MainLoop() no objeto wx.App.
# Isso leva à pergunta: 'O que é um evento?'. Um objeto evento é um pedaço
# de informação representando alguma interação que ocorreu, tipicamente
# com a GUI(mas pode ser gerado por qualquer coisa). Um evento é processado
# por um 'Event Handler'(Resolvedor de Eventos). Ele é um método que é
# chamado quando o evento ocorre. O evento é passado ao resolvedor como
# um parâmetro. Um 'Event Binder' (Conector de Eventos) é usado para ligar
# um evento a um resolvedor de eventos.
# -----------------------------------------------
# Definições de eventos
# É útil sumarizar as definições em torno de eventos pois a terminologia
# usada pode ser confusa e muito similar:
#   * EVENTO representa informação de um framework subjacenta à GUI que
#       descreve algo que aconteceu e qualquer informação associada. O
#       dado específico disponível dependera no que ocorreu. Por exemplo, se
#       uma janela foi movida, então a informação associada será relativa à
#       nova localização da janela. Enquanto um CommandEvent gerado por uma
#       ação de seleção de um ListBox fornece o índice do intem selecionado.
#   * EVENT LOOP é o loop de processamento principal da GUI que espera por
#       um evento ocorrer. Quando um evento ocorre, o resolvedor associado
#       é chamado.
#   * EVENT HANDLERS são os métodos(ou funções) que são chamados quando um
#       evento ocorre.
#   * EVENT BINDERS associam um tipo de evento com um resolvedor de eventos.
#       Há diferentes conectores para diferentes tipos de eventos. Por exemplo,
#       O conector de evento associado com wx.MoveEvent é chamado wx.EVT_MOVE.
# A relação entre Evento, Resolvedor de Eventos e Conector de Eventos é
# ilustrada abaixo:
#   |EVENTO|-----|CONECTOR DE EVENTOS|---|RESOLVEDOR DE EVENTOS|
# -------------------------------------------------------------
#  |MoveEvent|---------|EVT_MOVE|---------|on_move(self, event)|
# Os três itens de cima ilustram os conceitos enquanto os três de baixo
# são exemplos concretos de ligar um Move_Event a um método on_move pelo
# conector EVT_MOVE.
# ---------------------------------------------------------------
# Tipos de eventos
# Há diversos tipos diferentes de eventos, incluindo:
#   * wx.CloseEvent: usado para indicar que um Frame ou Dialog foi fechado.
#       O conector deste evento é chamado wx.EVT_CLOSE.
#   * wx.CommandEvent: usado com dispositivos como botões, caixas de listas,
#       items de menus, botões de rádio, barras de deslizamento, deslizadores, etc.
#       Dependendo do tipo de dispositivo que gerou o evento, diferentes informações
#       podem ser fornecidas. Por exemplo, para um Button, um CommandEvent indica
#       que o botão foi clicado, enquanto para um ListBox indica que uma opção
#       foi selecionada, etc. Conectores de evento diferentes são usados para
#       diferentes situações. Por exemplo, para ligar um evento de comando
#       a um resolvedor de evento para um botão, o conector wx.EVT_BUTTON é usado;
#       para um ListBox, um conector wx.EVT_LISTBOX pode ser usado.
#   * wx.FocusEvent: Este evento é enviado quando o foco de uma janela muda
#       (perde ou ganha foco). Você pode detectar uma janela ganhando foco usando
#       o conector de evento wx.EVT_SET_FOCUS. O wx.EVT_KILL_FOCUS é usado
#       para conectar um resolvedor de evento que será chamado quando uma
#       janela perde foco.
#   * wx.KeyEvent: Contém informação relacionada a aperto ou soltura de teclas.
#   * wx.MaximizeEvent: É gerado quando uma janela de nível topo é maximizada.
#   * wx.MenuEvent: É usado para ações de menu como abertura ou fechamento do menu;
#       entretando deve-se notar que não é usado quando um item do menu é selecionado (MenuItems geram CommandEvents).
#   * wx.MouseEvent: Esta classe de evento contem informação sobre os eventos
#       gerados pelo mouse: inclui informação sobre qual botão do mouse foi
#       pressionado(e solto) e se o mouse realizou um clique duplo etc.
#   * wx.WindowCreateEvent: É enviado logo após a janela atual ser criada.
#   * wx.WindowDestroyedEvent é enviado o mais cedo possível durante o processo de destruição da janela.
# ------------------------------------------------
# Conectando um evento a um resolvedor
# Um evento é ligado e um Resolvedor de Evento usando o método Bind() de um
# objeto gerador de eventos (como um botão, campo, item de menu etc) por
# um Conector de Evento nomeado. por exemplo:
# button.Bind(wx.EVT_BUTTON, self.event_handler_method)
# --------------------------------------------
# Implementado resolução de eventos
# Há quatro passos envolvidos na implementação de resolução de eventos para
# um dispositivo ou janela, sendo eles:
#   1 - Identificar o evento de interesse
#   2 - Encontrar o nome correto do Conector de Evento
#   3 - Implementar um resolvedor de evento
#   4 - Ligar o Evento ao Resolvedor.
# Para ilustrar esse processo, usamos um exemplo simples. Vamos escrever uma
# aplicação simples para resolver um evento. Ela terá um Fram contendo um
# Panel. O Panel conterá um rótulo usando a classe StaticText.
# Definimos um resolvedor de evento chamado on_mouse_click() que moverá
# o rótulo StaticText para o local atual do mouse quando o botão esquerdo
# do mouse é pressionado. Isto significa que podemo mover o rótulo pela tela.
# Para fazer isso, precisamos determinar o dispositivo que será usado para
# gerar o evento. Neste caso, é o painel que contém o rótulo de texto. Feito
# isso, podemos olhar na classe Panel para ver quais Conectores de Evento ela suporta.
# A classe Panel define diretamente suporte apenas para NavigationKeyEvents.
# Isto não é o que procuramos; entretanto, a classe Panel extende a classe
# Window.
# A classe Window suporta diversos conectores de eventos, daqueles associados
# ao foco até aperto de teclas, assim como eventos de mouse. Entretanto,
# há diversos conectores para eventos de mouse. Eles permitem cliques com
# o botão esquero, direito, e do meio, segurar o botão apertado e mesmo
# o mouse entrar e sair da janela etc. O que procuramos é o conector
# wx.EVT_LEFT_DOWN; ele detecta o MouseEvent quando o botão esquerdo do
# mouse é apertado(também existe o wx.EVT_LEFT_UP, que pode ser usado
# para detectar um evento que ocorre quando o botão esquero é solto).
# Sabemos agora que precisamos conectar o resolvedor de eventos on_mouse_click()
# ao MouseEvent pelo conector wx.EVT_LEFT_DOWN, por exemplo:
# self.panel.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_click)
# Todos os métodos resolvedores de evento pegam dois parâmetros, self e o
# evento do mouse. Assim, a assinatura(signature) do método on_mouse_click() é:
# def on_mouse_click(self, mouse_event):
# O objeto de evento do mouse tem diversos métodos definidos que permitem que
# informação sobre o mouse seja obtida como o número de cliques do mouse
# (GetClickCount()), qual botão foi pressionado(GetButton()) e a posição
# atual do mouse dentro do dispositivo ou janela(GetPosition()). Podemos,
# portanto, usar este último método para obter o local atual do mouse e usar
# o método SetPosition(x, y) no objeto Static Text para definir sua posição.
# O resultado final é o programa abaixo:
###########################################3
# import wx


# class WelcomeFrame(wx.Frame):
#     """A Janela/Frame principal da aplicação"""

#     def __init__(self):
#         super().__init__(parent=None, title="Sample App", size=(300, 200))

#         # Coloca o painel dentro da janela e o texto dentro do painel
#         self.panel = wx.Panel(self)
#         self.text = wx.StaticText(self.panel, label="Hello")

#         # Conecta o método on_mouse_click ao Evento do Mouse pelo conector
#         # do clique com botão esquerdo
#         self.panel.Bind(wx.EVT_LEFT_DOWN, self.on_mouse_click)

#     def on_mouse_click(self, mouse_event):
#         """Quando o botão esquerdo é clicado, chama este método.
#         Ele obtém a posição atual do mouse e reposiciona o texto nesta posição"""

#         x, y = mouse_event.GetPosition()
#         print(x, y)
#         self.text.SetPosition(wx.Point(x, y))


# class MainApp(wx.App):
#     def OnInit(self):
#         """Inicializa a GUI da aplicação"""
#         frame = WelcomeFrame()
#         frame.Show()
#         return True


# app = MainApp()
# app.MainLoop()
##########################################
# Uma GUI wxPython interativa
# Um exemplo de uma aplicação GUI um pouco maior, que conecta muitas das
# ideias apresentadas neste capítulo, é dada abaixo. Nesta aplicação,
# temos um campo de entrada de texto (um wx.TextCtrl) que permite que o
# usuário coloque seu nome. Quando eles clicam em um botão Enter (wx.Button)
# o texto Bem-vindo (um wx.StaticText) é atualizado com seu nome. O botão
# 'Mostrar mensagem' é usado para exibir um wx.MessageDialog que também
# conterá seu nome.
###############################################
# import wx


# class HelloFrame(wx.Frame):
#     def __init__(self, title):
#         super().__init__(None, title=title, size=(300, 200))

#         self.name = "<unknown>"

#         vertical_box_sizer = wx.BoxSizer(wx.VERTICAL)
#         self.SetSizer(vertical_box_sizer)

#         panel = wx.Panel(self)
#         vertical_box_sizer.Add(panel, wx.ID_ANY, wx.EXPAND | wx.ALL, 20)

#         grid = wx.GridSizer(4, 1, 5, 5)

#         self.text = wx.TextCtrl(panel, size=(150, -1))
#         enter_button = wx.Button(panel, label=("Enter"))
#         enter_button.Bind(wx.EVT_BUTTON, self.set_name)
#         self.label = wx.StaticText(panel, label="Bem vindo", style=wx.ALIGN_LEFT)
#         message_button = wx.Button(panel, label="Mostrar mensagem")
#         message_button.Bind(wx.EVT_BUTTON, self.show_message)

#         grid.AddMany([self.text, enter_button, self.label, message_button])

#         panel.SetSizer(grid)
#         self.Centre()

#     def show_message(self, event):
#         dialog = wx.MessageDialog(
#             None, message="Bem vindo ao Python " + self.name, caption="Olá", style=wx.OK
#         )
#         dialog.ShowModal()

#     def set_name(self, event):
#         self.name = self.text.GetLineText(0)
#         self.label.SetLabelText("Bem vindo " + self.name)


# class MainApp(wx.App):
#     def OnInit(self):
#         frame = HelloFrame(title="App exemplo")
#         frame.Show()
#         return True

#     def OnExit(sef):
#         print("Tchau!")
#         return True


# app = MainApp()
# app.MainLoop()
###############################################
