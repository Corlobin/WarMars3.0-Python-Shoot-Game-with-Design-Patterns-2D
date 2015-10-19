__author__ = 'Ricardo'
import pygame

class Municao(pygame.sprite.Sprite):

    def __init__(self, forma):
        super().__init__()
        self.image = pygame.Surface([10, 4])
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect()
        self.forma = forma

    def update(self):
        if(self.forma == 1):
            self.rect.x += 10
        else:
            self.rect.x -= 10
    def draw(self, surface):
        surface.blit(self.image, self.rect)