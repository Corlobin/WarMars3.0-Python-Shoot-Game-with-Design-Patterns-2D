__author__ = 'Ricardo'
class Bullet(Fragment):
        """a bullet flying in the direction of the BigBird's heading. May
           be subject to gravity"""
        def __init__(self, boss, dx, dy):
            self.color = (200,0,200)
            self.boss = boss
            self.groups = allgroup, bulletgroup, gravitygroup
            Fragment.__init__(self, self.boss.rect.center, 3) # layer behind Bird
            self.pos[0] = self.boss.pos[0]
            self.pos[1] = self.boss.pos[1]
            self.lifetime = 5 # 5 seconds
            self.image = pygame.Surface((4,20))
            self.image.set_colorkey((0,0,0)) # black transparent
            pygame.draw.rect(self.image, self.color, (0,0,4,20) )
            pygame.draw.rect(self.image, (10,0,0), (0,0,4,4)) # point
            self.image = self.image.convert_alpha()
            self.image0 = self.image.copy()
            self.rect = self.image.get_rect()
            self.rect.center = self.boss.rect.center
            self.image = pygame.transform.rotate(self.image, self.boss.angle)
            self.rect = self.image.get_rect()
            self.rect.center = self.boss.rect.center
            self.time = 0.0
            self.bulletspeed = 250.0 # pixel per second ?
            self.bulletarc = 0.05 # perfect shot has 0.0
            arc = self.bulletspeed * self.bulletarc
            self.dx = dx * self.bulletspeed + random.random()*2*arc -arc
            self.dy = dy * self.bulletspeed + random.random()*2*arc -arc
            self.mass = 25.0
            self.angle = self.boss.angle

        def update(self, time):
            Fragment.update(self,time)
            #--------- rotate into direction of movement ------------
            self.angle = math.atan2(-self.dx, -self.dy)/math.pi*180.0
            self.image = pygame.transform.rotozoom(self.image0,self.angle,1.0)