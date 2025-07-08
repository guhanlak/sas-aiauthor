from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes_books import router as books_router
from backend.routes_admin import router as admin_router
from backend.routes_chat import router as chat_router
from backend.routes_users import router as users_router

app = FastAPI()

origins = [
    "http://localhost:3000",
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Import and include routers (to be implemented)
# from backend.routes_auth import router as auth_router
# from backend.routes_books import router as books_router
# from backend.routes_admin import router as admin_router
# from backend.routes_chat import router as chat_router
# from backend.routes_users import router as users_router

app.include_router(books_router, prefix="/books", tags=["books"])
app.include_router(admin_router, prefix="/admin", tags=["admin"])
app.include_router(chat_router, prefix="/chat", tags=["chat"])
app.include_router(users_router, prefix="/auth", tags=["auth"])

@app.get("/")
def root():
    return {"message": "Ai Author API is running"}
