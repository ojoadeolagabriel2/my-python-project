import requests
import logging
from flask import jsonify, request, render_template, make_response
import utils.app_environment as resolver
from utils.app_context import AppContext
from utils.app_response_code import ResponseCode

app = AppContext().app
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s:%(message)s')


@app.route("/api/v1/pokemon", methods=['POST'])
def create_pokemon():
    try:
        payload = request.get_json()
        return jsonify({"created_version": payload["version"]})
    except KeyError as error:
        logging.debug(f"detected: {str(type(error))}")
        return jsonify({"code": ResponseCode.MISSING_FIELD, "message": f"missing field {error}"})
    finally:
        print("called POST /api/v1/pokemon done")


@app.route("/api/v1/monster/<name>", methods=['GET'])
def fetch_monster(name):
    resp = make_response(render_template("application/json", username='dexter'))
    resp.headers["x-response"] = name
    return resp


@app.route("/api/v1/pokemon/<name>", methods=['GET'])
def display_total_amount(name=None):
    try:
        page = request.args.get('page', default=1, type=int)
        page_filter = request.args.get('filter', default="*", type=str)
        logging.debug(f"read name {name} from /api/v1/pokemon/<name>, page {page}, filter {page_filter}")

        request_header = {
            "x-token": "12345AD",
            "content-type": "application/json"
        }

        response = requests.get(resolver.URL_TEMPLATE.format(resolver.resolve_pokemon_host(),
                                                             resolver.resolve_pokemon_host_port(),
                                                             name), headers=request_header)
        return jsonify({"id": 1, "description": response.json()["description"]})
    except Exception as error:
        return jsonify({"code": ResponseCode.UNKNOWN, "message": str(error)})
    finally:
        print("called GET /api/v1/pokemon/<name> done")


@app.route("/api/v1/pokemon/<int:pokemon_id>", methods=['GET'])
def display_total_amount_by_id(pokemon_id):
    try:
        logging.debug(f"read pokemon_id {pokemon_id} from /api/v1/pokemon/<pokemon_id>")

        response = requests.get(resolver.URL_TEMPLATE.format(resolver.resolve_pokemon_host(),
                                                             resolver.resolve_pokemon_host_port(),
                                                             pokemon_id))
        return jsonify({"id": pokemon_id, "description": response.json()["description"]})
    except Exception as error:
        return jsonify({"code": "", "message": str(error)})
    finally:
        print("called GET /api/v1/pokemon/<int:pokemonId> done")


app.run(host="0.0.0.0", port=resolver.resolve_app_port())
