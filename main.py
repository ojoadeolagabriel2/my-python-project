import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route("/api/v1/<int:amount>", methods=['GET'])
def display_total_amount(amount):
    print(amount)
    response = requests.get("http://pokemon-information-service-service.information-ns.svc.cluster.local:50002/pokemon/pikachu")
    return jsonify({"id": "1", "message": response.json()["description"]})


app.run(host="0.0.0.0", port=12345)
