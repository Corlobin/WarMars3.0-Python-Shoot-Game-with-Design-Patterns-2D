__author__ = 'Ricardo'

from ifes.cdp.Inimigo import Inimigo
from ifes.util.GameFactory import GameFactory

class GameInimigo(GameFactory):
    def criar_inimigo(self):
        return Inimigo()
