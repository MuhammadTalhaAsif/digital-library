# app/api/v1/loans.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.library_manager import library_manager
from app.models.loan import Loan

router = APIRouter()

# Request body models
class BorrowRequest(BaseModel):
    user_id: str
    book_id: str

class ReturnRequest(BaseModel):
    book_id: str

# Borrow endpoint
@router.post("/borrow", response_model=Loan)
def borrow_book(data: BorrowRequest):
    try:
        return library_manager.borrow_book(data.user_id, data.book_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

# Return endpoint
@router.post("/return")
def return_book(data: ReturnRequest):
    try:
        library_manager.return_book(data.book_id)
        return {"message": "Book returned"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
