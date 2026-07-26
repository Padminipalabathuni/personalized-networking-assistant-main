from pydantic import BaseModel
from typing import List


class EventRequest(BaseModel):
    event_description: str


class ConversationRequest(BaseModel):
    event_description: str
    interests: List[str]


class FactCheckRequest(BaseModel):
    topic: str


class FeedbackRequest(BaseModel):
    conversation_starter: str
    feedback: str


class EventResponse(BaseModel):
    themes: List[str]


class ConversationResponse(BaseModel):
    themes: List[str]
    conversation_starters: List[str]


class FactCheckResponse(BaseModel):
    topic: str
    summary: str
    source: str


class FeedbackResponse(BaseModel):
    message: str