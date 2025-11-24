# app/models/book.py
from pydantic import BaseModel

class Book(BaseModel):
    book_id: str
    title: str
    author: str
    is_available: bool = True

    def mark_borrowed(self):
        self.is_available = False
    
    def mark_returned(self):
        self.is_available = True

