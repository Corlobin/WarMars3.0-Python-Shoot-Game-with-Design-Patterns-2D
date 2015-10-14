__author__ = 'Ricardo'
import sqlite3 as lite

class DAOJogador(object):
    def __init__(self):
        try:
            self.con = lite.connect('usuarios.db')
        except lite.Error as e:
            print("Error ao conectar com o banco " + e)

    def inicia_conexao(self):
        try:
            cur = self.con.cursor()
            cur.executescript("CREATE TABLE IF NOT EXISTS Pessoa(Id_Pessoa INTEGER PRIMARY KEY AUTOINCREMENT, Data_criado TIMESTAMP, Nome TEXT, Senha TEXT, Idade INTEGER, Highscore INTEGER, Imagem TEXT, TempoJogo INTEGER, Tiros INTEGER, Percas INTEGER);");
            self.con.commit()

        except lite.Error as e:
            if self.con:
                self.con.rollback()

            print("Error " + e)

    def insere_jogador(self, pessoa):
        try:
            lista = []
            lista.append(pessoa)
            print(lista)
            cur = self.con.cursor()
            cur.executemany("INSERT INTO Pessoa (Data_criado, Nome, Senha, Idade, Highscore, Imagem, TempoJogo, Tiros, Percas) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", lista)
            self.con.commit()

        except lite.Error as e:
            if self.con:
                self.con.rollback()
            print("Error ao tentar inserir %s:" % e)


        return

    def get_jogadores(self):
        jogadores = []
        print('Before...: ' + jogadores)
        try:
            cur = self.con.cursor()
            cur.execute(""" SELECT Nome, Highscore FROM Pessoa ORDER BY highscore LIMIT 10 """)
            for linha in cur.fetchall():
                print(linha)
                jogadores.append(linha)
            print(jogadores)

        except Exception as e:
            print(e)


        return jogadores

    def fecha_conexao(self):
        if self.con:
            self.con.close()
