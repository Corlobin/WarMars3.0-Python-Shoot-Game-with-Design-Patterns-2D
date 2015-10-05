__author__ = 'Ricardo'

import os, pygame
main_dir = os.path.split(os.path.abspath(__file__))[0]

class Som(object):
    Singleton = None
    @staticmethod
    def tocar(sound, musica):

        try:
            diretorio = main_dir.replace("cdp", "")
            path = os.path.join(diretorio, 'dados/sons/', musica)
            if Som.Singleton is None:
                Som.Singleton = sound.Sound(path)
                Som.Singleton.play(-1)

        except pygame.error:
            raise SystemExit('Nao foi possivel carregar o som %s %s ' % (path, pygame.get_error()))
    @staticmethod
    def parar():
        if  Som.Singleton != None :
            Som.Singleton.stop()
            Som.Singleton = None
