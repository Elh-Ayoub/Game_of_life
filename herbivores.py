class Herbivore:

    dead = True
    x = None
    y = None

    def __init__(self):
        self.dead = False
    def isDead(self):
        return self.dead
    def kill(self):
        self.dead = True
    def isAlive(self):
        return not self.dead
    def coordinates(self):
        if(not isinstance(self.x, int) or  not isinstance(self.y, int)):
            raise TypeError("Coordinates must be type int")
        else:
            return [self.x, self.y]

