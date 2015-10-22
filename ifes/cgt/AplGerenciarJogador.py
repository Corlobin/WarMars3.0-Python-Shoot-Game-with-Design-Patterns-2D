__author__ = 'Ricardo'

from ifes.cgd import DAOJogador
from ifes.cdp import Pessoa
from ifes.cgd import Error
class AplGerenciarJogador():
    @staticmethod
    def cadastra_jogador(pessoa_dados):

        try:
            nome = pessoa_dados["nome"]
            idade = int(pessoa_dados["idade"])
            senha = pessoa_dados["senha"]

            pessoa = Pessoa.Pessoa()
            pessoa.set_nome(nome)
            pessoa.set_idade(idade)
            pessoa.set_senha(senha)

            daojogador = DAOJogador.DAOJogador()
            daojogador.inicia_conexao()
            daojogador.insere_jogador(pessoa.toString())
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

    @staticmethod
    def logar_jogador(pessoa_dados):

        try:
            print(pessoa_dados)
            nome = pessoa_dados["nome"]
            senha = pessoa_dados["senha"]
            if nome == '':
                raise Error.Error('Insira um nome')
            elif senha == '':
                raise Error.Error('Insira uma senha')

            daojogador = DAOJogador.DAOJogador()
            daojogador.inicia_conexao()
            dados = daojogador.logar_jogador(nome, senha)
            daojogador.fecha_conexao()


            pessoa = Pessoa.Pessoa()
            pessoa.set_id(dados[0])
            pessoa.set_data_criacao(dados[1])
            pessoa.set_nome(dados[2])
            pessoa.set_senha(dados[3])
            pessoa.set_idade(dados[4])
            pessoa.set_highscore(dados[5])
            pessoa.set_imagem(dados[6])
            pessoa.set_tempojogo(dados[7])
            pessoa.set_tempojogo(dados[8])
            pessoa.set_percas(dados[9])

        except Error.Error as detalhe:
            raise Error.Error(detalhe.msg)

        except ValueError:
            raise Error.Error('Idade tem que ser numero!')

        return pessoa
    @staticmethod
    def salvar_jogador(pessoa):

        try:
            daojogador = DAOJogador.DAOJogador()
            daojogador.inicia_conexao()
            daojogador.salvar_jogador(pessoa)
            daojogador.fecha_conexao()
        except Error.Error as detalhe:
            raise Error.Error(detalhe.msg)

        return

