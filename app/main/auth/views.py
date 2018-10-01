import re
from flask import jsonify, request
from app.main.auth import api
from app.main.auth.user import (create_new_user, get_user_by_username,
                                get_all_users)
from app.models import User


@api.route("/signup", methods=['POST'])
def register_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username == "" or password == "":
        return jsonify({"message": "Fields cannot be left empty."}), 400
    if not re.match("^[a-zA-Z0-9_.-]+$", username):
        return jsonify({"message": "Username should not have spaces."}), 400
    if len(password) <= 5:
        return jsonify({"message": "Password too short."}), 400
    user_exists = get_user_by_username(username)
    if user_exists:
        return jsonify({"message": "User already exists."}), 400
    return create_new_user(username, password), 201


@api.route("/login", methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    query = get_user_by_username(username)
    if not query:
        return jsonify({"message": "User does not exist."}), 404
    user = User(query[1], query[2])
    if user.password == password:
        return jsonify({
            "message": "Successfully logged in as {}.".format(username)
        }), 200
    return jsonify({"message": "Invalid credentials"}), 400


@api.route("/users", methods=['GET'])
def get_users():
    return get_all_users(), 200
