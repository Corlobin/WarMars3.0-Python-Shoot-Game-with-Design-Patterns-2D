__author__ = 'Ricardo'

import pygame

from ifes.cgd import *

class TelaFim(object):
    def __init__(self):
        self.background_menu = Imagem.Imagem.load_image('perdeu.png', 0)
        self.fonte = pygame.font.SysFont("comicsansms", 23)
        self.seta = Imagem.Imagem.load_image('seta.png', 1)
        self.texto_iniciar = self.fonte.render("Voltar", 1, (0, 0, 0))
        self.novo_score = self.fonte.render("Nao fez novo score!", 1, (0, 0, 0))
        self.texto = "Nao fez novo score"

    def mostrar_fim(self, game):
        if game.botoes[4]:  # KEY ENTER
            return 3

        if  0 == 0 :
            #game.player.highscore = game.player.pontos
            self.texto = "Novo score: %d" %(5)

        self.novo_score = self.fonte.render(self.texto, 1, (0, 0, 0))


        game.screen.blit(self.background_menu, (0, 0))
        game.screen.blit(self.texto_iniciar, (300, 400))
        game.screen.blit(self.seta, (275, 405))
        game.screen.blit(self.novo_score, (200, 50))
        pygame.display.update()
        return 2

