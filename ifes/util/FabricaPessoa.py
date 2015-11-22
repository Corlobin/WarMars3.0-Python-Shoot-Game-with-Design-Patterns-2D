__author__ = 'Ricardo'
from ifes.cdp.Pessoa import Pessoa
class FabricaPessoa:
    @staticmethod
    def criar_pessoa():
        return Pessoa()