__author__ = 'Ricardo'

from ifes.cih import TelaMenu
from ifes.cci import *

from ifes.cih import Singleton

class CtrlTelaMenu(Singleton.Singleton):

    def __init__(self):
        self.tela_menu = TelaMenu.TelaMenu()
        self.ctrl_ranking = CtrlTelaRanking.CtrlTelaRanking()
        self.ctrl_cadastro = CtrlTelaCadastro.CtrlTelaCadastro()
        self.ctrl_jogo = CtrlTelaCenario.CtrlTelaCenario()
        self.opcao = 0

    def imprime_menu(self, game):
        game.update_clock(10)
        if(self.opcao == 0):
            self.opcao = self.tela_menu.mostrar_menu(game)
            #print(self.opcao)

        elif self.opcao == 1:
            print("Iniciar")

        elif self.opcao == 2:
            self.opcao = self.ctrl_cadastro.mostrar_cadastro(game)
            #print(self.opcao)

        elif self.opcao == 3:
            print("Ranking")
            self.opcao = self.ctrl_ranking.mostrar_ranking(game)

        elif self.opcao == 4:
            print("Creditos")

        elif self.opcao == 5:
            game.sair()
