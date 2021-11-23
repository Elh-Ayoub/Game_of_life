class Animal:

    eaten = 0
    dead = True
    x = None
    y = None

    def __init__(self):
        self.dead = False

    def isDead(self):
        return self.dead
    def isAlive(self):
        return not self.dead
    def kill(self):
        self.dead = True
    def eat(self):
        if(self.isDead()):
            raise SyntaxError("Animal is dead!!")
        else:
            self.eaten += 1
    def coordinates(self):
        if(not isinstance(self.x, int) or  not isinstance(self.y, int)):
            raise TypeError("Coordinates must be type int")
        else:
            return [self.x, self.y]
