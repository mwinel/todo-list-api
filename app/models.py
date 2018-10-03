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
        Returns data in serializable format.
        """
        return {
            "username": self.username,
            "password": self.password
        }
