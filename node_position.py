import pandas as pd
import networkx as nx
import json

def setup_positions():
    G = nx.path_graph(57900)
    pos = nx.random_layout(G)
    with open('big_graph.json') as f:
        big=json.load(f)
        print(len(big))
        print(big[2535845]) 
        for i in range(len(pos)):
            try:
                big[i]["position"]["x"]=pos[i][0]
                big[i]["position"]["y"]=pos[i][1]
            except Exception as e:
                raise e
    
    with open('new_position.json', 'w', encoding='utf-8') as f:
        json.dump(big, f)