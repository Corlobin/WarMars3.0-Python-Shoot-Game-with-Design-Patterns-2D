__author__ = 'Ricardo'

import pygame
import random

from ifes.cdp import *
from ifes.cgd import Imagem, Som
from ifes.cdp import Inimigo
class TelaCenario(object):
    def __init__(self):
        # Iniciais
        self.bg_um = Imagem.Imagem.load_image('cenario_4.png', 0)
        self.bg_um = pygame.transform.scale(self.bg_um, (640, 480))
        self.bg_dois = Imagem.Imagem.load_image('cenario_4.png', 0)
        self.bg_dois = pygame.transform.scale(self.bg_dois, (640, 480))
        self.bg_dois_x = self.bg_dois.get_width()
        self.bg_um_x = 0
        self.player = Helicoptero.Helicoptero("aviaoplayer.png", 8)
        self.lstInimigos = []

        self.timeInimigo = 50
        self.counter = 10
        self.all_sprites_list = pygame.sprite.Group()
        self.municoes_list = pygame.sprite.Group()

        self.all_sprites_list.add(self.player)


        # Prefacio
        self.bg_prefacio = Imagem.Imagem.load_image('tela_tutorial.png', 0)
        self.fonte = pygame.font.SysFont("comicsansms", 18)
        self.seta = Imagem.Imagem.load_image('seta.png', 1)
        self.texto_iniciar = self.fonte.render("Continuar", 1, (0, 0, 0))
        self.pontos = self.fonte.render("Pontos: 0", 1, (255, 255, 255))
        return


    def mostrar_fase(self, game):

        if game.botoes[0]: #Cima
            self.player.move_cima()
        elif game.botoes[1]: #Baixo
            self.player.move_baixo()
        if game.botoes[7] and self.counter <= 0: #backspace
            municao = Municao.Municao()
            municao.rect.x = self.player.rect.x + 38 #Para deixar a municao saindo rente ao cano da arma
            municao.rect.y = self.player.rect.y + 38 #Para deixar a municao saindo rente ao cano da arma
            self.all_sprites_list.add(municao)
            self.municoes_list.add(municao)
            self.counter = 10


        if (self.timeInimigo <= 0):
            inimigo = Inimigo.Inimigo()
            self.lstInimigos.append(inimigo)
            self.all_sprites_list.add(inimigo)
            self.timeInimigo = 50

        print(self.lstInimigos)
        self.verifica_municoes() #Usado para deletar a municao caso ela atinja um inimigo ou saia fora da tela

        for inimigo in self.lstInimigos:
            inimigo.move_esquerda()
            if(inimigo.rect.x <= 0):
                self.all_sprites_list.remove(inimigo)
                self.lstInimigos.remove(inimigo)


        self.move_cenario_direita(game)
        self.all_sprites_list.update()
        self.all_sprites_list.draw(game.screen)

        pygame.display.flip()
        pygame.display.update()

    def verifica_municoes(self):
        for municao in self.municoes_list:
            if municao.rect.y < -10:
                self.municoes_list.remove(municao)
                self.all_sprites_list.remove(municao)
            for inimigo in self.lstInimigos:
                if inimigo.rect.colliderect(municao.rect):
                    self.all_sprites_list.remove(inimigo)
                    self.all_sprites_list.remove(municao)
                    self.player.atualiza_pontuacao(1)
                    self.atualiza_pontuacao()

        self.counter -= 1
        self.timeInimigo -= 1





    def mostrar_prefacio(self, game):
        if game.botoes[4]:  # KEY ENTER
            return 1

        game.screen.blit(self.bg_prefacio, (0, 0))
        game.screen.blit(self.texto_iniciar, (410, 370))
        game.screen.blit(self.seta, (385, 370))

        pygame.display.update()
        game.fps = 30


    def move_cenario_direita(self, game):
        self.bg_um_x -= 10
        self.bg_dois_x -= 10
        if self.bg_um_x <= -1 * self.bg_um.get_width():
            self.bg_um_x = self.bg_dois_x + self.bg_dois.get_width()
        if self.bg_dois_x <= -1 * self.bg_dois.get_width():
            self.bg_dois_x = self.bg_um_x + self.bg_um.get_width()

        game.screen.blit(self.bg_um, (self.bg_um_x, 0))
        game.screen.blit(self.bg_dois, (self.bg_dois_x, 0))
        game.screen.blit(self.pontos, (500, 0))

        return

    def atualiza_pontuacao(self):
        pontuacao = format("Pontos: %d" %(self.player.get_pontuacao()))
        self.pontos = self.fonte.render(pontuacao, 1, (255, 255, 225))

