class Book:
    def __init__(self, title, author, isbn, copies=1, available_copies=None):
        # Initialize the Book object with the provided parameters
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies
        self.available_copies = available_copies if available_copies is not None else copies

    def __str__(self):
        # Return a string representation of the Book object
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}, Copies: {self.copies}, Available Copies: {self.available_copies}"

    def check_out(self):
        # Check out a copy of the book
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        else:
            return False

    def check_in(self):
        # Check in a copy of the book
        if self.available_copies < self.copies:
            self.available_copies += 1
            return True
        else:
            return False
