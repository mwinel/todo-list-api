import unittest
from flask import current_app
from manage import app


class TestDevelopmentConfig(unittest.TestCase):
    """Test development enviromrnt configurations."""

    def create_app(self):
        app.config.from_object('app.config.DevelopmentConfig')
        return app

    def test_env_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertFalse(current_app is None)


class TestTestingConfig(unittest.TestCase):
    """Test testing enviromrnt configurations."""

    def create_app(self):
        app.config.from_object('app.config.TestingConfig')
        return app

    def test_env_is_testing(self):
        self.assertTrue(app.config['TESTING'] is False)
        self.assertFalse(current_app is None)


class TestProductionConfig(unittest.TestCase):
    """Test production enviromrnt configurations."""

    def create_app(self):
        app.config.from_object('app.config.ProductionConfig')
        return app

    def test_env_is_testing(self):
        self.assertTrue(app.config['DEBUG'] is False)
        self.assertFalse(current_app is None)
