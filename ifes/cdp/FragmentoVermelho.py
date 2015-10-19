__author__ = 'Ricardo'

 class RedFragment(Fragment):
        """explodes outward from (killed) Bird"""
        def __init__(self,pos):
            self.groups = allgroup, fragmentgroup, gravitygroup
            Fragment.__init__(self,pos)
            #red-only part -----------------------------
            self.color = (random.randint(25,255),0,0) # red
            self.pos[0] = pos[0]
            self.pos[1] = pos[1]
            self.dx = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)
            self.dy = random.randint(-self.fragmentmaxspeed,self.fragmentmaxspeed)
            self.lifetime = 1 + random.random()*3 # max 3 seconds
            self.init2() # continue with generic Fragment class
            self.mass = 48.0