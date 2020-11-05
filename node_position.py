import pandas as pd
import networkx as nx
import json

def setup_positions():
    '''
    ノードの座標を追加
    '''
    with open('static/big_graph.json') as f:
        big=json.load(f)
        # ノードとエッジをidがあるかどうかで判断、idがあるのがノード
        node_num = 0
        for i in range(len(big)):
            try:
                if big[i]['data']['id']:
                    node_num += 1
            except KeyError:
                # エッジデータはidがない
                continue
            except Exception as e:
                raise e
        G = nx.path_graph(node_num)
        # networkxでノードに座標を追加
        pos = nx.random_layout(G)

        # 追加した座標をノードデータに書き込み
        for i in range(len(pos)):
            try:
                if big[i]['data']['id']:
                    big[i]["position"]={ 
                        "x": 500*pos[i][0],
                        "y": 500*pos[i][1]
                    }
            except Exception as e:
                raise e
        print("position added")
    
    with open('static/full_data.json', 'w') as f:
        json.dump(big, f)