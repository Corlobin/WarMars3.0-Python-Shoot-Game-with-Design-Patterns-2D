__author__ = 'Ricardo'

from ifes.cgd import DAOJogador
from ifes.cdp import Pessoa
from ifes.cgd import Error
class AplGerenciarJogador():
    @staticmethod
    def cadastra_jogador(pessoa):
        print("Entrando na parte do cadastra jogador")

        objeto = Pessoa.Pessoa()
        try:
            nome = pessoa["nome"]
            idade = int(pessoa["idade"])
            senha = pessoa["senha"]

            print(nome, idade, senha)
            objeto.set_nome(nome)
            objeto.set_idade(idade)
            objeto.set_senha(senha)
            daojogador = DAOJogador.DAOJogador()
            daojogador.inicia_conexao()
            daojogador.insere_jogador(objeto)
            daojogador.fecha_conexao()


        except Error.Error as detalhe:
            raise Error.Error(detalhe.msg)

        except ValueError:
            raise Error.Error('Idade tem que ser numero!')


        return
    @staticmethod
    def retorna_jogadores():
        daojogador = DAOJogador.DAOJogador()
        return daojogador.get_jogadores()

