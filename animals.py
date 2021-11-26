import csv

class Animal:

    eaten = 0
    dead = True

    def __init__(self):
        with open('symbols.csv','r') as my_csv:
            csvreader = csv.reader(my_csv, delimiter=',')
            for row in csvreader:
                if(row != []):
                    animals_symbol = row[1]
            self.dead = False
            self.symbol = animals_symbol if(animals_symbol != '') else "2"
    def __str__(self):
        return self.symbol
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
