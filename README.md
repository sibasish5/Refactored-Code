Library Management System

Design Decisions and Architecture
Classes and Responsibilities

book.py
The Book class manages individual book details and operations such as checking out and checking in. It encapsulates attributes like title, author, isbn, copies, and available_copies.

user.py
The User class manages user details including user_id and name. It provides methods to update user information and handle user-related operations.

check.py
The Check class contains static methods for input validation, ensuring that user inputs are validated before processing.

storage.py
The Storage class handles file-based storage and retrieval using JSON format. It provides methods to load and save collections of books, users, and logs from/to JSON files.

models.py
The Library class acts as the core component managing collections of books and users. It facilitates interactions such as adding, updating, deleting, searching books and users. Additionally, it supports operations like checking out and checking in books, and logging these operations.

main.py
The main.py file contains the main Command-Line Interface (CLI) loop. It interacts with users through the command line, processes user inputs, and invokes appropriate methods in the Library class to perform operations.

Usage of Classes and Methods

Book Class
Attributes: Stores attributes like title, author, isbn, copies, and available_copies.
Methods: Includes methods for checking out (check_out()) and checking in (check_in()) books.

User Class
Attributes: Manages user_id and name of users.
Methods: Provides functionality to update user details.

Check Class
Static Methods: Contains static methods for input validation, ensuring robust handling of user inputs throughout the application.

Storage Class
Responsibility: Handles file-based storage operations using JSON format.
Methods:
load_books(), save_books(): Load and save books data.
load_users(), save_users(): Load and save users data.
load_logs(), save_logs(): Load and save logs data.

Library Class
Responsibility: Manages collections of books and users, and facilitates interactions between them.
Methods:
Books Management: add_book(), update_book(), delete_book(), list_books(), search_books()
Users Management: add_user(), update_user(), delete_user(), list_users(), search_users()
Book Operations: check_out_book(), check_in_book()
Logging: log_operation(), show_logs()

main.py
Functionality: Contains the main CLI loop where users interact with the library management system.
Process: Takes user inputs, validates them using methods from Check class, and calls appropriate methods in Library class to perform operations on books, users, and logging.
