__author__ = 'Ricardo'
import pygame

from ifes.cgd.Imagem import Imagem
from ifes.cdp.Municao import Municao


class Helicoptero(pygame.sprite.Sprite):

    def __init__(self, img, speed):
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed
        self.image = Imagem.load_image(img, 1)
        self.rect = self.image.get_rect()

        self._tiros = 0
        self._acertos = 0

        self._pontos = 0
        self._highscore = 0
        self._municao = 100
        self._delay = 15 # Delay de cada tiro

        self.municoes_list = pygame.sprite.Group()

    def update(self):
        for municao in self.municoes_list:
            if municao.rect.x > 640:
                municao.kill()
        self.municoes_list.update()
        if(self._delay > 0):
            self._delay -= 1

    def draw(self, surface):
        self.municoes_list.draw(surface)
        surface.blit(self.image, self.rect)

    def get_speed(self):
        return self.speed

    def set_imagem(self, img):
        self.image = Imagem.load_image(img, 1)
        self.rect = self.image.get_rect()

    def set_speed(self, speed):
        self.speed = speed

    def get_municao(self):
        return self._municao

    def set_municao(self, municao):
        self._municao = municao

    def atualiza_municao(self):
        self._municao -= 1

    def atualiza_pontuacao(self, pontos):
        self._pontos += pontos

    def get_pontuacao(self):
        return self._pontos

    def atualiza_acertos(self):
        self._acertos += 1

    def atualiza_pontos(self):
        self._pontos += 1
    def move_baixo(self):
        self.rect = self.rect.move(0, self.speed)

    def move_cima(self):
        self.rect = self.rect.move(0, -self.speed)

    def move_esquerda(self):
        self.rect.x -= self.speed

    def atirar(self):
        if(self._delay <= 0):
            municao = Municao(1)
            municao.rect.x = self.rect.x + 38 #Para deixar a municao saindo rente ao cano da arma
            municao.rect.y = self.rect.y + 38 #Para deixar a municao saindo rente ao cano da arma
            self.municoes_list.add(municao)
            self._delay = 15
            self._municao -= 1
            self._tiros += 1



