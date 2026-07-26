from fastapi import APIRouter
from app.schemas import (
    FactCheckRequest,
    FactCheckResponse
)

from app.services.fact_checker import fact_check

router = APIRouter(
    prefix="/fact-check",
    tags=["Fact Checker"]
)


@router.post("/", response_model=FactCheckResponse)
def fact_check_route(request: FactCheckRequest):
    """
    Verify a topic using Wikipedia.
    """

    result = fact_check(request.topic)

    return result