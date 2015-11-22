__author__ = 'Ricardo'

from ifes.cih import TelaMenu
from ifes.cci import *

from ifes.util import Singleton

from ifes.util.EnumOpcoes import OpcoesMenu

class CtrlTelaMenu(Singleton.Singleton):

    def __init__(self):
        self.tela_menu = TelaMenu.TelaMenu()
        self.ctrl_ranking = CtrlTelaRanking.CtrlTelaRanking()
        self.ctrl_cadastro = CtrlTelaCadastro.CtrlTelaCadastro()
        self.ctrl_jogo = CtrlTelaCenario.CtrlTelaCenario()
        self.ctrl_login = CtrlTelaLogin.CtrlTelaLogin()
        self.opcao = OpcoesMenu.menu
        self.pessoa = None

    def imprime_menu(self, game):

        if self.opcao == OpcoesMenu.menu:
            game.update_clock(10)
            self.opcao = self.tela_menu.mostrar_menu(game)

        elif self.opcao == OpcoesMenu.login:
            self.opcao = self.ctrl_login.mostrar_login(game)

        elif self.opcao == OpcoesMenu.cadastro:
            game.update_clock(10)
            self.opcao = self.ctrl_cadastro.mostrar_cadastro(game)

        elif self.opcao == OpcoesMenu.ranking:
            game.update_clock(10)
            self.opcao = self.ctrl_ranking.mostrar_ranking(game)

        elif self.opcao == OpcoesMenu.creditos:
            game.update_clock(10)

        elif self.opcao == OpcoesMenu.sair:
            game.sair()
