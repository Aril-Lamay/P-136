from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "data": data,
        "message": "success"
    }), 200


@app.route("/star")
def star():
    star_name = request.args.get("Star_name")
    star_data = next(item for item in data if item["Star_name"] == star_name)
    return jsonify({
        "data": star_data,
        "message": "success"
    }), 200

    
if __name__ == "__main__":
    app.run()
