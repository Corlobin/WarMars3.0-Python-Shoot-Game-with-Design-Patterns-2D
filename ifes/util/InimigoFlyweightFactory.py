__author__ = 'Ricardo'

from ifes.util.Reflection import Reflection
from ifes.util.Singleton import Singleton
class InimigoFlyweightFactory(Singleton):
    def __init__(self):
        self.dic_builders = {'Aviao':None, 'Boing':None, 'Elite':None, 'Helicoptero':None}

    def get_builder(self, inimigoPassado):
        print(self.dic_builders[inimigoPassado])
        if self.dic_builders[inimigoPassado] == None:
            print('CRIOU UM INIMIGO ' + inimigoPassado)
            self.dic_builders[inimigoPassado] = Reflection.reflection_builder(inimigoPassado)
        return self.dic_builders[inimigoPassado]
