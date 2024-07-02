from bookmanager import *

lib = Library()

lib.add_user(User("John", "123456"))
lib.add_user(User("Admin", "admin", True))

lib.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald"))
lib.add_book(Book("To Kill a Mockingbird", "Harper Lee"))
lib.add_book(Book("1984", "George Orwell"))

user = None
running = True

while running:
    if user is None:
        user = User("Guest", "guest")
    print(f"\nHi \x1B[36m{user.name}\x1B[0m, welcome to the library.")
    print("1. Login / Relogin")
    print("2. List my books")
    print("3. Query Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. List Books (admin only)")
    print("7. Sort Books (admin only)")
    print("8. Add Book (admin only)")
    print("9. Remove Book (admin only)")
    print("0. Exit\n")
    action = int(input("> "))
    if action == 1:
        name = input("Name: ")
        password = input("Password: ")
        user = lib.login(name, password)
        if user is None:
            print("Invalid name or password")
    elif action == 2:
        books = user.list_books()
        if not books:
            print("No books")
        else:
            for book in books:
                print(book)
    elif action == 3:
        title = input("Title: ")
        book = lib.query_book(title)
        if book is None:
            print("Book not found")
        else:
            print(book)
    elif action == 4:
        title = input("Title: ")
        book = lib.query_book(title)
        if book is None:
            print("Book not found")
        else:
            lib.borrow_book(user, book)
            print("Book borrowed")
    elif action == 5:
        title = input("Title: ")
        book = lib.query_book(title)
        if book is None:
            print("Book not found")
        else:
            lib.return_book(user, book)
            print("Book returned")
    elif action == 6:
        if user.admin:
            for book in lib.list_books():
                print(book)
        else:
            print("Admin only")
    elif action == 7:
        if user.admin:
            lib.sort_books()
            print("Books sorted")
        else:
            print("Admin only")
    elif action == 8:
        if user.admin:
            title = input("Title: ")
            author = input("Author: ")
            lib.add_book(Book(title, author))
            print("Book added")
        else:
            print("Admin only")
    elif action == 9:
        if user.admin:
            title = input("Title: ")
            book = lib.query_book(title)
            if book is None:
                print("Book not found")
            else:
                lib.remove_book(book)
                print("Book removed")
        else:
            print("Admin only")
    elif action == 0:
        running = False
    else:
        print("Invalid action")
