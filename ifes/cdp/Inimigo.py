__author__ = 'Ricardo'


import random
from ifes.cdp import Helicoptero
from ifes.cdp.Municao import Municao
class Inimigo(Helicoptero.Helicoptero):

    def __init__(self):
        imgs = ["aviaoinimigo.png", "aviaoinimigo2.png", "aviaoinimigo3.png", "aviaoinimigo4.png"]
        super().__init__(imgs[random.randint(0,3)], 7)
        self.rect.x = 500
        self.rect.y = random.randint(25,450)
        self.shoot = 15
        self.descendo = 1
        self.subindo = 0


    def update(self):
        self.atirar()
        self.rect.x -= 1
        if(self.rect.x < 0):
            self.kill()
        if(self.descendo):
            if(self.rect.y < 300):
                self.rect.y += 1
            else:
                self.descendo = 0
                self.subindo = 1

        elif(self.subindo):
            if(self.rect.y > 0):
                self.rect.y -= 1
            else:
                self.subindo = 0
                self.descendo = 1

        for municao in self.municoes_list:
            if municao.rect.x < 0:
                municao.kill()

        self.municoes_list.update()




    def atirar(self):
        if self.shoot < 0:
            municao = Municao(2)
            municao.rect.x = self.rect.x + 38 #Para deixar a municao saindo rente ao cano da arma
            municao.rect.y = self.rect.y + 38 #Para deixar a municao saindo rente ao cano da arma
            self.municoes_list.add(municao)
            self.shoot = 15
        self.shoot -= 1

