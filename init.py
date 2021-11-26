import random
import csv
from __init__ import updateField
from visualizer import Visualizer

width = int(input('Input board width: '))
height = int(input('Input board height: '))

herbivores_symbol = input("Input herbivores symbol: ")
animals_symbol = input("Input animals symbol: ")
plants_symbol = input("Input plants symbol: ")

with open('symbols.csv','w+') as symbols_csv:
        csvsymbolsWriter = csv.writer(symbols_csv, delimiter=',')
        csvsymbolsWriter.writerow([herbivores_symbol if(herbivores_symbol != "") else "1", animals_symbol if(animals_symbol != "") else "2", plants_symbol if(plants_symbol != "") else "3"])

def initialize_field(w, h):
    rectangular = []
    if(w > 0 and h > 0):
        for i in range(h):
            rectangular.append([0])
            rectangular[i] = [0] * w
    return rectangular

field = initialize_field(width, height)

def print_field(field):
    print("-- Game board --")
    v = Visualizer()
    v.set_entities(field)
    print(v)

print_field(field)
updateField(field)
print_field(field)
