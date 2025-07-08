from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
from backend.config import JWT_SECRET_KEY, JWT_ALGORITHM
from backend.models import User

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

# Password hashing

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

# JWT token

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    if not JWT_SECRET_KEY or not JWT_ALGORITHM:
        raise RuntimeError("JWT_SECRET_KEY and JWT_ALGORITHM must be set")
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=60))
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    if not JWT_SECRET_KEY or not JWT_ALGORITHM:
        raise RuntimeError("JWT_SECRET_KEY and JWT_ALGORITHM must be set")
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_ALGORITHM])
        return payload
    except JWTError:
        return None

# Dependency to get current user
async def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    # Fetch user from DB (pseudo, replace with actual DB call)
    # user = await get_user_by_id(user_id)
    user = User(_id=user_id, email="test@example.com", hashed_password="", role=payload.get("role", "user"))
    return user

def require_role(role: str):
    async def role_dependency(current_user: User = Depends(get_current_user)):
        if current_user.role != role:
            raise HTTPException(status_code=403, detail="Insufficient permissions")
        return current_user
    return role_dependency
