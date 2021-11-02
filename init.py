import random
import csv
from __init__ import updateField

width = int(input('Input board width: '))
height = int(input('Input board height: '))

def initialize_field(w, h):
    rectangular = []
    if(w > 0 and h > 0):
        for i in range(h):
            rectangular.append([0])
            rectangular[i] = [0] * w
    return rectangular

field = initialize_field(width, height)

def print_field(field):
    w_str = ""
    print("-- Game board --")
    for i in range(len(field)):
        for j in range(len(field[i])):
            w_str += "[" + str(field[i][j]) + "]"
        w_str += "\n"
    print(w_str)
    with open('board.csv','w+') as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(field)
    return w_str

print_field(field)
updateField(field)
print_field(field)
