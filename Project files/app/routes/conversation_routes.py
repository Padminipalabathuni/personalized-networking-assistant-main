from fastapi import APIRouter
from app.schemas import (
    ConversationRequest,
    ConversationResponse
)

from app.services.topic_generator import generate_conversation
from app.services.history_logger import save_history

router = APIRouter(
    prefix="/generate-conversation",
    tags=["Conversation Generator"]
)


@router.post("/", response_model=ConversationResponse)
def generate_conversation_route(request: ConversationRequest):
    """
    Generate personalized networking conversation starters.
    """

    result = generate_conversation(
        request.event_description,
        request.interests
    )

    save_history(
        event_description=request.event_description,
        interests=request.interests,
        themes=result["themes"],
        conversation_starters=result["conversation_starters"]
    )

    return {
        "themes": result["themes"],
        "conversation_starters": result["conversation_starters"]
    }