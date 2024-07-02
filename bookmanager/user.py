from typing import List
from .book import Book


class User:
    def __init__(self, name: str, password: str, admin: bool = False):
        self.name = name
        self.password = password
        self.admin = admin
        self.books: List[Book] = []

    def list_books(self):
        return self.books
