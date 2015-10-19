__author__ = 'Ricardo'

import time
from ifes.cih import TelaLogin
from ifes.cih import TelaCenario
from ifes.cci import CtrlTelaCenario
from ifes.cih import Singleton
from ifes.cgt import AplGerenciarJogador
from ifes.cgd import Error
class CtrlTelaLogin(Singleton.Singleton):

    def __init__(self):
        self.tela = TelaLogin.TelaLogin()
        self.telaJogando = TelaCenario.TelaCenario()
        self.ctrl_cenario = CtrlTelaCenario.CtrlTelaCenario()
        self.mostrandoCenario = False
        self.pessoa = None
        self.opcao = 1
        print("Invocando o metodo construtor mais de uma vez nao pode !!")

    def mostrar_login(self, game):
        if self.mostrandoCenario == False and self.pessoa == None:
            game.update_clock(10)
            self.pessoa, self.opcao = self.tela.mostrar_login(game)

        if self.pessoa != None and self.opcao == 1 and self.mostrandoCenario == False:
            try:
                print(self.pessoa)
                self.pessoa = AplGerenciarJogador.AplGerenciarJogador.logar_jogador(self.pessoa)
                print(self.pessoa)
                self.mostrandoCenario = True
                waiting = 0
                while waiting <= 200:
                    self.tela.update_error(game, waiting)
                    waiting += 1
                game.usuario = self.pessoa

                game.update_clock(30)

            except Error.Error as arg:
                print('Msg: ' + arg.msg)
                self.tela.exibe_mensagem(arg.msg)

        elif self.pessoa != None and self.mostrandoCenario == True:
            self.opcao = self.ctrl_cenario.mostrar_cenario(game)
            if(self.opcao == 0):
                self.mostrandoCenario = False

        elif self.pessoa != None and self.mostrandoCenario == False:
            self.mostrandoCenario = True

        return self.opcao

