import unittest
from manage import app
from app.models import Todo


class TestTodoObject(unittest.TestCase):
    """
    This class tests the todo object.
    """

    def setUp(self):
        self.app = app.test_client()
        self.todo1 = Todo("September List")

    def test_todo_object(self):
        """Test whether an object is an instance of the Todo class."""
        self.assertIsInstance(self.todo1, Todo)

    def test_title(self):
        """Test title is an instance variable of the Todo class."""
        self.assertEqual(self.todo1.title, "September List")
