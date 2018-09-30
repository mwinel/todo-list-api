# Class to handle request exceptions.
from flask import jsonify, request


class RequestError:
    """
    This class defines a way to handle request exceptions.
    Flask will not set an error code for you. Therefore provide
    the HTTP status code when returning a response.
    """

    message = {
        'error_message': "{0}, '{1}'"
    }

    def not_found(error):
        """
        Returns a formatted 404 NOT FOUND error message.
        parameters: error
        """
        return jsonify({"error": RequestError.message['error_message'].format(
            "The requested URL was not found on the server",
            request.url
        )}), 404

    def method_not_allowed(error):
        """
        Returns a formatted 405 METHOD NOT ALLOWED error message.
        parameters: error
        """
        return jsonify({"error": RequestError.message['error_message'].format(
            "The method is not allowed for the requested URL", request.url
        )}), 405

    def internal_server_error(error):
        """
        Returns a formatted 500 INTERNAL SERVER ERROR error message.
        parameters: error
        """
        return jsonify({"error": RequestError.message['error_message'].format(
            error, request.url
        )}), 500
