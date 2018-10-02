import json
from app.tests.base import TestBase


class TestAuthCase(TestBase):
    """
    This class tests the user auth endpoints.
    """

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
