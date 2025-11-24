# app/api/v1/users.py
from fastapi import APIRouter, HTTPException
from app.services.library_manager import library_manager
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=User)
def create_user(user: User):
    try:
        return library_manager.add_user(user)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{user_id}", response_model=User)
def get_user(user_id: str):
    user = library_manager.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
