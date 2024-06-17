class User:
    """
    Represents a user with a unique ID and a name.
    """

    def __init__(self, user_id, name):
        # Initialize the user object with the provided user ID and name.
        self.user_id = user_id
        self.name = name

    def __str__(self):
        # Return a string representation of the user object.
        return f"{self.name} (ID: {self.user_id})"
