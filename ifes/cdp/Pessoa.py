__author__ = 'Ricardo'

from ifes.cdp import Helicoptero
from ifes.cgd import Error
import datetime
class Pessoa:
    def __init__(self):
        self._datacriado = datetime.datetime.now()
        self.id = 1
        self._nome = ""
        self._senha = ""
        self._idade = 0

        self._highscore = 0
        self._imagem = None
        self._tempojogo = 0
        self._tiros = 0
        self._percas = 0

    def set_nome(self, nome):
        if len(nome) < 5:
            raise Error.Error('Nome tem que ter no min 5 caracteres.')

        self._nome = nome

    def set_idade(self, idade):

        if(idade < 12):
            raise Error.Error('Idade minima requerida: 12')

        self._idade = idade

    def set_senha(self, senha):

        if len(senha) < 5:
            raise Error.Error('Senha tem que ter no min 5 caracteres.')

        self._senha = senha

    #def __init__(self, id, data_criacao, nome, senha, idade, highscore, imagem, tempojogo, tiros, percas):
    def set_id(self, id):
        self.id = id
    def set_data_criacao(self, data_criacao):
        self._datacriado = data_criacao
    def set_highscore(self, highscore):
        self._highscore = highscore
    def set_imagem(self, imagem):
        self._imagem = imagem
    def set_tempojogo(self, tempo_jogo):
        self._tempojogo = tempo_jogo
    def set_tiros(self, tiros):
        self._tiros = tiros
    def set_percas(self, percas):
        self._percas = percas

    def get_id(self):
        return self.id
    def get_data_criacao(self):
        return self._datacriado
    def get_highscore(self):
        return self._highscore
    def get_imagem(self):
        return self._imagem
    def get_tempojogo(self):
        return self._tempojogo
    def get_tiros(self):
        return self._tiros
    def get_percas(self):
        return self._percas


    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def get_senha(self):
        return self._senha

    # Retornando uma tupla
    def toString(self):
        return (self._datacriado, self._nome, self._senha, self._idade, self._highscore, self._imagem, self._tempojogo, self._tiros, self._percas)


