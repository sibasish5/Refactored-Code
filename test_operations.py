from models import Library

def test_library_operations():
    # Initialize library instance
    library = Library("books.csv", "users.csv", "logs.csv")

    # Add books
    print("\nAdding books...")
    library.add_book("Python Programming 101", "John Doe Jr.", "9780134853987", 5)
    library.add_book("Advanced Data Structures", "Jane Smith", "9780262033849", 3)

    # List books
    print("\nListing books...")
    library.list_books()

    # Update a book
    print("\nUpdating a book...")
    library.update_book("9780134853987", title="Python Programming 101", author="John Doe Jr.", copies=7)

    # List books after update
    print("\nListing books after update...")
    library.list_books()

    # Add users
    print("\nAdding users...")
    library.add_user("U003", "Charlie Brown")
    library.add_user("U004", "Eve Smith")

    # List users
    print("\nListing users...")
    library.list_users()

    # Check out a book
    print("\nChecking out a book...")
    library.check_out_book("9780134853987", "U003")

    # Check in a book
    print("\nChecking in a book...")
    library.check_in_book("9780134853987", "U003")

    # List books after check in
    print("\nListing books after check in...")
    library.list_books()

    # Search books by title
    print("\nSearching books by title...")
    results = library.search_books(title="Python Programming 101")
    for book in results:
        print(book)

    # Search users by name
    print("\nSearching users by name...")
    results = library.search_users(name="Charlie Brown")
    for user in results:
        print(user)

    # Show logs
    print("\nShowing logs...")
    library.show_logs()

if __name__ == "__main__":
    test_library_operations()

