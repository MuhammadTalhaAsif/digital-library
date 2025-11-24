# digital-library/app/api/v1/books.py
from fastapi import APIRouter, HTTPException
from app.services.library_manager import library_manager
from app.models.book import Book

router = APIRouter()

@router.post("/", response_model=Book)
def create_book(book: Book):
    try:
        return library_manager.add_book(book)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{book_id}", response_model=Book)
def get_book(book_id: str):
    book = library_manager.get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book