__author__ = 'Ricardo'

import pygame

from ifes.cgd import *

from ifes.cgt import AplGerenciarJogador

class TelaLogin(object):
    # Essa e a tela responsavel por fazer o login do jogo
    # Carrego todas as informações e armazeno nas variaveis
    # Após isso passo para o controlador para resalizar as respectivas relaçoes
    # De validação etc
    def __init__(self):

        self.background_menu = Imagem.Imagem.load_image('logar.png', 0)
        self.fonte = pygame.font.SysFont("comicsansms", 23)
        self.seta = Imagem.Imagem.load_image('seta.png', 1)
        self.enviar = self.fonte.render("Enviar", 1, (0, 0, 0))
        self.voltar = self.fonte.render("Voltar", 1, (0, 0, 0))

        self.texto_usuario=""
        self.texto_senha=""

        self.fonte_error = pygame.font.SysFont("comicsansms", 16)
        self.texto_error = "Aperte TAB para mudar"
        self.error = self.fonte_error.render(self.texto_error, 1, (0, 0, 0))

        self.insercao_dados = 1
        self.opcao = 1


        self.usuario=self.fonte.render(self.texto_usuario, 1, (0, 0, 0))
        self.senha=self.fonte.render(self.texto_senha, 1, (0, 0, 0))
        print("called login")

    def mostrar_login(self, game):
        if game.botoes[0]: #cima
            if self.opcao == 1 :
                self.opcao -= 1
        if game.botoes[1]: #baixo
            if self.opcao == 0 :
                self.opcao += 1

        if game.botoes[4]:  # KEY ENTER
            dict={}
            if self.opcao == 0: #Enviar informacoes
                dict["nome"] = self.texto_usuario
                dict["senha"] = self.texto_senha
                return dict, 1
            else:
                return dict, 0

        if game.botoes[6]: #TAB
            if self.insercao_dados == 1 : # estou inserindo o usuario
                self.texto_usuario = game.teclas
                game.teclas = ""

            if self.insercao_dados == 2: # estou inserindo a senha
                self.texto_senha = game.teclas
                game.teclas = ""
                self.insercao_dados = 0

            self.insercao_dados+=1


        game.screen.blit(self.background_menu, (0, 0))

        self.atualiza_dados(game)
        game.screen.blit(self.usuario, (207, 212))
        game.screen.blit(self.senha, (203, 243))

        game.screen.blit(self.enviar, (300, 370))
        game.screen.blit(self.voltar, (300, 400))
        game.screen.blit(self.seta, (275, 400+self.retorna_posicao()))

        self.error = self.fonte_error.render(self.texto_error, 1, (255, 0, 0))
        game.screen.blit(self.error, (270, 320))

        pygame.display.update()
        return (None, 1)

    def retorna_posicao(self):
        return ((self.opcao-1) * 30)+5


    def atualiza_dados(self, game):

        if self.insercao_dados == 1 :
            self.texto_usuario = game.teclas
        elif self.insercao_dados == 2 :
            self.texto_senha = game.teclas

        self.usuario=self.fonte.render(self.texto_usuario, 1, (0, 0, 0))
        self.senha=self.fonte.render(self.texto_senha, 1, (0, 0, 0))

    def update_error(self, game, time):
        loading = Imagem.Imagem.load_image('carregando.png', 0)
        game.screen.blit(loading, (0, 0))
        mensagem = format("%d" % (time/4))
        error = self.fonte_error.render(mensagem, 1, (255, 0, 0))
        game.screen.blit(error, (399, 162))
        pygame.display.update()

    def exibe_mensagem(self, mensagem):
        self.texto_error = mensagem
        self.error = self.fonte_error.render(self.texto_error, 1, (0, 0, 0))


