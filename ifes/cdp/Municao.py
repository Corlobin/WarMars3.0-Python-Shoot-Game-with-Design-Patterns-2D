__author__ = 'Ricardo'
import pygame

class Municao(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([10, 4])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += 10