import json

from pathlib import Path
from flask import Flask, request

app = Flask(__name__)

with open("config.json", "r") as f:
    global config
    config = json.load(f)

Path("data.json").touch(exist_ok=True)
with open("data.json", "r+") as f:
    global data
    try:
        data = json.load(f)
    except:
        data = {}


def save_data(new_data):
    with open("data.json", "r+") as f:
        json.dump(new_data, f, sort_keys=True, indent=4)


def has_json_key(json, key):
    try:
        k = json[key]
    except KeyError:
        return False

    return True


@app.route('/')
def root():
    return 'Hello, World!'


@app.route('/register_app', methods=['POST'])
def register_app():
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header == f"Bearer {config['api_key']}":
        pass
    else:
        err = {
            'status': 'error',
            'error': 'You are not authorized to use this endpoint. Please make sure your API key is correct.'
        }

        return json.loads(json.dumps(err, indent=4)), 401

    content = request.get_json()
    app_name = content["app_name"]

    data[app_name] = {}
    data[app_name]["hits"] = 0
    save_data(data)

    success = {
        'status': 'success',
        'message': 'The app is now registered.'
    }

    return json.loads(json.dumps(success, indent=4)), 200


@app.route('/hit', methods=['POST'])
def hit():
    content = request.get_json()
    app_name = content["app_name"]

    if has_json_key(data, app_name):
        data[app_name]["hits"] += 1
        save_data(data)
        success = {
            'status': 'success',
            'message': 'Added a hit to the app.'
        }

        return json.loads(json.dumps(success, indent=4)), 200
    else:
        err = {
            'status': 'error',
            'error': 'This app is not registered.'
        }

        return json.loads(json.dumps(err, indent=4)), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=config["port"])
