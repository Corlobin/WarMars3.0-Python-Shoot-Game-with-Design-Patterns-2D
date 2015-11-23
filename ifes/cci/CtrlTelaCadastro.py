__author__ = 'Ricardo'


from ifes.cih import TelaCadastro
from ifes.util import Singleton
from ifes.cgt import AplGerenciarJogador
from ifes.cgd import Error
class CtrlTelaCadastro(Singleton.Singleton):
    #Faz o controle da tela do cadastro
    def __init__(self):
        self.tela = TelaCadastro.TelaCadastro()

    def mostrar_cadastro(self, game):

        pessoa,opcao = self.tela.mostrar_cadastro(game)

        if(pessoa != None and opcao == 2):
            try:
                AplGerenciarJogador.AplGerenciarJogador.cadastra_jogador(pessoa)
                self.tela.exibe_mensagem("Funcionou essa bagaca")
            except Error.Error as arg:
                print(arg.msg)
                self.tela.exibe_mensagem(arg.msg)

        #print(pessoa, opcao)
        return opcao


