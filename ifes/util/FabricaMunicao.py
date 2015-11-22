__author__ = 'Ricardo'
from ifes.cdp.Municao import Municao
class FabricaMunicao:
    @staticmethod
    def cria_municao(x, y):
        municao = Municao(1)
        municao.rect.x = x + 38 #Para deixar a municao saindo rente ao cano da arma
        municao.rect.y = y + 38 #Para deixar a municao saindo rente ao cano da arma
        return municao