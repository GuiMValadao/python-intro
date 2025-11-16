import wx


class Teste(wx.Frame):
    def __init__(self):
        super().__init__(parent=None, title="Jogo da Velha", size=(300, 350))
        self.painel_fundo = wx.Panel(self, size=(300, 350))
        x, y = 100, 100
        self.quadro = []
        for posicao in range(9):
            self.quadro.append(wx.Button(self.painel_fundo, size=(x, y)))
            #            self.grid.Add(self.quadro[posicao])
            #            self.quadro[posicao].Bind(
            #                wx.EVT_BUTTON, self.anotar_jogada, self.quadro[posicao]
            #            )
            if posicao == 2 or posicao == 5 or posicao == 6:
                self.quadro[posicao].SetLabel("X")
            else:
                self.quadro[posicao].SetLabel(str(posicao))

        if (
            (
                self.quadro[0].GetLabel() == self.quadro[1].GetLabel()
                and self.quadro[1].GetLabel() == self.quadro[2].GetLabel()
            )
            or (
                self.quadro[3].GetLabel() == self.quadro[4].GetLabel()
                and self.quadro[4].GetLabel() == self.quadro[5].GetLabel()
            )
            or (
                self.quadro[6].GetLabel() == self.quadro[7].GetLabel()
                and self.quadro[7].GetLabel() == self.quadro[8].GetLabel()
            )
            or (
                self.quadro[0].GetLabel() == self.quadro[3].GetLabel()
                and self.quadro[3].GetLabel() == self.quadro[6].GetLabel()
            )
            or (
                self.quadro[1].GetLabel() == self.quadro[4].GetLabel()
                and self.quadro[4].GetLabel() == self.quadro[7].GetLabel()
            )
            or (
                self.quadro[2].GetLabel() == self.quadro[5].GetLabel()
                and self.quadro[5].GetLabel() == self.quadro[8].GetLabel()
            )
            or (
                self.quadro[0].GetLabel() == self.quadro[5].GetLabel()
                and self.quadro[5].GetLabel() == self.quadro[8].GetLabel()
            )
            or (
                self.quadro[2].GetLabel() == self.quadro[5].GetLabel()
                and self.quadro[5].GetLabel() == self.quadro[6].GetLabel()
            )
        ):
            print("True")
        else:
            print("False")


class MainApp(wx.App):
    def OnInit(self):
        """Inicializa o aplicativo GUI principal"""
        frame = Teste()
        frame.Show()
        return True


app = MainApp()
app.MainLoop()
