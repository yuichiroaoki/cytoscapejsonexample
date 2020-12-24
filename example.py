import networkx as nx
import pandas as pd
import json
import time

# ノードデータを読み込み
nodes = pd.read_csv('static/data/node-data.csv')

# エッジデータを読み込み
with open('static/data/Data.json') as f:
    bigdata=json.load(f)
    bigdata = bigdata[57900:]

data = []

# ノードのデータを作成
for i in range(len(nodes)):
    one = {}
    one = {
        "data": {
            "id":nodes.iloc[i][0][-6:],
            "label":nodes.iloc[i][0][-6:]
        }
    }
    data.append(one)
print(data[1])
print(len(data))

pos = {}

def main(new):
    global data, bigdata
    num_nodes = len(data)
    print('num of nodes:', num_nodes)
    G = nx.path_graph(num_nodes)
    # networkxでノードに座標を追加
    new.update(nx.multipartite_layout(G, scale=500))
    # 追加した座標をノードデータに書き込み
    for i in range(len(data)):
        try:
            if data[i]['data']['id']:
                data[i]["position"]={ 
                    "x": pos[i][0],
                    "y": pos[i][1]
                }
        except Exception as e:
            raise e
    print("position added")
    for i in range(20000):
        data.append(bigdata[i])

# レイアウト計算の時間計測
start_time = time.time()
main(pos)
print(len(data))
with open('static/data/bipartmultipartite2.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)
print("--- %s seconds ---" % (time.time() - start_time))

