__author__ = 'Ricardo'

from ifes.cih import *

from ifes.cci import CtrlTelaMenu
from ifes.util import Singleton


class CtrlTelaJogo(Singleton.Singleton):
    def __init__(self):
        self.tela = TelaJogo.TelaJogo()
        self.controle = CtrlTelaMenu.CtrlTelaMenu()

    def exibe_tela(self):
        while True:
            self.tela.capturar_eventos()
            self.controle.imprime_menu(self.tela)

        return


