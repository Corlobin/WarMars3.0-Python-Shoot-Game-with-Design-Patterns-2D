__author__ = 'Ricardo'

from ifes.util.BuilderAbstrato import BuilderAbstrato
from ifes.util.FabricaInimigoElite import FabricaInimigoElite

class FabricaInimigoEliteBuilder(BuilderAbstrato):
    def __init__(self):
        super(FabricaInimigoEliteBuilder, self).__init__(FabricaInimigoElite)
        self.fabrica = FabricaInimigoElite()