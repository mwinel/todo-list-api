import unittest
from manage import app
from app.db import Database


class TestDbOject(unittest.TestCase):
    """
    This class test the database object.
    """

    def setUp(self):
        self.app = app.test_client()
        self.db1 = Database()

    def test_database_object(self):
        """Test whether an object is an instance of the Database class."""
        self.assertIsInstance(self.db1, Database)
