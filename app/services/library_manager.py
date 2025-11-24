# app/services/library_manager.py
import uuid
from typing import Dict, List
from app.models.book import Book
from app.models.user import User
from app.models.loan import Loan

class LibraryManager:
    def __init__(self):
        self.books: Dict[str, Book] = {}
        self.users: Dict[str, User] = {}
        self.loans: Dict[str, Loan] = {}

    
    # Book Operations
    def add_book(self, book: Book):
        if book.book_id in self.books:
            raise ValueError("Book with this ID already exists.")
        self.books[book.book_id] = book
        return book

    def get_book(self, book_id: str) -> Book:
        return self.books.get(book_id)
    
    # User Operations
    def add_user(self, user: User):
        if user.user_id in self.users:
            raise ValueError("User already exists")
        self.users[user.user_id] = user
        return user

    def get_user(self, user_id: str) -> User:
        return self.users.get(user_id)

    # Loan operations
    def borrow_book(self, user_id: str, book_id: str) -> Loan:
        book = self.get_book(book_id)
        user = self.get_user(user_id)
        if not book:
            raise ValueError("Book not found")
        if not user:
            raise ValueError("User not found")
        if not book.is_available:
            raise ValueError("Book not available")
        book.mark_borrowed()
        loan_id = str(uuid.uuid4())
        loan = Loan(loan_id=loan_id, book=book, user=user)
        self.loans[loan_id] = loan
        return loan

    def return_book(self, book_id: str):
        book = self.get_book(book_id)
        if not book:
            raise ValueError("Book not found")
        book.mark_returned()
        # remove loan(s) referencing this book
        to_delete = [lid for lid, l in self.loans.items() if l.book.book_id == book_id]
        for lid in to_delete:
            del self.loans[lid]
        return True

library_manager = LibraryManager()