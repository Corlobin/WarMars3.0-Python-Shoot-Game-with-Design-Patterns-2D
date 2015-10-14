__author__ = 'Ricardo'

import pygame
import sys
class TelaJogo:

    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.music = pygame.mixer
        self.clock = pygame.time.Clock()
        self.music.init()
        self.status = 0
        self.teclas = ""
        pygame.mouse.set_visible(True)
        pygame.display.set_caption("Guerra em Marte - Versao 1.0")
        self.screen = pygame.display.set_mode((640, 480))
        pygame.key.set_repeat(1)
        #0CIMA  #1BAIX  #2ESQ   #3DIRE  #4ENTER #5ESC #6TAB #7 BACKSPACE
        self.botoes = [False, False, False, False, False, False, False, False]
        return

    def update_clock(self, clock):
        self.clock.tick(clock)
    def sair(self):
        pygame.quit()
        sys.exit(0)
    def update(self):
        pygame.display.update()

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
                    self.sair()
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
                if evento.key == pygame.K_TAB:  # TAB
                    self.botoes[6] = False
                if evento.key == pygame.K_SPACE:
                    self.botoes[7] = False

            if evento.type == pygame.QUIT:
                self.sair()




