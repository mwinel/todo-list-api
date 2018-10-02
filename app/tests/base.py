import unittest
from manage import app
# from app.models import User
# from app.db import Database


class TestBase(unittest.TestCase):
    """
    This class defines the general setup of unit tests.
    """

    def setUp(self):
        self.app = app.test_client()

        self.test_user1 = {
            "username": "mimi",
            "password": "123456"
        }

        self.test_user2 = {
            "username": "",
            "password": "123456"
        }

        self.test_user3 = {
            "username": "mimi",
            "password": ""
        }

        self.test_user4 = {
            "username": "mimi",
            "password": "123"
        }
