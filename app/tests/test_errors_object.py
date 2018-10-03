import unittest
from manage import app
from app.main.errors.request_errors import RequestError


class TestRequestError(unittest.TestCase):
    """
    This class tests the request error object.
    """

    def setUp(self):
        self.app = app.test_client()
        self.request_error = RequestError()

    def test_request_error_object(self):
        """Test whether an object is an instance of the RequestError class."""
        self.assertIsInstance(self.request_error, RequestError)

    def test_not_found_error(self):
        """Test not found error response."""
        self.assertTrue(self.request_error.not_found())

    def test_method_not_allowed_error(self):
        """Test method not allowed error response."""
        self.assertTrue(self.request_error.method_not_allowed())

    def test_internal_server_error(self):
        """Test method internal server error response."""
        self.assertTrue(self.request_error.internal_server_error())
