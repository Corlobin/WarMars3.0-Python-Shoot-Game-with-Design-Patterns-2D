__author__ = 'Ricardo'

import os
import pygame


main_dir = os.path.split(os.path.abspath(__file__))[0]


class Imagem(object):

    @staticmethod
    def load_image(name, transparent):
        diretorio = main_dir.replace("cdp", "")
        path = os.path.join(diretorio, 'dados/imagens/', name)
        print(path)
        try:
            surface = pygame.image.load(path)

        except pygame.error:
            raise SystemExit('Nao foi possivel carregar a imagem %s %s ' % (path, pygame.get_error()))


        if transparent:
            corner = surface.get_at((0, 0))
            surface.set_colorkey(corner, pygame.RLEACCEL)


        print(surface)
        return surface.convert()
