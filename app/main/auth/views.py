import re
from flask import jsonify, request
from app.main.auth import api
from app.main.auth.user import (create_new_user, get_user_by_username,
                                get_all_users)


@api.route("/signup", methods=['POST'])
def register_user():
    username = request.json.get('username')
    password = request.json.get('password')
    if username == "" or password == "":
        return jsonify("Fields cannot be left empty."), 400
    if not re.match("^[a-zA-Z0-9_.-]+$", username):
        return jsonify("Username should not have spaces."), 400
    if len(password) <= 5:
        return jsonify("Password too short."), 400
    user_exists = get_user_by_username(username)
    if user_exists:
        return jsonify("User already exists."), 400
    return create_new_user(username, password), 201


@api.route("/users", methods=['GET'])
def get_users():
    return get_all_users(), 200
