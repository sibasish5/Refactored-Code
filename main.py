from models import Library
from check import Check

def main():
    # Create a Library object with the storage file name
    library = Library("library_storage.json")

    while True:
        # Display the menu options
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. List Books")
        print("5. Search Books")
        print("6. Add User")
        print("7. Update User")
        print("8. Delete User")
        print("9. List Users")
        print("10. Search Users")
        print("11. Check Out Book")
        print("12. Check In Book")
        print("13. Show Logs")
        print("14. Exit")
        
        # Get user's choice
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add a new book
            title = input("Enter title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            if not Check.validate_isbn(isbn):
                print("Invalid ISBN. Must be 10 or 13 digits.")
                continue
            copies = input("Enter number of copies: ")
            if not Check.validate_copies(copies):
                print("Invalid number of copies. Must be a positive integer.")
                continue
            library.add_book(title, author, isbn, int(copies))

        elif choice == "2":
            # Update an existing book
            isbn = input("Enter ISBN of the book to update: ")
            if not Check.validate_isbn(isbn):
                print("Invalid ISBN. Must be 10 or 13 digits.")
                continue
            title = input("Enter new title (leave blank to keep current): ")
            author = input("Enter new author (leave blank to keep current): ")
            copies = input("Enter new number of copies (leave blank to keep current): ")
            copies = int(copies) if copies and Check.validate_copies(copies) else None
            library.update_book(isbn, title, author, copies)

        elif choice == "3":
            # Delete a book
            isbn = input("Enter ISBN of the book to delete: ")
            if not Check.validate_isbn(isbn):
                print("Invalid ISBN. Must be 10 or 13 digits.")
                continue
            library.delete_book(isbn)

        elif choice == "4":
            # List all books
            library.list_books()

        elif choice == "5":
            # Search for books
            search_params = {}
            title = input("Enter title to search (leave blank to skip): ")
            if title:
                search_params['title'] = title
            author = input("Enter author to search (leave blank to skip): ")
            if author:
                search_params['author'] = author
            isbn = input("Enter ISBN to search (leave blank to skip): ")
            if isbn and Check.validate_isbn(isbn):
                search_params['isbn'] = isbn
            results = library.search_books(**search_params)
            for book in results:
                print(book)

        elif choice == "6":
            # Add a new user
            user_id = input("Enter user ID: ")
            if not Check.validate_user_id(user_id):
                print("Invalid User ID. Must start with 'U' followed by digits.")
                continue
            name = input("Enter name: ")
            if not Check.validate_name(name):
                print("Invalid name. Must contain only alphabetic characters.")
                continue
            library.add_user(user_id, name)

        elif choice == "7":
            # Update an existing user
            user_id = input("Enter user ID to update: ")
            if not Check.validate_user_id(user_id):
                print("Invalid User ID. Must start with 'U' followed by digits.")
                continue
            name = input("Enter new name (leave blank to keep current): ")
            if name and not Check.validate_name(name):
                print("Invalid name. Must contain only alphabetic characters.")
                continue
            library.update_user(user_id, name)

        elif choice == "8":
            # Delete a user
            user_id = input("Enter user ID to delete: ")
            if not Check.validate_user_id(user_id):
                print("Invalid User ID. Must start with 'U' followed by digits.")
                continue
            library.delete_user(user_id)

        elif choice == "9":
            # List all users
            library.list_users()

        elif choice == "10":
            # Search for users
            search_params = {}
            user_id = input("Enter user ID to search (leave blank to skip): ")
            if user_id and Check.validate_user_id(user_id):
                search_params['user_id'] = user_id
            name = input("Enter name to search (leave blank to skip): ")
            if name and Check.validate_name(name):
                search_params['name'] = name
            results = library.search_users(**search_params)
            for user in results:
                print(user)

        elif choice == "11":
            # Check out a book
            isbn = input("Enter ISBN of the book to check out: ")
            if not Check.validate_isbn(isbn):
                print("Invalid ISBN. Must be 10 or 13 digits.")
                continue
            user_id = input("Enter user ID: ")
            if not Check.validate_user_id(user_id):
                print("Invalid User ID. Must start with 'U' followed by digits.")
                continue
            library.check_out_book(isbn, user_id)

        elif choice == "12":
            # Check in a book
            isbn = input("Enter ISBN of the book to check in: ")
            if not Check.validate_isbn(isbn):
                print("Invalid ISBN. Must be 10 or 13 digits.")
                continue
            user_id = input("Enter user ID: ")
            if not Check.validate_user_id(user_id):
                print("Invalid User ID. Must start with 'U' followed by digits.")
                continue
            library.check_in_book(isbn, user_id)

        elif choice == "13":
            # Show logs
            library.show_logs()

        elif choice == "14":
            # Exit the program
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
