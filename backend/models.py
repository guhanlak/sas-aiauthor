from pydantic import BaseModel, Field, EmailStr
from typing import Optional, List
from datetime import datetime

class User(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    email: EmailStr
    hashed_password: str
    role: str = "user"  # 'user' or 'admin'
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Book(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    title: str
    author: str
    description: Optional[str]
    file_url: str
    uploaded_by: str  # user id
    uploaded_at: datetime = Field(default_factory=datetime.utcnow)
    embedding_id: Optional[str]

class ChatMessage(BaseModel):
    id: Optional[str] = Field(None, alias="_id")
    user_id: str
    book_id: Optional[str]
    message: str
    response: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
