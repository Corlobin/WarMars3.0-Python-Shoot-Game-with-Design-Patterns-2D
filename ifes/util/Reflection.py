__author__ = 'Ricardo'

class Reflection():
    @staticmethod
    def reflection_builder(inimigoPassado):
        construtorBuilder = "FabricaInimigo" + inimigoPassado + "Builder"
        # Pegando o Builder do inimigo passado
        nome = [construtorBuilder]
        path = "ifes.util." + construtorBuilder
        _temp = __import__(path, fromlist=nome)
        builder = getattr(_temp, construtorBuilder)
        builder = builder()
        return builder
