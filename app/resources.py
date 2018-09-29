from flask import jsonify, request
from app import app
from app.users import create_new_user, get_all_users, get_user_by_username
from app.db import users


@app.errorhandler(404)
def not_found(error):
    return jsonify("The requested URL was not found on the server."), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify("The method is not allowed for the requested URL."), 405


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


@app.route("/api/login", methods=['POST'])
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


@app.route("/api/users", methods=['GET'])
def get_users():
    return get_all_users()
