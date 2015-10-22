__author__ = 'Ricardo'

import sqlite3 as lite
from ifes.cgd import Error

class DAOJogador(object):
    def __init__(self):
        try:
            self.con = lite.connect('usuarios.db')
        except lite.Error as e:
            print("Error ao conectar com o banco " + e)

    def inicia_conexao(self):
        try:
            cur = self.con.cursor()
            cur.executescript("CREATE TABLE IF NOT EXISTS Pessoa(Id_Pessoa INTEGER PRIMARY KEY AUTOINCREMENT, Data_criado TIMESTAMP, Nome TEXT UNIQUE, Senha TEXT, Idade INTEGER, Highscore INTEGER, Imagem TEXT, TempoJogo INTEGER, Tiros INTEGER, Percas INTEGER);");
            self.con.commit()

        except lite.Error as e:
            if self.con:
                self.con.rollback()

            print("Error " + e)

    def insere_jogador(self, pessoa):
        try:
            lista = []
            lista.append(pessoa)
            cur = self.con.cursor()
            cur.executemany("INSERT INTO Pessoa (Data_criado, Nome, Senha, Idade, Highscore, Imagem, TempoJogo, Tiros, Percas) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", lista)
            self.con.commit()

        except lite.IntegrityError:

            if self.con:
                self.con.rollback()
            error = Error.Error('Ja existe alguem com esse usuario')
            raise error

        except Exception as e:
            if self.con:
                self.con.rollback()
            error = Error.Error('Ocorreu um erro com o banco de dados')
            raise error


        return

    def get_jogadores(self):
        jogadores = []
        try:
            cur = self.con.cursor()
            cur.execute(""" SELECT Nome, Highscore FROM Pessoa ORDER BY Highscore DESC LIMIT 10""")
            for linha in cur.fetchall():
                print(linha)
                jogadores.append(linha)
            print(jogadores)

        except Exception as e:
            print(e)


        return jogadores

    def logar_jogador(self, nome, senha):
        data = None
        try:
            lst=[nome, senha]
            cur = self.con.cursor()
            cur.execute(""" SELECT * FROM Pessoa WHERE Nome = ? AND Senha = ? """, lst)
            data = cur.fetchone()

            if data == None:
                if self.con:
                    self.con.close()
                raise Error.Error('Usuario inexistente')

        except Error.Error as e:
            raise Error.Error(e.msg);
        except Exception:
            raise Error.Error('Error com o banco de dados');

        return data

    def salvar_jogador(self, pessoa):
        try:
            lst=[pessoa.get_highscore(), pessoa.get_tiros(), pessoa.get_percas(), pessoa.get_id()]
            cur = self.con.cursor()
            cur.execute(""" UPDATE Pessoa SET Highscore = ?, Tiros = ?, Percas = ? WHERE Id_Pessoa = ?""", lst)
            self.con.commit()

        except Error.Error as e:
            raise Error.Error(e.msg);
        except Exception as e:
            raise Error.Error('Error com o banco de dados ' + e[0]);


    def fecha_conexao(self):
        if self.con:
            self.con.close()
