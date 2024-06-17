import pandas as pd
from book import Book
from user import User

class Storage:
    def __init__(self, books_file, users_file, logs_file):
        self.books_file = books_file
        self.users_file = users_file
        self.logs_file = logs_file

    def load_books(self):
        try:
            # Read the books data from the CSV file
            df = pd.read_csv(self.books_file)
            # Create a dictionary of books using ISBN as the key
            books = {row['isbn']: Book(row['title'], row['author'], row['isbn'], row['copies'], row['available_copies']) for _, row in df.iterrows()}
            return books
        except FileNotFoundError:
            return {}

    def save_books(self, books):
        # Convert the books dictionary into a list of dictionaries
        data = [{'title': book.title, 'author': book.author, 'isbn': book.isbn, 'copies': book.copies, 'available_copies': book.available_copies} for book in books.values()]
        # Create a DataFrame from the list of dictionaries
        df = pd.DataFrame(data)
        # Save the DataFrame to the books file as a CSV
        df.to_csv(self.books_file, index=False)

    def load_users(self):
        try:
            # Read the users data from the CSV file
            df = pd.read_csv(self.users_file)
            # Create a dictionary of users using user_id as the key
            users = {row['user_id']: User(row['user_id'], row['name']) for _, row in df.iterrows()}
            return users
        except FileNotFoundError:
            return {}

    def save_users(self, users):
        # Convert the users dictionary into a list of dictionaries
        data = [{'user_id': user.user_id, 'name': user.name} for user in users.values()]
        # Create a DataFrame from the list of dictionaries
        df = pd.DataFrame(data)
        # Save the DataFrame to the users file as a CSV
        df.to_csv(self.users_file, index=False)

    def load_logs(self):
        try:
            # Read the logs data from the CSV file
            df = pd.read_csv(self.logs_file)
            # Convert the logs column into a list
            logs = df['log'].tolist()
            return logs
        except FileNotFoundError:
            return []

    def save_logs(self, logs):
        # Create a DataFrame with a single column 'log' containing the logs
        df = pd.DataFrame({'log': logs})
        # Save the DataFrame to the logs file as a CSV
        df.to_csv(self.logs_file, index=False)
