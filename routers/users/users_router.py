from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

fake_user_db = [
    {"username": "teeruch"},
    {"username": "Chaiwat"},
]


@router.get("/")
def get_all_user():
    return fake_user_db
