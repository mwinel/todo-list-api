# Define a user class.
class User:
    """
    This class defines the user in terms of
    the username, password.
    """
    user_id_counter = 1

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.id = User.user_id_counter
        User.user_id_counter += 1

    # Define a method and we can access it
    # as an attribute.
    @property
    def serialize(self):
        """
        Retruns data in serializable format.
        """
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password
        }
