__author__ = 'Ricardo'

from ifes.util.BuilderAbstrato import BuilderAbstrato
from ifes.util.FabricaInimigoHelicoptero import FabricaInimigoHelicoptero

class FabricaInimigoHelicopteroBuilder(BuilderAbstrato):
    def __init__(self):
        super(FabricaInimigoHelicopteroBuilder, self).__init__(FabricaInimigoHelicoptero)
        self.fabrica = FabricaInimigoHelicoptero()