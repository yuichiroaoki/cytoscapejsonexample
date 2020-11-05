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

@api.route("/new_position.json")
def new_position(req, resp):
    with open('static/new_position.json') as f:
        data=json.load(f)

    resp.media= data

if __name__ == '__main__':
    # setup_positions()
    api.run()