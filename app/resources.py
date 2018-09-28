# import json
from flask import jsonify, request
from app import app
from app.users import create_new_user, get_all_users, get_user_by_username
# from app.db import users


@app.route("/api/index", methods=['GET'])
def index():
    return jsonify({"message": "Welcome to todo-lists"}), 200


@app.route("/api/signup", methods=['POST'])
def register_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username == "" or password == "":
        return jsonify("Fields cannot be left empty."), 400
    if len(password) <= 5:
        return jsonify("Password too short."), 400
    user_exists = get_user_by_username(username)
    if user_exists:
        return jsonify("User already exists."), 400
    return create_new_user(username, password), 201


@app.route("/api/users", methods=['GET'])
def get_users():
    return get_all_users()
