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
        self.ctrl_login = CtrlTelaLogin.CtrlTelaLogin()
        self.opcao = 0
        self.pessoa = None

    def imprime_menu(self, game):
        if(self.opcao == 0):
            game.update_clock(10)
            self.opcao = self.tela_menu.mostrar_menu(game)
            #print(self.opcao)

        elif self.opcao == 1:
            self.opcao = self.ctrl_login.mostrar_login(game)
            #print("Iniciar")

        elif self.opcao == 2:
            game.update_clock(10)
            self.opcao = self.ctrl_cadastro.mostrar_cadastro(game)
            #print(self.opcao)

        elif self.opcao == 3:
            game.update_clock(10)
            print("Ranking")
            self.opcao = self.ctrl_ranking.mostrar_ranking(game)

        elif self.opcao == 4:
            game.update_clock(10)
            print("Creditos")

        elif self.opcao == 5:
            game.sair()
