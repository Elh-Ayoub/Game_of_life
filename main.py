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
if(iterations < 0):
    raise ValueError("Iterations must be positive")
g_0 = float(input("Input probability of empty cells(0): "))
g_3 = float(input("Input probability of Plants(3): "))

g = (g_0, g_3)
if(not math.isclose(sum(g[:]), 1.0)):
    raise ValueError('Distribution must be exact for these probabilities')

def exec_iteration(field, iterations, g):
    for i in range(iterations):
        field = exec_rand(field, g, i+1)
        print_iter(field, i)
    with open('board.csv','w+') as my_csv:
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(field)
    return 0

def exec_rand(field, g, iterations):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if(field[i][j] == 0 or field[i][j] == 3):
                x = random.choices([0, 3], g)[0]
                field[i][j] = x
    field = herbivores_behavior(field)
    field = predators_behavior(field, iterations)
    time.sleep(0.5)
    return field

def herbivores_behavior(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if(field[i][j] == 1):
                #Top cell
                if(i - 1 < 0): t_cell = 0
                else: t_cell = i-1
                #Right cell
                if(j + 2 >= len(field[i])): r_cell = len(field[i])
                else: r_cell = j + 2
                #Bottom cell
                if(i + 2 >= len(field)): b_cell = len(field)
                else: b_cell = i + 2
                #Left cell
                if(j - 1 < 0): l_cell = 0
                else: l_cell = j - 1

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

def predators_behavior(field, iterations):
    eaten = []
    for i in range(len(field)):
        eaten.append([])
        for j in range(len(field[i])):
            eaten[i].append([False, 0])
    for i in range(len(field)):
        for j in range(len(field[i])):
            if(field[i][j] == 2):
                #Top cell
                if(i - 2 < 0): t_cell = 0
                else: t_cell = i - 2
                #Right cell
                if(j + 3 >= len(field[i])): r_cell = len(field[i])
                else: r_cell = j + 3
                #Bottom cell
                if(i + 3 >= len(field)): b_cell = len(field)
                else: b_cell = i + 3
                #Left cell
                if(j - 2 < 0): l_cell = 0
                else: l_cell = j - 2

                predators = 0
                herbivorous = 0
                eaten[i][j] = [False, iterations]
                for k in range(t_cell, b_cell):
                    for l in range(l_cell, r_cell):
                        if (i, j) != (k, l):
                            if(field[k][l] == 2): predators += 1
                            elif(field[k][l] == 1): herbivorous += 1
                if(herbivorous >= 1):
                    herbivorous_in_A = 1
                    eaten[i][j] = [True, iterations]
                    if(predators >= 1 and herbivorous >=2):
                        herbivorous_in_A = 2
                    x = random.randrange(t_cell, b_cell)
                    y = random.randrange(l_cell, r_cell)
                    while(herbivorous_in_A != 0):
                        if(field[x][y] == 1 and herbivorous_in_A):
                            if(herbivorous_in_A == 2): field[x][y] = 2
                            else: field[x][y] = 0
                            herbivorous_in_A -= 1
                        x = random.randrange(t_cell, b_cell)
                        y = random.randrange(l_cell, r_cell)
                if(not eaten[i][j][0]):
                    if(eaten[i][j][1] > 5):
                        field[i][j] = 3
                    else:
                        m_top = 0 if i - 2 < 0 else i - 2
                        m_bottom = len(field) if i + 3 >= len(field) else i + 3
                        m_left = 0 if j - 2 < 0 else j - 2
                        m_right = len(field[i]) if j + 3 >= len(field[i]) else j + 3
                        all_herbivorous = []
                        for m in range(m_top, m_bottom):
                            for n in range(m_left, m_right):
                                if (i, j) != (m, n):
                                    if field[m][n] == 1:
                                        all_herbivorous.append((m, n))
                        lengths = []
                        if(len(all_herbivorous) > 0):
                            for element in all_herbivorous:
                                lengths.append([(i, j), math.sqrt((element[0]-i)**2+(element[1]-j)**2)])
                            closest_lengths = sorted(lengths, key=lambda x: x[1], reverse=True)
                            for item in closest_lengths:
                                t_close = m_top if item[0] - 1 < m_top else item[0] - 1
                                b_close = m_bottom if item[0] + 2 >= m_bottom else item[0] + 2
                                l_close = m_left if item[1] - 1 < m_left else item[1] - 1
                                r_close = m_right if item[1] + 2 >= m_right else item[1] + 2
                                for m in range(t_close, b_close):
                                    for n in range(l_close, r_close):
                                        if field[m][n] == 0:
                                            field[m][n] = 2
                                            field[i][j] = 0
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