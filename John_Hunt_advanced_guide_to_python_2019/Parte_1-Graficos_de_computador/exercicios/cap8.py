# Neste exercício você vai criar sua aplicação GUI simples.
# A aplicação deveria gerar a exibição de uma UI simples.

import wx


class MainApp(wx.App):
    def OnInit(self):
        """Inicializa o aplicativo GUI principal"""
        frame = wx.Frame(parent=None, title="Simples Olá Mundo")
        frame.Show()
        # Indica se o processamento deveria continuar ou não
        return True
