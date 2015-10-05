__author__ = 'Ricardo'

import pygame
import random

from ifes.cdp import *




class TelaCenario(object):
    def __init__(self):
        # Iniciais
        self.bg_um = Imagem.Imagem.load_image('cenario_4.png', 0)
        self.bg_um = pygame.transform.scale(self.bg_um, (640, 480))
        self.bg_dois = Imagem.Imagem.load_image('cenario_4.png', 0)
        self.bg_dois = pygame.transform.scale(self.bg_dois, (640, 480))

        self.bg_dois_x = self.bg_dois.get_width()
        self.bg_um_x = 0

        self.badtimer = 100
        self.badtimer1 = 0
        self.badguys = [[640, 100]]
        self.badguyimg1 = Imagem.Imagem.load_image('aviao.png', 1)
        self.badguyimg = self.badguyimg1


        # Prefacio
        self.bg_prefacio = Imagem.Imagem.load_image('tela_tutorial.png', 0)
        self.fonte = pygame.font.SysFont("comicsansms", 18)
        self.seta = Imagem.Imagem.load_image('seta.png', 1)
        self.texto_iniciar = self.fonte.render("Continuar", 1, (0, 0, 0))
        self.pontos = self.fonte.render("Pontos: 0", 1, (255, 255, 255))
        #width, height, w, h, qtd):
        self.aviao = Aviao.Aviao("aviao.png", 400, 200, 68, 60, 1)

        self.firespeed = 3

        self.bullet_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()
        return

    def mostrar_prefacio(self, game):
        Som.Som.tocar(game.music, "texto_prefacio.wav")
        if game.botoes[4]:  # KEY ENTER
            Som.Som.parar()
            game.status = 21

        game.screen.blit(self.bg_prefacio, (0, 0))
        game.screen.blit(self.texto_iniciar, (410, 370))
        game.screen.blit(self.seta, (385, 370))

        pygame.display.update()
        game.fps = 30

    def mostrar_fase(self, game):
        Som.Som.tocar(game.music, "fase1.wav")
        x = 0
        y = 0

        if game.botoes[0]:
            game.player.move_cima()
        elif game.botoes[1]:
            game.player.move_baixo()
        if game.botoes[7] and self.firespeed <= 0:
            self.firespeed = 8
            bullet = Bullet.Bullet()
            # Set the bullet so it is where the player is
            bullet.rect.x = game.player.pos.x+38
            bullet.rect.y = game.player.pos.y+38
            # Add the bullet to the lists
            self.all_sprites_list.add(bullet)
            self.bullet_list.add(bullet)
        self.firespeed -= 1

        self.move_cenario_direita(game)

        game.screen.blit(self.bg_um, (self.bg_um_x, 0))
        game.screen.blit(self.bg_dois, (self.bg_dois_x, 0))
        game.screen.blit(self.pontos, (500, 0))
        self.all_sprites_list.update()


        index=0
        for badguy in self.badguys:
            badrect = pygame.Rect(self.badguyimg.get_rect())
            badrect.top = badguy[1]
            badrect.left = badguy[0]
            if game.player.get_rect().colliderect(badrect) :
                Som.Som.parar()
                self.badguys.pop(index)
                game.status = 5

            index+=1
        for bullet in self.bullet_list:
            index=0
            for badguy in self.badguys:

                #print(badguy)
                badrect = pygame.Rect(self.badguyimg.get_rect())
                badrect.top = badguy[1]
                badrect.left = badguy[0]
                if badrect.colliderect(bullet.rect) :
                    #print("collide")
                    self.bullet_list.remove(bullet)
                    self.all_sprites_list.remove(bullet)
                    game.player.atualiza_pontuacao(1)
                    self.atualiza_pontuacao(game)
                    self.badguys.pop(index)
                    #print("colidiram")
                index+=1
            if bullet.rect.y < -10:
                self.bullet_list.remove(bullet)
                self.all_sprites_list.remove(bullet)

        self.badtimer -= 1
        if self.badtimer == 0:
            self.badguys.append([640, random.randint(50,430)])
            self.badtimer= 100-(self.badtimer1*2)
            if self.badtimer1 >= 35:
                self.badtimer1=35
            else:
                self.badtimer1 += 5
        index = 0
        for badguy in self.badguys:
            if badguy[0]<= 0 :
                self.badguys.pop(index)
            badguy[0]-=7
            index+=1
        for badguy in self.badguys:
            game.screen.blit(self.badguyimg, badguy)


        game.player.render(game.screen)
        game.player.update()
        self.all_sprites_list.draw(game.screen)

        pygame.display.flip()
        pygame.display.update()

        game.fps = 30



    def move_cenario_direita(self, game):
        self.bg_um_x -= game.player.speed*2
        self.bg_dois_x -= game.player.speed*2
        if self.bg_um_x <= -1 * self.bg_um.get_width():
            self.bg_um_x = self.bg_dois_x + self.bg_dois.get_width()
        if self.bg_dois_x <= -1 * self.bg_dois.get_width():
            self.bg_dois_x = self.bg_um_x + self.bg_um.get_width()
        return
    def atualiza_pontuacao(self, game):
        pontuacao = format("Pontos: %d" %(game.player.get_pontuacao()))
        self.pontos = self.fonte.render(pontuacao, 1, (255, 255, 225))

