import random
import csv
import math
import time

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
    field = herbivores_behavior(field)
    time.sleep(0.5)
    return field

def herbivores_behavior(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if(field[i][j] == 1):
                #Top cell
                if(i - 2 < 0): t_cell = 0
                else: t_cell = i-2
                #Right cell
                if(j + 3 >= len(field[i])): r_cell = len(field[i])
                else: r_cell = j + 3
                #Bottom cell
                if(i + 3 >= len(field)): b_cell = len(field)
                else: b_cell = i + 3
                #Left cell
                if(j - 2 < 0): l_cell = 0
                else: l_cell = j - 3

                plants = 0
                herbivorous = 0
                for k in range(t_cell, b_cell):
                    for l in range(l_cell, r_cell):
                        if (i, j) != (k, l):
                            if(field[k][l] == 3): plants += 1
                            elif(field[k][l] == 1): herbivorous += 1
                if herbivorous >= 1 and plants >= 4:
                    plants =4
                    herbivorous = 1
                    x = random.randrange(t_cell, b_cell)
                    y =  random.randrange(l_cell, r_cell)
                    while plants or herbivorous:
                        if((field[x][y] == 3) and plants):
                            field[x][y] = 0
                            plants -= 1
                        elif((field[x][y] == 0) and herbivorous):
                            field[x][y] = 1
                            herbivorous -= 1
                        x = random.randrange(t_cell, b_cell)
                        y = random.randrange(l_cell, r_cell)
            else:
                continue
    return field 

def print_iter(field, n):
    print("Borad number {0}: ".format(n+1))
    for i in range(len(field)):
        for j in range(len(field[i])):
            print("[{0}]".format(field[i][j]), end='')
        print()
    print()

exec_iteration(field, iterations, g)