import re
from flask import g, jsonify, request
from flask_httpauth import HTTPBasicAuth
from app.main.auth import api
from app.main.auth.user import (create_new_user, get_user_by_username,
                                get_all_users)
from app.models import User


auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    user = get_user_by_username(username)
    if not user:
        return False
    g.user = user
    return True


@auth.error_handler
def auth_error():
    return jsonify({"error": "Unauthorized Access!"}), 401


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
        return jsonify({"message": "User does not exist."}), 400
    user = User(query[1], query[2])
    if user.password == password:
        return jsonify({
            "message": "Successfully logged in as {}.".format(username)
        }), 200
    return jsonify({"message": "Invalid credentials"}), 400


@api.route("/users", methods=['GET'])
@auth.login_required
def get_users():
    return get_all_users(), 200
