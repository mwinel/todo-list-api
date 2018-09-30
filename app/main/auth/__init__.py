from flask import Blueprint

api = Blueprint('auth', __name__)

from app.main.auth import views
