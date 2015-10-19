__author__ = 'Ricardo'
import pygame
import random
class Fragment(pygame.sprite.Sprite):
        """generic Fragment class. Inherits to blue Fragment (implosion),
           red Fragment (explosion), smoke (black) and shots (purple)"""
        def __init__(self, pos, layer = 9):
            FRAGMENTMAXSPEED = 200
            self._layer = layer
            pygame.sprite.Sprite.__init__(self, self.groups)
            self.pos = [0.0,0.0]
            self.fragmentmaxspeed = FRAGMENTMAXSPEED# try out other factors !

        def init2(self):  # split the init method into 2 parts for better access from subclasses
            self.image = pygame.Surface((10,10))
            self.image.set_colorkey((0,0,0)) # black transparent
            pygame.draw.circle(self.image, self.color, (5,5), random.randint(2,5))
            self.image = self.image.convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.center = self.pos #if you forget this line the sprite sit in the topleft corner
            self.time = 0.0

        def update(self, seconds):
            self.time += seconds
            if self.time > self.lifetime:
                self.kill()
            self.pos[0] += self.dx * seconds
            self.pos[1] += self.dy * seconds
            self.rect.centerx = round(self.pos[0],0)
            self.rect.centery = round(self.pos[1],0)