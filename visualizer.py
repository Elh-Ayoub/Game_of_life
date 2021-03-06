import pandas as pd
import os

from pandas.core.frame import DataFrame

class Visualizer:

    def __init__(self):
        df = pd.read_csv('board.csv', header=None,index_col=False)
        self.collection = df
    
    def __str__(self):
        return pd.DataFrame(self.collection).to_string()

    def set_entities(self, ent_collection):
        if(isinstance(ent_collection, list)):
            if all(isinstance(element, list) for element in ent_collection):
                self.collection = ent_collection
                df = pd.DataFrame(ent_collection)
                df.to_csv('board.csv', header=None,index=False)
            else:
                raise ValueError('List items are not a list')
        elif(isinstance(ent_collection, DataFrame)):
                self.collection = pd.DataFrame(ent_collection).to_numpy()
        else:
            raise ValueError('Variable is not a list')

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


