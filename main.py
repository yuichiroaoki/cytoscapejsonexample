import responder
import json

api = responder.API(templates_dir='./static')

#ホームにアクセスするとReactのviewが表示される
@api.route("/")
def index(req, resp):
    resp.html= api.template('index.html')


@api.route("/big_graph.json")
def bigGraph(req, resp):
    with open('static/big_graph.json') as f:
        df=json.load(f)

    resp.media= df

if __name__ == '__main__':
    api.run()