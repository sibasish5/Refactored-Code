from book import Book
from user import User
from storage import Storage
import datetime

class Library:
    def __init__(self, books_file, users_file, logs_file):
        self.storage = Storage(books_file, users_file, logs_file)
        self.books = self.storage.load_books()  # Load books from storage
        self.users = self.storage.load_users()  # Load users from storage
        self.logs = self.storage.load_logs()  # Load logs from storage

    def add_book(self, title, author, isbn, copies=1):
        if isbn in self.books:
            self.books[isbn].copies += copies  # Increase copies of existing book
            self.books[isbn].available_copies += copies  # Increase available copies
        else:
            self.books[isbn] = Book(title, author, isbn, copies)  # Create new book
        self.storage.save_books(self.books)  # Save books to storage
        self.log_operation(f"Added book: {title} (ISBN: {isbn})")  # Log the operation

    def update_book(self, isbn, title=None, author=None, copies=None):
        if isbn in self.books:
            book = self.books[isbn]
            if title:
                book.title = title  # Update book title
            if author:
                book.author = author  # Update book author
            if copies is not None:
                book.copies = copies  # Update total copies
                book.available_copies = copies  # Reset available copies
            self.storage.save_books(self.books)  # Save books to storage
            self.log_operation(f"Updated book: {isbn}")  # Log the operation
        else:
            print("Book not found")

    def delete_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]  # Delete book
            self.storage.save_books(self.books)  # Save books to storage
            self.log_operation(f"Deleted book: {isbn}")  # Log the operation
        else:
            print("Book not found")

    def list_books(self):
        for book in self.books.values():
            print(book)

    def search_books(self, **kwargs):
        results = []
        for book in self.books.values():
            match = all(getattr(book, key) == value for key, value in kwargs.items())
            if match:
                results.append(book)
        return results

    def add_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name)  # Create new user
            self.storage.save_users(self.users)  # Save users to storage
            self.log_operation(f"Added user: {name} (ID: {user_id})")  # Log the operation
        else:
            print("User ID already exists")

    def update_user(self, user_id, name=None):
        if user_id in self.users:
            user = self.users[user_id]
            if name:
                user.name = name  # Update user name
            self.storage.save_users(self.users)  # Save users to storage
            self.log_operation(f"Updated user: {user_id}")  # Log the operation
        else:
            print("User not found")

    def delete_user(self, user_id):
        if user_id in self.users:
            del self.users[user_id]  # Delete user
            self.storage.save_users(self.users)  # Save users to storage
            self.log_operation(f"Deleted user: {user_id}")  # Log the operation
        else:
            print("User not found")

    def list_users(self):
        for user in self.users.values():
            print(user)

    def search_users(self, **kwargs):
        results = []
        for user in self.users.values():
            match = all(getattr(user, key) == value for key, value in kwargs.items())
            if match:
                results.append(user)
        return results

    def check_out_book(self, isbn, user_id):
        if isbn in self.books and user_id in self.users:
            book = self.books[isbn]
            if book.check_out():
                self.storage.save_books(self.books)  # Save books to storage
                self.log_operation(f"Checked out {isbn} to {user_id}")  # Log the operation
            else:
                print("Book not available")
        else:
            print("Book or User not found")

    def check_in_book(self, isbn, user_id):
        if isbn in self.books and user_id in self.users:
            book = self.books[isbn]
            if book.check_in():
                self.storage.save_books(self.books)  # Save books to storage
                self.log_operation(f"Checked in {isbn} from {user_id}")  # Log the operation
            else:
                print("All copies already checked in")
        else:
            print("Book or User not found")

    def log_operation(self, operation):
        timestamp = datetime.datetime.now().isoformat()
        self.logs.append(f"{timestamp}: {operation}")  # Add operation to logs
        self.storage.save_logs(self.logs)  # Save logs to storage

    def show_logs(self):
        for log in self.logs:
            print(log)
