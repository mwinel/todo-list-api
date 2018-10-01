from flask import jsonify
from app.models import User
from app.db import Database


db = Database()


def create_new_user(username, password):
    """
    This method creates a user.
    parameters: username, password
    returns: a json dictionary of the user.
    """
    user = User(username=username, password=password)
    db.insert_user_data(username, password)
    return jsonify(User=user)


def get_all_users():
    """
    This method returns a list of users.
    """
    users = db.fetch_all_users()
    return jsonify(Users=users)


def get_user_by_username(username):
    """
    This method checks for a user given the username.
    parameters: username
    returns: user
    """
    user = db.get_by_argument('users', 'username', username)
    return user
