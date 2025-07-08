from pydantic import BaseModel, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: Optional[str] = "user"

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class BookCreate(BaseModel):
    title: str
    author: str
    description: Optional[str]
    file_url: str

class BookResponse(BaseModel):
    id: str
    title: str
    author: str
    description: Optional[str]
    file_url: str
    uploaded_by: str
    uploaded_at: str

class ChatRequest(BaseModel):
    book_id: Optional[str]
    message: str

class ChatResponse(BaseModel):
    response: str
    audio_url: Optional[str]
