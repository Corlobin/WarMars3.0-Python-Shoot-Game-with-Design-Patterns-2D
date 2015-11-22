__author__ = 'Ricardo'

from ifes.util.BuilderAbstrato import BuilderAbstrato
from ifes.util.FabricaInimigoAviao import FabricaInimigoAviao

class FabricaInimigoAviaoBuilder(BuilderAbstrato):
    def __init__(self):
        super(FabricaInimigoAviaoBuilder, self).__init__(FabricaInimigoAviao)
        self.fabrica = FabricaInimigoAviao()