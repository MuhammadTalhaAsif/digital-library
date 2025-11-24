# app/models/loan.py
from pydantic import BaseModel
from app.models.book import Book
from app.models.user import User
from datetime import datetime

class Loan(BaseModel):
    loan_id: str
    book: Book
    user: User
    borrowed_at: datetime = datetime.utcnow()