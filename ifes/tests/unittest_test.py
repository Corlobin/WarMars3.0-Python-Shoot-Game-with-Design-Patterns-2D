import importlib
import unittest
import pygame
from ifes.cdp import Pessoa
from ifes.cgd import DAOJogador
from ifes.cgd import Error
from ifes.cih import TelaLogin
from ifes.cgd import Imagem

from ifes.cdp import Helicoptero
from ifes.cdp import Municao
from ifes.util.FabricaInimigo import FabricaInimigo

from ifes.cdp.Inimigo import Inimigo
class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

    def test_salvarusuario(self):
        try:
            pessoa = Pessoa.Pessoa()
            pessoa.set_nome("Ricardo")
            pessoa.set_idade(13)
            pessoa.set_senha("sahdua123")
            daojogador = DAOJogador.DAOJogador()
            daojogador.inicia_conexao()
            daojogador.insere_jogador(pessoa.toString())
            daojogador.fecha_conexao()
        except Error.Error as m:
            print(m.msg)
        except Exception as e:
            print(e.args[0])

        self.assertEqual(pessoa.toString(), ('ricardo'))

    def testa_loading(self):
        pygame.init()
        pygame.font.init()
        pygame.mouse.set_visible(True)
        screen = pygame.display.set_mode((640, 480))
        waiting = 0
        fonte_error = pygame.font.SysFont("comicsansms", 16)
        while waiting <= 400:
            loading = Imagem.Imagem.load_image('carregando.png', 0)
            screen.blit(loading, (0, 0))
            mensagem = format("%d" % (waiting/4))
            error = fonte_error.render(mensagem, 1, (255, 0, 0))
            screen.blit(error, (399, 162))
            pygame.display.update()
            waiting += 1

    def test_imagem_sequencias(self):
        pygame.init()
        pygame.font.init()
        pygame.mouse.set_visible(True)
        screen = pygame.display.set_mode((640, 480))

        while True:
            screen.fill((0,0,0))
            imagem = Imagem.Imagem.load_image("imagens_player.png", 1)
            x_de_cada_imagem = 30
            y_de_cada_imagem = 31
            calculo1 = (0*30+0)
            calculo2 = (2*30+6)
            calculo3 = (3*30+9)
            calculo4 = (4*30+12)
            calculo5 = (5*30+15)
            calculo6 = (6*30+18)
            calculo7 = (7*30+21)
            calculo8 = (8*30+24)
            calculo9 = (9*30+27)
            calculo10 = (10*30+30)
            calculo11 = (11*30+33)
            calculo12 = (12*30+36)

            # Primeiro do de baixo:
            # 30 + 3
            # Segundo
            # 60 + 6
            # Terceiro
            # 90 + 9
            # Quarto
            # 120 + 12
            # Quinto
            # 150 + 15

            screen.blit(imagem, (0, 0), (calculo1, 0, x_de_cada_imagem, y_de_cada_imagem))
            screen.blit(imagem, (0, 40), (calculo2, 0, x_de_cada_imagem, y_de_cada_imagem))
            screen.blit(imagem, (0, 80), (calculo3, 0, x_de_cada_imagem, y_de_cada_imagem))
            screen.blit(imagem, (000, 120), (calculo4, 0, x_de_cada_imagem, y_de_cada_imagem))
            screen.blit(imagem, (000, 160), (calculo5, 0, x_de_cada_imagem, y_de_cada_imagem))
            screen.blit(imagem, (000, 200), (calculo6, 0, x_de_cada_imagem, y_de_cada_imagem))
            screen.blit(imagem, (000, 240), (calculo7, 0, x_de_cada_imagem, y_de_cada_imagem))
            screen.blit(imagem, (000, 280), (calculo8, 0, x_de_cada_imagem, y_de_cada_imagem))
            screen.blit(imagem, (000, 320), (calculo9, 0, x_de_cada_imagem, y_de_cada_imagem))
            screen.blit(imagem, (000, 360), (calculo10, 0, x_de_cada_imagem, y_de_cada_imagem))
            screen.blit(imagem, (000, 400), (calculo11,0, x_de_cada_imagem, y_de_cada_imagem))
            screen.blit(imagem, (000, 440), (calculo12,0, x_de_cada_imagem, y_de_cada_imagem))

            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # ESC
                        pygame.quit()


    def test_shoot_helicoptero(self):
        pygame.init()
        pygame.font.init()
        pygame.mouse.set_visible(True)
        screen = pygame.display.set_mode((640, 480))
        clock = pygame.time.Clock()
        helicoptero = Helicoptero.Helicoptero("aviao.png", 10)
        inimigo = Inimigo()
        inimigo.rect.y = 10


        sprites_list = pygame.sprite.Group()
        helicoptero_sprite = pygame.sprite.Group()
        inimigos_list = pygame.sprite.Group()


        sprites_list.add(helicoptero)
        sprites_list.add(inimigo)

        helicoptero_sprite.add(helicoptero)
        inimigos_list.add(inimigo)

        while True:
            screen.fill((255,255,255))

            #quadrado = pygame.draw.rect(screen, (0,0,0), (500,30,20,20), 0)
            #sprites.add(quadrado)

            #print('Colisao helicoptero x inimigo: %s' % result1)

            #print('Colisao municao x inimigo: %s' % result2)

            #print('Colisao municao x inimigo: %s' % result2)
            result1 = pygame.sprite.groupcollide(helicoptero_sprite, inimigos_list, True, False)
            result2 = pygame.sprite.groupcollide(helicoptero.municoes_list, inimigos_list, False, True)
            for inimigo in inimigos_list:
                result3 = pygame.sprite.groupcollide(helicoptero_sprite, inimigo.municoes_list, True, False)
                if result3:
                    print("GAME OVER")


            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # ESC
                        pygame.quit()
                    if event.key == pygame.K_SPACE:
                        helicoptero.atirar()
            clock.tick(15)


            sprites_list.update()
            for sprite in sprites_list:
                sprite.draw(screen)

            pygame.display.update()

    def testa_salvar(self):
        try:

            pessoa = Pessoa.Pessoa()
            pessoa.set_nome("Velhote")
            pessoa.set_idade(13)
            pessoa.set_senha("sahdua123")
            daojogador = DAOJogador.DAOJogador()
            daojogador.inicia_conexao()
            #daojogador.insere_jogador(pessoa.toString())
            print(daojogador.get_jogadores())


            pessoa.set_highscore(100)
            print(pessoa.get_highscore())
            daojogador.salvar_jogador(pessoa)

            print(daojogador.get_jogadores())

            daojogador.fecha_conexao()

        except Error.Error as m:
            print(m.msg)
        except Exception as e:
            print(e.args[0])

    def testa_fabrica(self):
        inimigo = FabricaInimigo.criar_inimigo()
        print(inimigo.pontuacao)
        print(inimigo.image)

    def testa_reflection2(self, nome):
        nome = [nome]
        path = "ifes.cdp." + nome
        _temp = __import__(path, fromlist=nome)
        inimigo = getattr(_temp, nome)
        inimigo = inimigo()
        print(inimigo)

    def testa_reflection(self):
        nome = ['Inimigo']
        path = "ifes.cdp.Inimigo"
        #_temp = __import__(path, fromlist=nome)
        #inimigo = _temp.Inimigo
        #inimigo = inimigo()

    def testa_fabrica(self):

        pygame.init()
        pygame.font.init()
        pygame.mouse.set_visible(True)
        screen = pygame.display.set_mode((640, 480))
        clock = pygame.time.Clock()
        inimigo = FabricaInimigo.criar_inimigo()

        while True:
            screen.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:  # ESC
                        pygame.quit()
            clock.tick(15)


            inimigo.update()
            pygame.display.update()



if __name__ == '__main__':
    unittest.main()
