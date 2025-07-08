import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
DB_NAME = "ai_author"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URI)
db = client[DB_NAME]

users_collection = db["users"]
books_collection = db["books"]
chat_collection = db["chat_messages"]

def get_user_collection():
    return users_collection

def get_book_collection():
    return books_collection

def get_chat_collection():
    return chat_collection
