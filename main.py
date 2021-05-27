from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route("/api/v1/<int:amount>", methods=['GET'])
def display_total_amount(amount):
    print(amount)
    return jsonify({"id": "1"})


app.run(port=12345)
