__author__ = 'Ricardo'

import pygame

from ifes.cdp import *

from ifes.cgt import AplGerenciarJogador

class TelaCadastro(object):
    def __init__(self):

        self.background_menu = Imagem.Imagem.load_image('cadastro.png', 0)
        self.fonte = pygame.font.SysFont("comicsansms", 23)
        self.seta = Imagem.Imagem.load_image('seta.png', 1)
        self.enviar = self.fonte.render("Enviar", 1, (0, 0, 0))
        self.voltar = self.fonte.render("Voltar", 1, (0, 0, 0))

        self.texto_usuario=""
        self.texto_senha=""
        self.texto_idade=""

        self.fonte_error = pygame.font.SysFont("comicsansms", 16)
        self.texto_error = "Aperte TAB para mudar"
        self.error = self.fonte_error.render(self.texto_error, 1, (0, 0, 0))

        self.insercao_dados = 1
        self.opcao = 1


        self.usuario=self.fonte.render(self.texto_usuario, 1, (0, 0, 0))
        self.senha=self.fonte.render(self.texto_senha, 1, (0, 0, 0))
        self.idade=self.fonte.render(self.texto_idade, 1, (0, 0, 0))


    def mostrar_cadastro(self, game):
        if game.botoes[0]: #cima
            if self.opcao == 1 :
                self.opcao -= 1
        if game.botoes[1]: #baixo
            if self.opcao == 0 :
                self.opcao += 1

        if game.botoes[4]:  # KEY ENTER
            if self.opcao == 0: #Enviar informacoes
                self.texto_error = " "
                if len(self.texto_usuario) < 5:
                    self.texto_error += "Nome tem que ter no minimo 5 caracteres."
                    self.error = self.fonte_error.render(self.texto_error, 1, (0, 0, 0))

                elif len(self.texto_senha) < 5:
                    self.texto_error += "Senha tem que ter no minimo 5 caracteres."
                    self.error = self.fonte_error.render(self.texto_error, 1, (0, 0, 0))
                elif len(self.texto_idade) < 1:
                    self.texto_error += "Digite uma idade!"
                    self.error = self.fonte_error.render(self.texto_error, 1, (0, 0, 0))
                else:
                    self.texto_error = "Cadastrado com sucesso!"
                    self.error = self.fonte_error.render(self.texto_error, 1, (0, 0, 0))
                    AplGerenciarJogador.AplGerenciarJogador.cadastra_jogador(self.texto_usuario, self.texto_senha, self.texto_idade)



            else:
                game.status = 20
        if game.botoes[6]:
            if self.insercao_dados == 1 : # estou inserindo o usuario
                if len(self.texto_usuario) < 5 :
                    self.texto_error = "Aperte TAB para mudar"
                else:
                    self.insercao_dados = 2
                    self.texto_usuario = game.teclas
                    game.teclas = ""

            if self.insercao_dados == 2: # estou inserindo a senha
                if len(self.texto_senha) < 5:
                    print("Insira mais que 5 caracteres!!!!")
                else:
                    self.insercao_dados = 3
                    self.texto_senha = game.teclas
                    game.teclas = ""

            if self.insercao_dados == 3 : # estou inserindo a idade
                if len(self.texto_idade) < 1:
                    print("Insira mais que 1 caracter!!!!")
                else:
                    self.insercao_dados = 1
                    self.texto_idade = game.teclas
                    game.teclas = ""



        game.screen.blit(self.background_menu, (0, 0))

        self.atualiza_dados(game)
        game.screen.blit(self.usuario, (207, 212))
        game.screen.blit(self.senha, (203, 243))
        game.screen.blit(self.idade, (203, 270))

        game.screen.blit(self.enviar, (300, 370))
        game.screen.blit(self.voltar, (300, 400))
        game.screen.blit(self.seta, (275, 400+self.retorna_posicao()))
        #game.screen.blit(self.seta, (275, 405))

        self.error = self.fonte_error.render(self.texto_error, 1, (255, 0, 0))
        game.screen.blit(self.error, (270, 320))

        self.fps = 10
        pygame.display.update()
        return
    def retorna_posicao(self):
        return ((self.opcao-1) * 30)+5

    def atualiza_dados(self, game):
        if self.insercao_dados == 1 :
            self.texto_usuario = game.teclas
        elif self.insercao_dados == 2 :
            self.texto_senha = game.teclas
        elif self.insercao_dados == 3 :
            self.texto_idade = game.teclas

        self.usuario=self.fonte.render(self.texto_usuario, 1, (0, 0, 0))
        self.senha=self.fonte.render(self.texto_senha, 1, (0, 0, 0))
        self.idade=self.fonte.render(self.texto_idade, 1, (0, 0, 0))


