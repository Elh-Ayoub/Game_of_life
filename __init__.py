import random
import math
def updateField(field):
    p_0 = float(input("Input probability for free cell(0): "))
    p_1 = float(input("Input probability for herbivores(1): "))
    p_2 = float(input("Input probability for carnivores(2): "))
    p_3 = float(input("Input probability for plants(3): "))
    length = len(field)
    p = (p_0, p_1, p_2, p_3)
    if(not math.isclose(sum(p[:-1]), 1.0)):
        raise ValueError('Distribution for First three probabilities')
    x = random.randrange(0, length-1)
    y = random.randrange(0, len(field[length -1]))
    field[x][y] = random.choices([0, 1, 2 ,3], [p_0, p_1, p_2, p_3])[0]
    
