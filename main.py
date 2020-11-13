import responder
import json

api = responder.API(templates_dir='./static')

#ホームにアクセスするとReactのviewが表示される
@api.route("/")
def index(req, resp):
    resp.html= api.template('index.html')

@api.route("/{file}/json")
def json_file(req, resp, *, file):
    with open('static/data/'+ file + '.json') as f:
        data=json.load(f)

    resp.media= data


if __name__ == '__main__':
    api.run()