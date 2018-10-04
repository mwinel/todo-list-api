from flask import Blueprint

api = Blueprint('todos', __name__)

from app.main.todos import views
