__author__ = 'Ricardo'

import pygame
from ifes.cih import *
from ifes.cgt import AplGerenciarJogador
from ifes.cgd import Error

from ifes.cci import CtrlTelaMenu
from ifes.cih import Singleton
class CtrlTelaJogo(Singleton.Singleton):
    def __init__(self):
        self.tela = TelaJogo.TelaJogo()
        self.controle = CtrlTelaMenu.CtrlTelaMenu()

    def exibe_tela(self):
        while True:
            self.tela.capturar_eventos()
            self.controle.imprime_menu(self.tela)

        return


