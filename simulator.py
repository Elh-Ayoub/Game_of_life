from visualizer import Visualizer
import pandas as pd
from __init__ import updateField
from helpers import exec_iteration

class Simulator:

    visualizer = Visualizer()
    def __init__(self, visualizer, g):
        self.visualizer = visualizer
        self.g = g
        df = pd.DataFrame(self.visualizer.collection)
        df.to_csv('board.csv', header=None,index=False)
    def draw(self):
        print(self.visualizer)

    def fill(self):
        updateField(self.visualizer.collection)
    
    def step(self):
        exec_iteration(self.visualizer.collection, 1, self.g, self, self.visualizer)

    def clear(self):
        field = list(self.visualizer.collection)
        for i in range(len(field)):
            for j in range(len(field[i])):
                if(field[i][j] != 0 and field[i][j].isDead()):
                    field[i][j] = 0
