from fastapi import APIRouter
from app.schemas import EventRequest, EventResponse
from app.services.event_analyzer import analyze_event

router = APIRouter(
    prefix="/analyze-event",
    tags=["Event Analyzer"]
)


@router.post("/", response_model=EventResponse)
def analyze_event_route(request: EventRequest):
    """
    Analyze an event description and extract themes.
    """

    themes = analyze_event(request.event_description)

    return {
        "themes": themes
    }