from fastapi import APIRouter
from backend.schemas import UserCreate, UserLogin

router = APIRouter()

@router.post("/register")
async def register(user: UserCreate):
    # Placeholder: Register user in DB
    return {"message": "User registered"}

@router.post("/login")
async def login(user: UserLogin):
    # Placeholder: Authenticate user, return JWT
    return {"access_token": "jwt-token", "token_type": "bearer"}
