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
        self.rotulo_nome = wx.StaticText(self.painel_nome, label="Nome:", pos=[10, 10])
        self.entrada_nome = wx.TextCtrl(self.painel_nome, size=(150, 20), pos=[55, 10])
        self.painel_nome.SetSize(15, 15, 200, 30)

        # Campo para digitar a idade
        self.painel_idade = wx.Panel(backgroundpanel)
        self.rotulo_idade = wx.StaticText(
            self.painel_idade, label="Idade:", pos=[10, 0]
        )
        self.entrada_idade = wx.TextCtrl(self.painel_idade, size=(150, 20), pos=[55, 0])
        self.painel_idade.SetSize(15, 45, 200, 30)

        # Botões e mensagem
        self.painel_botoes = wx.Panel(backgroundpanel)
        botao_enter = wx.Button(self.painel_botoes, label="Enter", pos=(10, 0))
        botao_enter.Bind(wx.EVT_BUTTON, self.set_nome)
        self.mensagem = wx.StaticText(
            self.painel_botoes, label="Bem-vindo!", pos=(10, 30)
        )

        botao_aniversario = wx.Button(
            self.painel_botoes, label="Aniversário", pos=(10, 60)
        )
        botao_aniversario.Bind(wx.EVT_BUTTON, self.exibir_mensagem)
        self.painel_botoes.SetSize(15, 75, 300, 90)
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

    def set_nome(self, event):
        # Define o nome
        self.nome = self.entrada_nome.GetLineText(0)
        self.mensagem.SetLabelText(f"Bem vindo, {self.nome}!")

    def checar_idade(self):
        # Checa se a idade é um número inteiro, se não abre uma caixa de diálogo para o erro
        try:
            self.idade = self.entrada_idade.GetLineText(0)
            int(self.idade)
            self.idade = int(self.entrada_idade.GetLineText(0))
            return True
        except ValueError:
            dialog = wx.MessageDialog(
                None,
                message="Valor para idade não é um número",
                caption="Erro",
                style=wx.OK,
            )
            dialog.ShowModal()
            return False

    def exibir_mensagem(self, event):
        # Se a idade fornecida é um número inteiro, exibe a mensagem de aniversário.
        if self.checar_idade():
            feliz_aniversario = wx.MessageDialog(
                None,
                message=f"Feliz aniversário {self.nome}, agora você tem {self.idade + 1} anos!",
                caption="Aniversário",
                style=wx.OK,
            )
            feliz_aniversario.ShowModal()


class MainApp(wx.App):
    def OnInit(self):
        """Inicializa o aplicativo GUI principal"""
        frame = QuadroAniversario()
        frame.Show()
        return True


app = MainApp()
app.MainLoop()
