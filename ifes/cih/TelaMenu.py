__author__ = 'Ricardo'

import pygame

from ifes.cdp import *

class TelaMenu(object):
    def __init__(self):
        self.opcao = 1

        self.bg_menu = Imagem.Imagem.load_image('menu.png', 0)
        self.seta = Imagem.Imagem.load_image('seta.png', 1)

        self.fonte = pygame.font.SysFont("comicsansms", 23)
        self.texto_iniciar = self.fonte.render("Iniciar", 1, (0, 0, 0))
        self.texto_ranking = self.fonte.render("Ranking", 1, (0, 0, 0))
        self.texto_creditos = self.fonte.render("Creditos", 1, (0, 0, 0))
        self.texto_cadastrar = self.fonte.render("Cadastrar", 1, (0, 0, 0))
        self.texto_sair = self.fonte.render("Sair", 1, (0, 0, 0))

    def mostrar_menu(self, game):

        if game.botoes[0]: #cima
            if  self.opcao <= 5 and self.opcao > 1 :
                self.opcao -= 1
                print(self.opcao)

        if game.botoes[1]: #baixo
            if self.opcao >= 1 and self.opcao < 5 :
                self.opcao += 1
                print(self.opcao)

        if game.botoes[4]:  # KEY ENTER
            if self.opcao == 5 :
                game.status = 99
            game.status = self.opcao


        self.update(game)
        return

    def retorna_posicao(self):
        if self.opcao == 6 :
            return ((5-1) * 30)+5
        return ((self.opcao-1) * 30)+5

    def update(self, game):
        game.screen.blit(self.bg_menu, (0, 0))
        game.screen.blit(self.texto_iniciar, (300, 280))
        game.screen.blit(self.texto_cadastrar, (300, 310))
        game.screen.blit(self.texto_ranking, (300, 340))
        game.screen.blit(self.texto_creditos, (300, 370))
        game.screen.blit(self.texto_sair, (300, 400))
        game.screen.blit(self.seta, (275, 280+self.retorna_posicao()))

        pygame.display.update()
        game.fps = 10

