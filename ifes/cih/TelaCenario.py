__author__ = 'Ricardo'

import pygame
import random

from ifes.cdp import *
from ifes.cgd import Imagem, Som
from ifes.util.GameInimigo import GameInimigo

from ifes.util.GameInimigo import GameInimigo
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
        self.inimigo = GameInimigo().criar_inimigo()
        #self.inimigo.rect.y = 10


        self.sprites_list = pygame.sprite.Group()
        self.helicoptero_sprite = pygame.sprite.Group()
        self.inimigos_list = pygame.sprite.Group()

        self.sprites_list.add(self.player)
        self.sprites_list.add(self.inimigo)

        self.helicoptero_sprite.add(self.player)
        self.inimigos_list.add(self.inimigo)
        self.time = 45


        # Prefacio
        self.bg_prefacio = Imagem.Imagem.load_image('tela_tutorial.png', 0)
        self.fonte = pygame.font.SysFont("comicsansms", 18)
        self.seta = Imagem.Imagem.load_image('seta.png', 1)
        self.texto_iniciar = self.fonte.render("Continuar", 1, (0, 0, 0))
        self.pontos = self.fonte.render("Pontos: 0", 1, (255, 255, 255))

        # Fim
        self.bgfim = Imagem.Imagem.load_image('perdeu.png', 0)
        self.novo_score = self.fonte.render("Nao fez novo score!", 1, (0, 0, 0))


        return


    def mostrar_fase(self, game):

        if game.botoes[0]: #Cima
            self.player.move_cima()
        elif game.botoes[1]: #Baixo
            self.player.move_baixo()
        if game.botoes[7]: #backspace
            self.player.atirar()

        self.move_cenario_direita(game)
        if self.time <= 0:
            inimigo = GameInimigo().criar_inimigo()
            self.inimigos_list.add(inimigo)
            self.sprites_list.add(inimigo)
            self.time = 60
        self.time -= 1
        print(self.inimigos_list)

        result1 = pygame.sprite.groupcollide(self.helicoptero_sprite, self.inimigos_list, False, True)
        if result1:
            print("Fim de jogo")
            return 2

        result2 = pygame.sprite.groupcollide(self.player.municoes_list, self.inimigos_list, False, True)
        if result2:
            self.player.atualiza_acertos()
            self.player.atualiza_pontos()

        for inimigo in self.inimigos_list:
            result3 = pygame.sprite.groupcollide(self.helicoptero_sprite, inimigo.municoes_list, False, True)
            if result3:
                inimigo.kill()
                print("OK")
                return 2

        self.sprites_list.update()
        for sprite in self.sprites_list:
            sprite.draw(game.screen)
        self.atualiza_pontuacao()
        pygame.display.flip()
        return 1

    def mostrar_prefacio(self, game):
        if game.botoes[4]:  # KEY ENTER
            return 1

        game.screen.blit(self.bg_prefacio, (0, 0))
        game.screen.blit(self.texto_iniciar, (410, 370))
        game.screen.blit(self.seta, (385, 370))

        pygame.display.update()
        game.fps = 30

    def mostrar_fim(self, game):
        if game.botoes[4]:  # KEY ENTER
            return 0

        self.texto_iniciar = self.fonte.render("Voltar", 1, (0, 0, 0))
        #print('Pontuacao: %d' % self.player.get_pontuacao())
        #print('Highscore: %d' % game.usuario.get_highscore())

        if self.player.get_pontuacao() > game.usuario.get_highscore():
            texto = "Novo score: %d" %(self.player.get_pontuacao())
            self.novo_score = self.fonte.render(texto, 1, (0, 0, 0))
            game.usuario.set_highscore(self.player.get_pontuacao())


        game.screen.blit(self.bgfim, (0, 0))
        game.screen.blit(self.texto_iniciar, (300, 400))
        game.screen.blit(self.seta, (275, 405))
        game.screen.blit(self.novo_score, (200, 50))
        pygame.display.update()
        return 2

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

