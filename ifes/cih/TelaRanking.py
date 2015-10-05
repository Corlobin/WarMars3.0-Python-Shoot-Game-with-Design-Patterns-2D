__author__ = 'Ricardo'

import pygame

from ifes.cdp import *
from ifes.cgt import AplGerenciarJogador

class TelaRanking(object):
    def __init__(self):

        self.background_menu = Imagem.Imagem.load_image('ranking.png', 0)
        self.fonte = pygame.font.SysFont("comicsansms", 23)
        self.fontebt = pygame.font.SysFont("comicsansms", 13)
        self.seta = Imagem.Imagem.load_image('seta.png', 1)

        self.texto_iniciar = self.fonte.render("Voltar", 1, (0, 0, 0))




    def mostrar_ranking(self, game):
        if game.botoes[4]:  # KEY ENTER
            game.status = 20


        game.screen.blit(self.background_menu, (0, 0))
        game.screen.blit(self.texto_iniciar, (300, 380))
        game.screen.blit(self.seta, (275, 385))
        index = 0
        for jogador in AplGerenciarJogador.AplGerenciarJogador.retorna_jogadores():
            if index != 10 :
                botao = self.fontebt.render(jogador, 1, (0, 0, 0))
                game.screen.blit(botao, (125, 160+(index*20)))
            index+=1
        pygame.display.update()

        return

