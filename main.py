import random
import csv
import math

def read_csv():
    field = []
    i = 0
    with open('board.csv','r') as my_csv:
        csvreader = csv.reader(my_csv, delimiter=',')
        for row in csvreader:
            if(row != []):
                field.append([])
                for ele in row:
                    field[i].append(int(ele))
                i += 1
    return field
field = read_csv()

iterations = int(input("Input number of iterations: "))
g_0 = float(input("Input probability of empty cells(0): "))
g_3 = float(input("Input probability of Plants(3): "))

g = (g_0, g_3)
if(not math.isclose(sum(g[:]), 1.0)):
    raise ValueError('Distribution must be exact for these probabilities')

def exec_iteration(field, iterations, g):
    for i in range(iterations):
            field = exec_rand(field, g)
            print_iter(field, i)
    return 0

def exec_rand(field, g):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if(field[i][j] == 0 or field[i][j] == 3):
                x = random.choices([0, 3], g)[0]
                field[i][j] = x
    return field

def print_iter(field, n):
    print("Borad number {0}: ".format(n+1))
    for i in range(len(field)):
        for j in range(len(field[i])):
            print("[{0}]".format(field[i][j]), end='')
        print()
    print()

exec_iteration(field, iterations, g)