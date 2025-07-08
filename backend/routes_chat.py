from fastapi import APIRouter, Depends
from backend.auth import get_current_user
from backend.schemas import ChatRequest, ChatResponse

router = APIRouter()

@router.post("/ask", response_model=ChatResponse)
async def ask_question(request: ChatRequest, user=Depends(get_current_user)):
    # Placeholder: Call OpenAI, style response, generate TTS audio
    return ChatResponse(response="Adiyogi-style answer", audio_url=None)
