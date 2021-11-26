import pandas as pd
import os

class Visualizer:

    def __init__(self):
        df = pd.read_csv('board.csv', header=None,index_col=False)
        self.collection = df
    
    def __str__(self):
        df = pd.read_csv('board.csv', header=None,index_col=False)
        # self.clear()
        return df.to_string()

    def set_entities(self, ent_collection):
        if(ent_collection and isinstance(ent_collection, list)):
            if all(isinstance(element, list) for element in ent_collection):
                self.collection = ent_collection
                df = pd.DataFrame(ent_collection)
                df.to_csv('board.csv', header=None,index=False)
            else:
                raise ValueError('List items are not a list')
        else:
            raise ValueError('Variable is not a list')

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')


