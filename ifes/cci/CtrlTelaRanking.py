__author__ = 'Ricardo'


from ifes.cih import TelaRanking
from ifes.cih import Singleton
class CtrlTelaRanking(Singleton.Singleton):

    def __init__(self):

        self.tela = TelaRanking.TelaRanking()

    def mostrar_ranking(self, game):
        opcao = self.tela.mostrar_ranking(game)
        return opcao


