from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chatbot_service import ask_chatbot

router = APIRouter(
    prefix="/chatbot",
    tags=["Chatbot"]
)

class ChatRequest(BaseModel):
    question: str

@router.post("/chat")
def chat(request: ChatRequest):
    return ask_chatbot(request.question)