from typing import List
from .user import User
from .book import Book


class Library:
    def __init__(self):
        self.books: List[Book] = []
        self.users: List[User] = []

    def add_user(self, user: User):
        self.users.append(user)

    def login(self, name: str, password: str):
        for user in self.users:
            if user.name == name and user.password == password:
                return user
        return None

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        self.books.append(book)

    def query_book(self, title: str):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def list_books(self):
        return self.books

    def sort_books(self):
        self.books.sort(key=lambda x: x.title)

    def borrow_book(self, user: User, book: Book):
        if book in self.books:
            user.books.append(book)
            self.books.remove(book)

    def return_book(self, user: User, book: Book):
        if book in user.books:
            user.books.remove(book)
            self.books.append(book)
