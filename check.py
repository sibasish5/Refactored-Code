class Check:
    @staticmethod
    def validate_isbn(isbn):
        """
        Validates the ISBN number.
        :param isbn: The ISBN number to validate.
        :return: True if the ISBN is valid, False otherwise.
        """
        return isbn.isdigit() and (len(isbn) == 10 or len(isbn) == 13)

    @staticmethod
    def validate_user_id(user_id):
        """
        Validates the user ID.
        :param user_id: The user ID to validate.
        :return: True if the user ID is valid, False otherwise.
        """
        return user_id.startswith("U") and user_id[1:].isdigit()

    @staticmethod
    def validate_name(name):
        """
        Validates the name.
        :param name: The name to validate.
        :return: True if the name is valid, False otherwise.
        """
        return name.isalpha()

    @staticmethod
    def validate_copies(copies):
        """
        Validates the number of copies.
        :param copies: The number of copies to validate.
        :return: True if the number of copies is valid, False otherwise.
        """
        return copies.isdigit() and int(copies) > 0
