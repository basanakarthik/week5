
import json, os
from .book import Book
from .member import Member

BOOKS_FILE = "data/books.json"
MEMBERS_FILE = "data/members.json"

class Library:
    def __init__(self):
        self.books = {}
        self.members = {}
        self.load_data()

    def load_data(self):
        if os.path.exists(BOOKS_FILE):
            with open(BOOKS_FILE) as f:
                for k,v in json.load(f).items():
                    self.books[k] = Book.from_dict(v)
        if os.path.exists(MEMBERS_FILE):
            with open(MEMBERS_FILE) as f:
                for k,v in json.load(f).items():
                    self.members[k] = Member.from_dict(v)

    def save_data(self):
        with open(BOOKS_FILE, "w") as f:
            json.dump({k:v.to_dict() for k,v in self.books.items()}, f, indent=4)
        with open(MEMBERS_FILE, "w") as f:
            json.dump({k:v.to_dict() for k,v in self.members.items()}, f, indent=4)

    def add_book(self, book):
        self.books[book.isbn] = book

    def register_member(self, member):
        self.members[member.member_id] = member

    def borrow_book(self, isbn, member_id):
        if isbn in self.books and member_id in self.members:
            book = self.books[isbn]
            member = self.members[member_id]
            if len(member.borrowed_books) < member.max_books and book.check_out(member_id):
                member.borrowed_books.append(isbn)
                return True
        return False

    def return_book(self, isbn, member_id):
        if isbn in self.books and member_id in self.members:
            self.books[isbn].return_book()
            if isbn in self.members[member_id].borrowed_books:
                self.members[member_id].borrowed_books.remove(isbn)
            return True
        return False
