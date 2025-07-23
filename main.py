from flask import Flask, jsonify
from scraper import fetch_pc_releases

app = Flask(__name__)

@app.route("/api/releases", methods=["GET"])
def releases():
    return jsonify(fetch_pc_releases())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
