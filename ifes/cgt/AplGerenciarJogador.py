__author__ = 'Ricardo'

from ifes.cgd import DAOJogador

class AplGerenciarJogador():
    @staticmethod
    def cadastra_jogador(usuario, senha, idade):
        print(usuario, senha, idade)
        DAOJogador.DAOJogador.insere_jogador(usuario, senha, idade)

        return
    @staticmethod
    def retorna_jogadores():
        return DAOJogador.DAOJogador.get_jogadores()

