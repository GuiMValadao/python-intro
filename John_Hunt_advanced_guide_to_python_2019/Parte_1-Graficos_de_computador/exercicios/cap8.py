# Neste exercício você vai criar sua aplicação GUI simples.
# A aplicação deveria gerar a exibição de uma UI simples.

import wx


class QuadroAniversario(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="App Feliz Aniversário", size=(300, 220))

        grid = wx.GridSizer(5, 1, 0, 0)
        backgroundpanel = wx.Panel(self, size=(300, 250))

        # Campo para digitar o nome
        self.painel_nome = wx.Panel(backgroundpanel)
        rotulo_nome = wx.StaticText(self.painel_nome, label="Nome:", pos=[10, 10])
        entrada_nome = wx.TextCtrl(self.painel_nome, size=(150, 20), pos=[55, 10])
        self.painel_nome.SetSize(15, 15, 200, 30)

        # Campo para digitar a idade
        self.painel_idade = wx.Panel(backgroundpanel)
        rotulo_idade = wx.StaticText(self.painel_idade, label="Idade:", pos=[10, 0])
        entrada_idade = wx.TextCtrl(self.painel_idade, size=(150, 20), pos=[55, 0])
        self.painel_idade.SetSize(15, 45, 200, 30)

        # Botões e mensagem
        self.painel_botoes = wx.Panel(backgroundpanel)
        botao_enter = wx.Button(self.painel_botoes, label="Enter", pos=(10, 0))

        mensagem = wx.StaticText(self.painel_botoes, label="Bem-vindo!", pos=(10, 30))

        botao_aniversario = wx.Button(
            self.painel_botoes, label="Aniversário", pos=(10, 60)
        )
        self.painel_botoes.SetSize(15, 75, 200, 90)
        # Coloca os items em uma grade com 1 coluna
        grid.AddMany(
            (
                self.painel_nome,
                self.painel_idade,
                self.painel_botoes,
            )
        )
        # Define a cor de fundo
        backgroundpanel.SetBackgroundColour(wx.Colour(25, 155, 25))
        # Coloca os objetos no painel
        backgroundpanel.SetSizer(grid)


class MainApp(wx.App):
    def OnInit(self):
        """Inicializa o aplicativo GUI principal"""
        frame = QuadroAniversario()
        frame.Show()
        return True


app = MainApp()
app.MainLoop()
