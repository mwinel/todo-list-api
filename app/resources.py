from flask import jsonify
from app import app


@app.route("/api/index", methods=['GET'])
def index():
    return jsonify({"message": "Welcome to todo-lists"}), 200
