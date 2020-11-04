import pandas as pd
import networkx as nx
import json

def setup_positions():
    G = nx.path_graph(57900)
    pos = nx.random_layout(G)
    with open('static/bigGraph.json') as f:
        big=json.load(f)
        print(len(big))
        print(big[2535845]) 
        for i in range(len(pos)):
            try:
                big[i]["position"]={ 
                    "x": 500*pos[i][0],
                    "y": 500*pos[i][1]
                }
            except Exception as e:
                raise e
        print("position added")
    
    with open('static/full_data.json', 'w') as f:
        json.dump(big, f)