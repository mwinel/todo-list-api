import unittest
import json
from run import app
from app.models import User


class TestTodoApi(unittest.TestCase):
    """
    Tests for the todo-list api.
    """

    def setUp(self):
        self.app = app.test_client()

        # Test user objects.
        self.user1 = User("nelson", "password")
        self.user2 = User("jackmah", "password")

        # Test users.
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

    def test_user_object(self):
        """Test whether an object is an instance of the User class."""
        self.assertIsInstance(self.user1, User)

    def test_username(self):
        """Test username is an instance variable of the User class."""
        self.assertEqual(self.user1.username, "nelson")

    def test_password(self):
        """Test password is an instance variable of the User class."""
        self.assertEqual(self.user1.password, "password")

    def test_index(self):
        """Test response to index endpoint."""
        rv = self.app.get("/api/index")
        self.assertTrue(rv.status_code, 200)
        b"Welcome to todo-lists" in rv.data

    def test_register_user(self):
        """Test API can signup new user."""
        rv = self.app.post("/api/signup", data=json.dumps(self.test_user1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)

    def test_register_with_empty_username_field(self):
        """Test user can not signup with empty username field."""
        rv = self.app.post("/api/signup", data=json.dumps(self.test_user2),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 400)
        b"Fields cannot be left empty" in rv.data

    def test_register_with_empty_password_field(self):
        """Test user can not signup with empty password field."""
        rv = self.app.post("/api/signup", data=json.dumps(self.test_user3),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 400)
        b"Fields cannot be left empty" in rv.data

    def test_register_with_short_password(self):
        """Test user can not signup with a password less than 6 characters."""
        rv = self.app.post("/api/signup", data=json.dumps(self.test_user4),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 400)
        b"Password too short" in rv.data

    def test_register_for_existing_user(self):
        """Test API can not signup exiting user."""
        rv = self.app.post("/api/signup", data=json.dumps(self.test_user1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/signup", data=json.dumps(self.test_user1),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)

    def test_user_login(self):
        """Test API can login a user."""
        rv = self.app.post("/api/signup", data=json.dumps(self.test_user1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/login", data=json.dumps(self.test_user1),
                            content_type='application/json')
        self.assertTrue(res.status_code, 200)
        b"Successfully logged in as mimi."

    def test_user_login_invalid_credentials(self):
        """Test API can not login a user with invalid credentials."""
        rv = self.app.post("/api/signup", data=json.dumps(self.test_user1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/login",
                            data=json.dumps({
                                "username": "mimi",
                                "password": "prince"
                            }),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"Invalid credentials" in res.data

    def test_user_login_for_non_registered_user(self):
        """Test API can not login a non registered user."""
        rv = self.app.post("/api/signup", data=json.dumps(self.test_user1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 400)
        b"User does not exist." in rv.data

    def tearDown(self):
        pass


if __name__ == "__main__":
    unittest.main(verbosity=2)
