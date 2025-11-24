from app.models.book import Book
from app.models.user import User
from app.services.library_manager import LibraryManager

def test_borrow_and_return_book():
    manager = LibraryManager()

    # Add a book and a user
    book = Book(book_id="b1", title="1984", author="George Orwell")
    user = User(user_id="u1", name="Alice")
    manager.add_book(book)
    manager.add_user(user)

    # Borrow the book
    loan = manager.borrow_book(user_id="u1", book_id="b1")
    assert loan.book.is_available is False
    assert loan.user.user_id == "u1"

    # Return the book
    result = manager.return_book(book_id="b1")
    assert result is True
    assert book.is_available is True
