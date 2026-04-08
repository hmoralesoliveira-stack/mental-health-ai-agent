from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    return ChatResponse(
        reply=(
            "Obrigado por compartilhar isso comigo. "
            "Você quer me contar um pouco mais sobre o que está sentindo?"
        )
    )
