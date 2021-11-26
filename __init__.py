import random
import math
import csv
from plants import Plant
from herbivores import Herbivore
from animals import Animal

def updateField(field):

    with open('symbols.csv','r') as my_csv:
        csvreader = csv.reader(my_csv, delimiter=',')
        for row in csvreader:
            if(row != []):
                herbivores_symbol = row[0]
                animals_symbol = row[1]
                plants_symbol = row[2]

    p_0 = float(input("Input probability for free cell(0): "))
    p_1 = float(input("Input probability for herbivores({}): ".format(herbivores_symbol)))
    p_2 = float(input("Input probability for carnivores({}): ".format(animals_symbol)))
    p_3 = float(input("Input probability for plants({}): ".format(plants_symbol)))
    length = len(field)
    p = (p_0, p_1, p_2, p_3)
    if(p[-1] >= 1):
        raise ValueError('Plants probability more or equal to 1')
    if(not math.isclose(sum(p[:-1]), 1.0)):
        raise ValueError('Distribution for First three probabilities')
    for i in range(len(field)):
        for j in range(len(field[i])):
            field[i][j] = random.choices([0, Herbivore(), Animal() ,Plant()], p)[0]
