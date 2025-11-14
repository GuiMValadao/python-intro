# Capítulo 9, Exercício 2
# O objetivo deste exercício é implementar um jogo da velha simples.
# O jogo deveria permitir que dois usuários joguem interativamente usando
# o mesmo mouse. O primeiro usuário jogará como o jogador 'X' e o segundo
# como o jogador '0'.
# Quando cada usuário seleciona um botão, você pode definir o rótulo para o
# botão como o símbolo dele. Voce precisará checar após cada jogada para
# verificar se alguém ganhou(ou se deu empate). Ainda precisará da representação
# do tabuleiro para poder determinar quem, se alguém, ganhou. Também pode acrescentar
# diálogos para pegar o nome dos jogadores e notificar quem ganhou.

import wx


class QuadroJogo(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Jogo da Velha", size=(300, 350))

        grid = wx.GridSizer(3, 3, 0, 0)
        self.painel_fundo = wx.Panel(self, size=(300, 350))
        jogador = ["X", "0"]
        x, y = 100, 100
        self.quadro = {}

        for posicao in range(9):
            self.quadro[posicao] = wx.Button(self.painel_fundo, size=(x, y))
            grid.Add(self.quadro[posicao])
            self.quadro[posicao].Bind(wx.EVT_LEFT_DOWN, self.anotar_jogada)
        self.mapear_tabuleiro = {}
        for item in range(9):
            local = self.quadro[item]
            self.mapear_tabuleiro[local] = item

        self.painel_fundo.SetSizer(grid)

    def tabuleiro():
        pass

    def anotar_jogada(self, event):
        botao = event.GetButton()
        print(botao)
        return self.quadro

    def obter_nomes():
        pass

    def checar_vencedor():
        pass

    def loop_jogo():
        pass


class MainApp(wx.App):
    def OnInit(self):
        """Inicializa o aplicativo GUI principal"""
        frame = QuadroJogo()
        frame.Show()
        return True


app = MainApp()
app.MainLoop()
