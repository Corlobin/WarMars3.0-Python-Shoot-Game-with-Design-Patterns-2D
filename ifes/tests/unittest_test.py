import unittest
from ifes.cdp import Pessoa
from ifes.cgd import DAOJogador

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
      pessoa = Pessoa.Pessoa()
      pessoa.set_nome("Ricardo")
      pessoa.set_idade(13)
      pessoa.set_senha("sahdua123")
      daojogador = DAOJogador.DAOJogador()
      daojogador.inicia_conexao()
      daojogador.insere_jogador(pessoa.toString())
      daojogador.fecha_conexao()
      self.assertEqual(pessoa.toString(), ('ricardo'))




if __name__ == '__main__':
    unittest.main()
