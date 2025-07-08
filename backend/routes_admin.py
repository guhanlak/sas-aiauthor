from fastapi import APIRouter, Depends
from backend.auth import require_role

router = APIRouter()

@router.get("/users", dependencies=[Depends(require_role("admin"))])
async def list_users():
    # Placeholder: Return list of users
    return []
