__author__ = 'Ricardo'

from ifes.cdp.Inimigo import Inimigo

from ifes.util.Singleton import  Singleton
class GameInimigo(Singleton):
    def criar_inimigo(self):
        return Inimigo()
