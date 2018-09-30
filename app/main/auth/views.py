import re
from flask import jsonify, request
from functools import wraps
from app.main.auth import api
from app.main.auth.user import (create_new_user, get_user_by_username,
                                get_all_users)
from app.db import users


def check_auth(username, password):
    # Check if username or password combinations are valid.
    return username == 'username' and password == 'password'


def authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return jsonify("Unauthorized Access!"), 401
        return f(*args, **kwargs)
    return wrapper


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


@api.route("/api/login", methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')
    current_user = get_user_by_username(username)
    if not current_user:
        return jsonify("User does not exist."), 404
    for user in users:
        if username == user.username and password == user.password:
            return jsonify("Successfully logged in as {}."
                           .format(username)), 200
        return jsonify("Invalid credentials"), 400


@api.route("/users", methods=['GET'])
def get_users():
    return get_all_users(), 200
