__author__ = 'Ricardo'
import time
from ifes.cih import TelaLogin
from ifes.cih import TelaCenario
from ifes.cci import CtrlTelaCenario
from ifes.util import Singleton
from ifes.cgt import AplGerenciarJogador
from ifes.cgd import Error
class CtrlTelaLogin(Singleton.Singleton):

    def __init__(self):
        self.tela = TelaLogin.TelaLogin()
        self.telaJogando = TelaCenario.TelaCenario()
        self.ctrl_cenario = CtrlTelaCenario.CtrlTelaCenario()
        self.mostrandoCenario = False
        self.pessoa = None
        self.opcao = 0
        print("Invocando o metodo construtor mais de uma vez nao pode !!")

    def mostrar_login(self, game):
        # LOGIN
             #1 Enviar
             #0 Sair
        #Status padrao
            #0 Nao logado
            #1 Logado

        if self.opcao == 0:

            #if self.mostrandoCenario == False and self.pessoa == None:
            game.update_clock(10)
            self.pessoa, qual = self.tela.mostrar_login(game)
            if qual == 0:
                return 0
            else:
                if(self.pessoa != None):
                    print(self.pessoa)
                    try:

                        self.pessoa = AplGerenciarJogador.AplGerenciarJogador.logar_jogador(self.pessoa)
                        self.mostrandoCenario = True
                        self.opcao = 1
                        waiting = 0
                        while waiting <= 200:
                            self.tela.update_error(game, waiting)
                            waiting += 1
                        game.usuario = self.pessoa

                        game.update_clock(30)

                    except Error.Error as arg:
                        print('Msg: ' + arg.msg)
                        self.tela.exibe_mensagem(arg.msg)

        else:
        #elif self.pessoa != None and self.mostrandoCenario == True:
            status = self.ctrl_cenario.mostrar_cenario(game)
            print('Status: %d' % status)
            if(status == 0):
                #self.mostrandoCenario = False
                AplGerenciarJogador.AplGerenciarJogador.salvar_jogador(game.usuario)
                game.update_clock(10)
                time.sleep(2)
                return 0
        #elif self.pessoa != None and self.mostrandoCenario == False:
        #    self.mostrandoCenario = True

        return 1

