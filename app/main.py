# app/main.py
from fastapi import FastAPI
from app.api.v1.books import router as books_router
from app.api.v1.users import router as users_router
from app.api.v1.loans import router as loans_router

app = FastAPI(title="Digital Library")

app.include_router(books_router, prefix="/api/v1/books", tags=["Books"])
app.include_router(users_router, prefix="/api/v1/users", tags=["Users"])
app.include_router(loans_router, prefix="/api/v1/loans", tags=["Loans"])