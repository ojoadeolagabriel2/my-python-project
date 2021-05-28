import requests
from flask import Flask, jsonify

import utils.resolver

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

URL_TEMPLATE = "http://{}:{}/pokemon/{}"


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route("/api/v1/pokemon/<name>", methods=['GET'])
def display_total_amount(name=None):
    print(name)
    response = requests.get(URL_TEMPLATE.format(utils.resolver.resolve_pokemon_host(),
                                                utils.resolver.resolve_pokemon_host_port(),
                                                name))
    return jsonify({"id": "1", "description": response.json()["description"]})


app.run(host="0.0.0.0", port=utils.resolver.resolve_app_port())
