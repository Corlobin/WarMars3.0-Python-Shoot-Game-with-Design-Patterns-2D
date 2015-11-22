__author__ = 'Ricardo'
class Desenvolvedor():
    def criar_inimigo(self, builder_ajudante):
        builder_ajudante.prepararImagem()
        builder_ajudante.prepararPontuacao()
        inimigo = builder_ajudante.inicializarInimigo()
        return inimigo

