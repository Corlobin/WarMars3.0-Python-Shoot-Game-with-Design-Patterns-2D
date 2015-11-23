__author__ = 'Ricardo'

from ifes.cdp.Inimigo import Inimigo
import random
from ifes.util.Singleton import  Singleton
from ifes.util.Desenvolvedor import Desenvolvedor
from ifes.util.InimigoFlyweightFactory import InimigoFlyweightFactory
from ifes.cdp import Pessoa
class FabricaInimigo():
    @staticmethod
    def criar_inimigo():
        # Aqui eu deixo dinamicamente ele escolher a classe que ele quer importar.
        # Se eu quiser acrescentar mais um inimigo basta adicionar nessa lista e aumentar o total de inimigos
        #totalInimigos = 3
        #inimigos = ['Aviao', 'Boing', 'Elite', 'Helicoptero']
        #num = random.randint(0, totalInimigos)
        #inimigoPassado = inimigos[num]
        #builder = Reflection.reflection_builder(inimigoPassado)
        inimigoPassado = FabricaInimigo.inimigo_aleatorio()
        peso_mosca = InimigoFlyweightFactory()
        builder = peso_mosca.get_builder(inimigoPassado)
        desenvolvedor = Desenvolvedor()
        inimigo = desenvolvedor.criar_inimigo(builder)
        return inimigo
    @staticmethod
    def inimigo_aleatorio():
        totalInimigos = 3
        inimigos = ['Aviao', 'Boing', 'Elite', 'Helicoptero']
        num = random.randint(0, totalInimigos)
        return inimigos[num]


