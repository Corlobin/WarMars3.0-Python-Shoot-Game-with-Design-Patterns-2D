__author__ = 'Ricardo'
import pygame

from ifes.cdp.Imagem import Imagem


class Jogador(pygame.sprite.Sprite):

    def __init__(self, img, height, speed, w, h, qtd):
        pygame.sprite.Sprite.__init__(self)

        self.width=w
        self.height=h
        self.num_images = qtd
        self.cImage = 0

        self.speed = speed
        self.image = Imagem.load_image(img, 1)
        self.rect = self.image.get_rect()
        self.pos = self.image.get_rect().move(0, height)

        self.vertical = 0
        self.pontos = 0
        self.highscore = 0

    def atualiza_pontuacao(self, pontos):
        self.pontos += pontos
    def get_pontuacao(self):
        return self.pontos
    def get_rect(self):
        return self.pos
    def update(self):
        if self.cImage >= self.num_images-1 :
            self.cImage = 0
        else:
            self.cImage += 1

    def render(self, window):
        window.blit(self.image, self.pos, (self.cImage*self.width, 0, self.width, self.height))

    def mover(self,x,y):
        if x > 0 :
            self.move_direita()
        elif y > 0 :
            self.move_esquerda()


    def move_direita(self):
        if self.pos.right <= 642:
            self.pos = self.pos.move(self.speed, self.vertical)
        self.update()

    def move_esquerda(self):
        if self.pos.left >= 0:
            self.pos.left = self.pos.left - self.speed
        self.update()

    def move_baixo(self):
        self.pos = self.pos.move(0, self.speed)
    def move_cima(self):
        self.pos = self.pos.move(0, -self.speed)

