import responder
import json
from node_position import setup_positions

api = responder.API(templates_dir='./static')

#ホームにアクセスするとReactのviewが表示される
@api.route("/")
def index(req, resp):
    resp.html= api.template('index.html')


@api.route("/bigGraph.json")
def bigGraph(req, resp):
    with open('static/bigGraph.json') as f:
        df=json.load(f)

    resp.media= df

if __name__ == '__main__':
    api.run()
    setup_positions()