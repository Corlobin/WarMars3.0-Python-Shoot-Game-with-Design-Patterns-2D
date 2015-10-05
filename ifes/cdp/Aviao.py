__author__ = 'Ricardo'


__author__ = 'Ricardo'
import pygame

from ifes.cdp.Imagem import Imagem


class Aviao(pygame.sprite.Sprite):
    def __init__(self, img, width, height, w, h, qtd):
        pygame.sprite.Sprite.__init__(self)
        self.width=w
        self.height=h
        self.num_images = qtd
        self.c_image = 0
        self.image = Imagem.load_image(img, 1)
        self.rect = self.image.get_rect()
        self.pos = self.image.get_rect().move(width, height)
        self.pontos = 1
        self.vertical = 0


    def set_pontos(self, pontos):
        self.pontos = pontos
    def get_pontos(self):
        return self.pontos

    def get_rect(self):
        return self.pos
    def update(self):
        if self.c_image >= self.num_images-1 :
            self.c_image = 0
        else:
            self.c_image += 1

    def render(self, window):
        window.blit(self.image, self.pos, (self.c_image*self.width, 0, self.width, self.height))

    def move_esquerda(self, velocidade):
        self.pos.left -= velocidade
    def move_direita(self, velocidade):
        self.pos.left += velocidade
    def move_baixo(self, velocidade):
        self.height += velocidade
    def move_cima(self, velocidade):
        self.height -= velocidade

