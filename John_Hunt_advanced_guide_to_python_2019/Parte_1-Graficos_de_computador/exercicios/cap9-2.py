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

        self.grid = wx.GridSizer(3, 3, 0, 0)
        self.painel_fundo = wx.Panel(self, size=(300, 350))
        self.quadro = []
        self.jogada = 0
        self.painel_fundo.SetSizer(self.grid)
        self.tabuleiro()
        self.nome_jogador1, self.nome_jogador2 = self.obter_nomes()

    def tabuleiro(self):
        x, y = 100, 100
        for posicao in range(9):
            self.quadro.append(wx.Button(self.painel_fundo, size=(x, y)))
            self.grid.Add(self.quadro[posicao])
            self.quadro[posicao].Bind(
                wx.EVT_BUTTON, self.anotar_jogada, self.quadro[posicao]
            )

    def anotar_jogada(self, event):
        botao_clicado = event.GetEventObject()  # Obtém o botão que foi clicado
        rotulo_atual = botao_clicado.GetLabel()  # Obtém o rótulo atual

        if self.jogada % 2 == 0:

            if rotulo_atual == "":
                botao_clicado.SetLabel("X")
        else:
            if rotulo_atual == "":
                botao_clicado.SetLabel("0")
        self.jogada += 1
        if self.jogo_terminou() or self.jogada == 9:
            app.ExitMainLoop()

    def obter_nomes(self):
        nome_jogador1 = wx.TextEntryDialog(
            None,
            message="Digite o nome do jogador 1.",
            caption="Escolha os nomes",
            value="Jogador 1",
        )
        nome_jogador1.ShowModal()
        nome_jogador2 = wx.TextEntryDialog(
            None,
            message="Digite o nome do jogador 2.",
            caption="Escolha os nomes",
            value="Jogador 2",
        )
        nome_jogador2.ShowModal()
        return nome_jogador1.GetValue(), nome_jogador2.GetValue()

    def jogo_terminou(self):
        def checar_vencedor():
            if self.jogada % 2 == 1:
                jogador_vencedor = wx.MessageDialog(
                    None,
                    message=f"Parabéns, {self.nome_jogador1} venceu!",
                    caption="Vencedor",
                    style=wx.OK,
                )
            else:
                jogador_vencedor = wx.MessageDialog(
                    None,
                    message=f"Parabéns, {self.nome_jogador2} venceu!",
                    caption="Vencedor",
                    style=wx.OK,
                )

            jogador_vencedor.ShowModal()
            return True

        if (
            (
                self.quadro[0].GetLabel() == self.quadro[1].GetLabel()
                and self.quadro[1].GetLabel() == self.quadro[2].GetLabel()
                and self.quadro[0].GetLabel() != ""
            )
            or (
                self.quadro[3].GetLabel() == self.quadro[4].GetLabel()
                and self.quadro[4].GetLabel() == self.quadro[5].GetLabel()
                and self.quadro[3].GetLabel() != ""
            )
            or (
                self.quadro[6].GetLabel() == self.quadro[7].GetLabel()
                and self.quadro[7].GetLabel() == self.quadro[8].GetLabel()
                and self.quadro[6].GetLabel() != ""
            )
            or (
                self.quadro[0].GetLabel() == self.quadro[3].GetLabel()
                and self.quadro[3].GetLabel() == self.quadro[6].GetLabel()
                and self.quadro[0].GetLabel() != ""
            )
            or (
                self.quadro[1].GetLabel() == self.quadro[4].GetLabel()
                and self.quadro[4].GetLabel() == self.quadro[7].GetLabel()
                and self.quadro[1].GetLabel() != ""
            )
            or (
                self.quadro[2].GetLabel() == self.quadro[5].GetLabel()
                and self.quadro[5].GetLabel() == self.quadro[8].GetLabel()
                and self.quadro[2].GetLabel() != ""
            )
            or (
                self.quadro[0].GetLabel() == self.quadro[4].GetLabel()
                and self.quadro[4].GetLabel() == self.quadro[8].GetLabel()
                and self.quadro[0].GetLabel() != ""
            )
            or (
                self.quadro[2].GetLabel() == self.quadro[4].GetLabel()
                and self.quadro[4].GetLabel() == self.quadro[6].GetLabel()
                and self.quadro[2].GetLabel() != ""
            )
        ):
            return checar_vencedor()

        if self.jogada == 9:
            empate = wx.MessageDialog(
                None,
                message=f"Deu velha!",
                caption="Empate",
                style=wx.OK,
            )
            empate.ShowModal()
            return True

        return False


class MainApp(wx.App):
    def OnInit(self):
        """Inicializa o aplicativo GUI principal"""
        frame = QuadroJogo()
        frame.Show()
        return True


app = MainApp()
app.MainLoop()
