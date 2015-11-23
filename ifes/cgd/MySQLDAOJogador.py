__author__ = 'Ricardo'

from ifes.cgd.DAOJogador import DAOJogador
class MySQLDAOJogador(DAOJogador):
    def __init__(self, fromObj):
        self.fromObject = fromObj
    def mysql_insere(self, jogador):
        self.fromObject.insere_jogador(self, jogador)

