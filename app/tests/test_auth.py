import json
from werkzeug.test import Client
from werkzeug.datastructures import Headers
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

    def test_register_for_existing_user(self):
        """Test API can not signup existing user."""
        rv = self.app.post("/api/signup", data=json.dumps(self.test_user5),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/signup", data=json.dumps(self.test_user5),
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

    def test_admin_page_is_locked(self):
        rv = self.app.get('/api/users')
        self.assertTrue(rv.status_code, 401)
        self.assertTrue('WWW-Authenticate' in rv.headers)
        self.assertTrue('Basic' in rv.headers['WWW-Authenticate'])

    def test_login_rejects_bad_password(self):
        """Test user cannot login with invalid password."""
        h = Headers()
        h.add('Authorization', 'Basic ' + ('mimi:654321'))
        rv = Client.open(self.app, path='/api/login', headers=h)
        self.assertTrue(rv.status_code, 401)

    def test_login_rejects_bad_username(self):
        """Test user cannot login with invalid username."""
        h = Headers()
        h.add('Authorization', 'Basic ' + ('mosalah:654321'))
        rv = Client.open(self.app, path='/api/login', headers=h)
        self.assertTrue(rv.status_code, 401)

    def test_login_accepts_valid_login(self):
        """Test login with valid credentials."""
        h = Headers()
        h.add('Authorization', 'Basic ' + ('mimi:123456'))
        rv = Client.open(self.app, path='/api/login', headers=h)
        self.assertTrue(rv.status_code, 200)
