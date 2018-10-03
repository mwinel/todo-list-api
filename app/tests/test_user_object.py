import unittest
from manage import app
from app.models import User


class TestUserObject(unittest.TestCase):
    """
    This class tests the user object.
    """

    def setUp(self):
        self.app = app.test_client()
        self.user1 = User("nelson", "password")
        self.user2 = User("jackmah", "password")

    def test_user_object(self):
        """Test whether an object is an instance of the User class."""
        self.assertIsInstance(self.user1, User)

    def test_username(self):
        """Test username is an instance variable of the User class."""
        self.assertEqual(self.user1.username, "nelson")

    def test_password(self):
        """Test password is an instance variable of the User class."""
        self.assertEqual(self.user1.password, "password")
