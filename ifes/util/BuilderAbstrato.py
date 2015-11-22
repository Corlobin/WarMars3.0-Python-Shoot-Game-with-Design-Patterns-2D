__author__ = 'Ricardo'

from ifes.cdp.Inimigo import Inimigo
class BuilderAbstrato:
    def __init__(self, fabrica):
        self.inimigo = Inimigo()
        self.fabrica = fabrica

    def prepararImagem(self):
        self.inimigo.set_imagem(self.fabrica.criarImagem())
    def prepararPontuacao(self):
        self.inimigo.set_pontuacao(self.fabrica.criarPontuacao())
    def inicializarInimigo(self):
        return self.inimigo
