# Define a user class.
class User:
    """
    This class defines the user in terms of
    the username, password.
    """

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def serialize(self):
        """
        Returns user data in JSON serializable format.
        """
        return {
            "username": self.username,
            "password": self.password
        }


# Define todo-list model
class Todo:
    """
    This class defines the todo list in terms
    of the title.
    """

    def __init__(self, title):
        self.title = title

    @property
    def serialize(self):
        """
        Returns todo data in JSON serializable format.
        """
        return {
            "title": self.title
        }
