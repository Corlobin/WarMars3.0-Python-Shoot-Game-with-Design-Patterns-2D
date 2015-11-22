__author__ = 'Ricardo'

from ifes.util.BuilderAbstrato import BuilderAbstrato
from ifes.util.FabricaInimigoBoing import FabricaInimigoBoing

class FabricaInimigoBoingBuilder(BuilderAbstrato):
    def __init__(self):
        super(FabricaInimigoBoingBuilder, self).__init__(FabricaInimigoBoing)
        self.fabrica = FabricaInimigoBoing()