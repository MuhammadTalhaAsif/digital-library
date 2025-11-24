from app.models.book import Book
from app.services.library_manager import LibraryManager

def test_add_book():
    manager = LibraryManager()
    book = Book(book_id="b_test", title="Test Book", author="Author")
    result = manager.add_book(book)
    assert result.book_id == "b_test"
    assert result.is_available is True