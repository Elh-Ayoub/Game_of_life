import csv

class Plant:

    dead = True

    def __init__(self):
        with open('symbols.csv','r') as my_csv:
            csvreader = csv.reader(my_csv, delimiter=',')
            for row in csvreader:
                if(row != []):
                    plants_symbol = row[2]
            self.dead = False
            self.symbol = plants_symbol if(plants_symbol != '') else "3"
    def __str__(self):
        return self.symbol
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

# plant = Plant()
# print(plant.isAlive())
# plant.kill()
# print(plant.isAlive())
# print(plant.coordinates())
