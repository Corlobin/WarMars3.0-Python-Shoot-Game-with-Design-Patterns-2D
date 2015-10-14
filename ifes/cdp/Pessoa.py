__author__ = 'Ricardo'

from ifes.cdp import Helicoptero
from ifes.cgd import Error
import datetime
class Pessoa:
    def __init__(self):
        self._datacriado = datetime.datetime.now()
        self._nome = ""
        self._senha = ""
        self._idade = 0

        self._highscore = 0
        self._imagem = None
        self._tempojogo = 0
        self._tiros = 0
        self._percas = 0

        self._helicoptero = None

    def get_helicoptero(self):
        return self._helicoptero

    def create_helicoptero(self):
        self.helicoptero = Helicoptero.Helicoptero()

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

    def get_nome(self):
        return self._nome

    def get_idade(self):
        return self._idade

    def get_senha(self):
        return self._senha

    def toString(self):
        print(type(self._idade))
                #Data_criado,       Nome,       Senha,      Idade,         Highscore,       Imagem,         TempoJogo,  Tiros,      Percas
        return (self._datacriado, self._nome, self._senha, self._idade, self._highscore, self._imagem, self._tempojogo, self._tiros, self._percas)