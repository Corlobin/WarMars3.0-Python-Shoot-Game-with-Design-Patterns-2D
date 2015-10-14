__author__ = 'Ricardo'


import random
from ifes.cdp import Helicoptero

class Inimigo(Helicoptero.Helicoptero):

    def __init__(self):
        imgs = ["aviaoinimigo.png", "aviaoinimigo2.png", "aviaoinimigo3.png", "aviaoinimigo4.png"]
        super().__init__(imgs[random.randint(0,3)], 7)
        self.rect.x = 500
        self.rect.y = random.randint(25,450)

