import random
import math
def updateField(field):
    p_0 = float(input("Input probability for free cell(0): "))
    p_1 = float(input("Input probability for herbivores(1): "))
    p_2 = float(input("Input probability for carnivores(2): "))
    p_3 = float(input("Input probability for plants(3): "))
    length = len(field)
    p = (p_0, p_1, p_2, p_3)
    if(p[-1] >= 1):
        raise ValueError('Plants probability more or equal to 1')
    if(not math.isclose(sum(p[:-1]), 1.0)):
        raise ValueError('Distribution for First three probabilities')
    for i in range(len(field)):
        for j in range(len(field[i])):
            field[i][j] = random.choices([0, 1, 2 ,3], p)[0]
