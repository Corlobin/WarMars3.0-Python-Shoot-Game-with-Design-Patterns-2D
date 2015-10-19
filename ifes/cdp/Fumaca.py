__author__ = 'Ricardo'
import random
from ifes.cdp import Fragmento
class Smoke(Fragment):
        """black exhaust indicating that the BigBird sprite is moved by
           the player. Exhaust direction is inverse of players movement direction"""
        def __init__(self, pos, dx, dy):
           self.color = ( random.randint(1,50), random.randint(1,50), random.randint(1,50) )
           self.groups = allgroup
           Fragment.__init__(self,pos, 3) # give startpos and layer
           self.pos[0] = pos[0]
           self.pos[1] = pos[1]
           self.lifetime = 1 + random.random()*2 # max 3 seconds
           Fragment.init2(self)
           self.smokespeed = 120.0 # how fast the smoke leaves the Bird
           self.smokearc = .3 # 0 = thin smoke stream, 1 = 180 Degrees
           arc = self.smokespeed * self.smokearc
           self.dx = dx * self.smokespeed + random.random()*2*arc - arc
           self.dy = dy * self.smokespeed + random.random()*2*arc - arc
