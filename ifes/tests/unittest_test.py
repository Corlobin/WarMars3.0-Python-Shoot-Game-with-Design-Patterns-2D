import unittest
import pygame
from ifes.cdp import Pessoa
from ifes.cgd import DAOJogador
from ifes.cgd import Error
from ifes.cih import TelaLogin
from ifes.cgd import Imagem

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


if __name__ == '__main__':
    unittest.main()
