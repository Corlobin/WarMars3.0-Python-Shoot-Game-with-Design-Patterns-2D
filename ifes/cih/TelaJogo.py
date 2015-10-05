__author__ = 'Ricardo'

import pygame

from ifes.cih import TelaCenario
from ifes.cih import TelaMenu
from ifes.cih import TelaCreditos
from ifes.cih import TelaRanking
from ifes.cih import TelaCadastro
from ifes.cih import TelaFim
from ifes.cdp import Jogador
class TelaJogo(object):

    def __init__(self):
        self.clock = pygame.time.Clock()
        self.status = 20
        self.fps = 30
        self.teclas = ""
        return

    def inicia(self):
        pygame.init()
        pygame.font.init()
        self.music = pygame.mixer
        self.music.init()
        pygame.mouse.set_visible(True)
        pygame.display.set_caption("Guerra em Marte")
        self.screen = pygame.display.set_mode((640, 480))
        self.player = Jogador.Jogador("aviaoplayer.png", 320, 5, 55, 75, 1)

        self.menu = TelaMenu.TelaMenu()
        self.cenario = TelaCenario.TelaCenario()
        self.ranking = TelaRanking.TelaRanking()
        self.creditos = TelaCreditos.TelaCreditos()
        self.cadastro = TelaCadastro.TelaCadastro()
        self.fim = TelaFim.TelaFim()
                       #0CIMA  #1BAIX  #2ESQ   #3DIRE  #4ENTER #5ESC #6TAB #7 BACKSPACE
        self.botoes = [False, False, False, False, False, False, False, False]

        while self.status != 99: # Loop principal do jogo
            self.capturar_eventos()
            if self.botoes[5] :
                self.status = 99

            if self.status == 1: # Logar
                self.cenario.mostrar_prefacio(self)
            elif self.status == 2: #Cadastrar
                self.cadastro.mostrar_cadastro(self)
            elif self.status == 3: #Ranking
                self.ranking.mostrar_ranking(self)
            elif self.status == 4: #Creditos
                self.creditos.mostrar_creditos(self)
            elif self.status == 5:
                self.fim.mostra_fim(self)

            elif self.status == 20: #Menu
                self.menu.mostrar_menu(self)
            elif self.status == 21: #Jogar
                self.cenario.mostrar_fase(self)

            self.clock.tick(self.fps)
        pygame.quit()
        return

    def capturar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    self.botoes[3] = True
                if evento.key == pygame.K_LEFT:
                    self.botoes[2] = True
                if evento.key == 13:  # KEY ENTER
                    self.botoes[4] = True
                if evento.key == pygame.K_UP:  # PARA CIMA
                    self.botoes[0] = True
                if evento.key == pygame.K_DOWN:  # PARA BAIXO
                    self.botoes[1] = True
                if evento.key == pygame.K_ESCAPE:  # ESC
                    self.botoes[5] = True
                if evento.key == pygame.K_TAB:
                    self.botoes[6] = True
                if evento.key == pygame.K_SPACE:
                    self.botoes[7] = True

                #Capturando do teclado e deletando ..
                if  (evento.key >= 97 and evento.key <= 122) or (evento.key >= 48 and evento.key <= 57) :
                    self.teclas = self.teclas + chr(evento.key)

                if (evento.key == pygame.K_DELETE) or (evento.key == pygame.K_BACKSPACE):
                    if  len(self.teclas) != 0 :
                        self.teclas = self.teclas[:-1]


            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_RIGHT:
                    self.botoes[3] = False
                if evento.key == pygame.K_LEFT:
                    self.botoes[2] = False
                if evento.key == 13:
                    self.botoes[4] = False
                if evento.key == pygame.K_UP:  # PARA CIMA
                    self.botoes[0] = False
                if evento.key == pygame.K_DOWN:  # PARA BAIXO
                    self.botoes[1] = False
                if evento.key == pygame.K_ESCAPE:  # ESC
                    self.botoes[5] = False
                if evento.key == pygame.K_TAB:  # TAB
                    self.botoes[6] = False
                if evento.key == pygame.K_SPACE:
                    self.botoes[7] = False

            if evento.type == pygame.QUIT:
                self.botoes[5] = True



