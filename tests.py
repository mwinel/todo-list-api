import unittest
from app import app


class TestTodoApi(unittest.TestCase):
    """
    Tests for the todo-list api.
    """

    def setUp(self):
        self.app = app.test_client()

    def test_index(self):
        """Test response to index endpoint."""
        rv = self.app.get("/api/index")
        assert rv.status_code == 200
        b"Welcome to todo-lists" in rv.data


if __name__ == "__main__":
    unittest.main(verbosity=2)
