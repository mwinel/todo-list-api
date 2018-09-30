from flask import Flask
from app.config import app_config
from app.main.errors.request_errors import RequestError


# Create app factory. Create the app intance in the app factory
# Register app configurations.
# Return the app.
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])

    # Request exceptions
    app.errorhandler(404)(RequestError.not_found)
    app.errorhandler(405)(RequestError.method_not_allowed)
    app.errorhandler(500)(RequestError.internal_server_error)

    # Register blueprints
    from app.main.auth import api as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/api")

    return app
