import random
import csv
import math
import time
from plants import Plant
from herbivores import Herbivore
from animals import Animal
from visualizer import Visualizer
from simulator import Simulator
from helpers import exec_iteration

iterations = int(input("Input number of iterations: "))
if(iterations < 0):
    raise ValueError("Iterations must be positive")
g_0 = float(input("Input probability of empty cells(0): "))
g_3 = float(input("Input probability of Plants(3): "))
with open('symbols.csv','r') as my_csv:
        csvreader = csv.reader(my_csv, delimiter=',')
        for row in csvreader:
            if(row != []):
                herbivores_symbol = row[0]
                animals_symbol = row[1]
                plants_symbol = row[2]

def read_csv():
    field = []
    i = 0
    with open('board.csv','r') as my_csv:
        csvreader = csv.reader(my_csv, delimiter=',')
        for row in csvreader:
            if(row != []):
                field.append([])
                for ele in row:
                    if((ele) == '0'): field[i].append(0)
                    elif((ele) == herbivores_symbol): field[i].append(Herbivore())
                    elif((ele) == animals_symbol): field[i].append(Animal())
                    elif((ele) == plants_symbol): field[i].append(Plant())
                i += 1
    return field
field = read_csv()
v = Visualizer()
v.set_entities(field)
g = (g_0, g_3)
simulator = Simulator(v, g)

if(not math.isclose(sum(g[:]), 1.0)):
    raise ValueError('Distribution must be exact for these probabilities')

exec_iteration(field, iterations, g, simulator, v)