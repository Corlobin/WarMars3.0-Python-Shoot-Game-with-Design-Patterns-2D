__author__ = 'Ricardo'
from ifes.cih import TelaCenario
from ifes.cih import Singleton
class CtrlTelaCenario(Singleton.Singleton):
    def __init__(self):
        self.tela = TelaCenario.TelaCenario()
        return

    def mostrar_cenario(self, game):
        game.update_clock(30)
        self.tela.mostrar_fase(game)
