from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from models.database import get_db
from models.users.users_model import UserBase, UserDisplayBase

from routers.users import user_controller


router = APIRouter(prefix="/users", tags=["users"])

fake_user_db = [
    {"username": "teeruch"},
    {"username": "Chaiwat"},
]


@router.get("/")
def get_all_user():
    return fake_user_db

@router.post("/")
def register_user(request: UserBase, db: Session= Depends(get_db)):
    return user_controller.create(db, request)
