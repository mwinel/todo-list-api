import json
from app.tests.base import TestBase


class TestTodosCase(TestBase):
    """
    This class tests the todos endpoints.
    """

    def test_create_todo(self):
        """Test API can create a new todo."""
        rv = self.app.post("/api/todo", data=json.dumps(self.todo1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)

    def test_create_todo_with_empty_fields(self):
        """Test API cannot create a todo with empty fields."""
        rv = self.app.post("/api/todo", data=json.dumps(self.todo2),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 400)
        b"Fields cannot be left empty." in rv.data

    def test_create_todo_with_short_title(self):
        """Test API cannot create a todo with short title."""
        rv = self.app.post("/api/todo", data=json.dumps(self.todo3),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 400)
        b"Title too short." in rv.data

    def test_create_existing_todo(self):
        """Test API cannot create an existing todo."""
        rv = self.app.post("/api/todo", data=json.dumps(self.todo1),
                           content_type='application/json')
        self.assertTrue(rv.status_code, 201)
        res = self.app.post("/api/todo", data=json.dumps(self.todo1),
                            content_type='application/json')
        self.assertTrue(res.status_code, 400)
        b"Todo lis exists." in rv.data

    def test_create_todo_is_locked(self):
        rv = self.app.get("/api/todo")
        self.assertTrue(rv.status_code, 401)
