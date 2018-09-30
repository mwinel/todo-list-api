from flask import jsonify
from app.models import User
from app.db import users


def create_new_user(username, password):
    """
    This method creates a user.
    parameters: username, password
    returns: a json dictionary of the user.
    """
    user = User(username=username, password=password)
    users.append(user)
    return jsonify(User=user.serialize)


def get_all_users():
    """
    This method returns a list of users.
    """
    return jsonify(Users=[i.serialize for i in users])


def get_user_by_username(username):
    """
    This method checks for a user given the username.
    parameters: username
    returns: user
    """
    for user in users:
        if user.username == username:
            return user
