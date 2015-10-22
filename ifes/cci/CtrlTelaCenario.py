__author__ = 'Ricardo'
from ifes.cih import TelaCenario, TelaFim
from ifes.util import Singleton


class CtrlTelaCenario(Singleton.Singleton):
    def __init__(self):
        self.tela_cenario = TelaCenario.TelaCenario()
        self.tela_fim = TelaFim.TelaFim()
        self.opcao = 1
        return

    def mostrar_cenario(self, game):
        game.update_clock(30)
        if self.opcao == 1:
            self.opcao = self.tela_cenario.mostrar_fase(game)

        elif self.opcao == 2:
            self.opcao = self.tela_cenario.mostrar_fim(game)
            if (self.opcao == 0):
                self.opcao = 1
                return 0
        #print(self.opcao)
        return 1
