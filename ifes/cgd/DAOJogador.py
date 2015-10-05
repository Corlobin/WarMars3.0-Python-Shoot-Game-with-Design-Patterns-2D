__author__ = 'Ricardo'

class DAOJogador():
    @staticmethod
    def insere_jogador(usuario, senha, idade):
        texto = ""
        arquivo = open('../players.txt', 'w+')
        arquivo.writelines(usuario + " " + senha + " " + idade)
        arquivo.close()
        return
    @staticmethod
    def get_jogadores():
        texto = ""
        jogadores = []
        arquivo = open('../players.txt', 'r+')
        for line in arquivo:
            linhas = line.split(" ")
            jogadores.append(linhas[0])
        #print(jogadores)
        arquivo.close()
        return jogadores
