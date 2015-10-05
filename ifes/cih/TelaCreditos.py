__author__ = 'Ricardo'

import pygame

from ifes.cdp import *

class TelaCreditos(object):
    def __init__(self):

        self.bg_menu = Imagem.Imagem.load_image('creditos.png', 0)
        self.fonte = pygame.font.SysFont("comicsansms", 23)
        self.seta = Imagem.Imagem.load_image('seta.png', 1)
        self.texto_iniciar = self.fonte.render("Voltar", 1, (0, 0, 0))

    def mostrar_creditos(self, game):
        if game.botoes[4]:  # KEY ENTER
            game.status = 20

        game.screen.blit(self.bg_menu, (0, 0))
        game.screen.blit(self.texto_iniciar, (300, 400))
        game.screen.blit(self.seta, (275, 405))
        pygame.display.update()
        return

