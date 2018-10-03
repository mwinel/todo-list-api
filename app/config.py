import os


class Config:
    """Base configurations."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'precious')
    DEBUG = False


class DevelopmentConfig(Config):
    """Development configurations."""
    DEBUG = True
    DATABASE_URL = "postgresql://postgres:myPassword@localhost/todo"


class TestingConfig(Config):
    """Testing configurations."""
    TESTING = True
    DATABASE_URL = "postgresql://postgres:myPassword@localhost/todo_tests"


class ProductionConfig(Config):
    """Production configurations."""
    DEBUG = False


app_config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
