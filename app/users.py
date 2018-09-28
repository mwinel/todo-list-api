from flask import jsonify
from app.models import User
from app.db import users


def create_new_user(username, password):
    user = User(username=username, password=password)
    users.append(user)
    return jsonify(User=user.serialize)


def get_all_users():
    return jsonify(Users=[i.serialize for i in users])


def get_user_by_username(username):
    for user in users:
        if user.username == username:
            return user
