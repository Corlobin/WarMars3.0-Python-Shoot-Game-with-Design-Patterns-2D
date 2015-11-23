__author__ = 'Ricardo'

import time
import pygame
from ifes.cgd.Imagem import Imagem
from ifes.util.Singleton import Singleton
class LoadProxy:
    def __init__(self):
        self.loading = Imagem.load_image('carregando.png', 0)
        self.fonte_error = pygame.font.SysFont("comicsansms", 16)
        self.error = self.fonte_error.render("", 1, (255, 0, 0))
        self.waiting = 0

    def start(self, game):
        while self.waiting <= 5000:
            self.waiting += 1
            game.screen.blit(self.loading, (0, 0))
            mensagem = format("%d" % (self.waiting/50))
            self.error = self.fonte_error.render(mensagem, 1, (255, 0, 0))
            game.screen.blit(self.error, (399, 162))
            pygame.display.update()

