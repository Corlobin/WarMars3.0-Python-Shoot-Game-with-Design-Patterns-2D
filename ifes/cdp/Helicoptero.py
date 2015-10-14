__author__ = 'Ricardo'
import pygame

from ifes.cgd.Imagem import Imagem


class Helicoptero(pygame.sprite.Sprite):

    def __init__(self, img, speed):
        pygame.sprite.Sprite.__init__(self)

        self.speed = speed
        self.image = Imagem.load_image(img, 1)
        self.rect = self.image.get_rect()

        self._pontos = 0
        self._highscore = 0
        self._municao = 100

    def get_speed(self):
        return self.speed

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

    def move_baixo(self):
        self.rect = self.rect.move(0, self.speed)

    def move_cima(self):
        self.rect = self.rect.move(0, -self.speed)

    def move_esquerda(self):
        self.rect.x -= self.speed



