from fastapi import FastAPI

from app.routes.event_routes import router as event_router
from app.routes.conversation_routes import router as conversation_router
from app.routes.fact_routes import router as fact_router

app = FastAPI(
    title="Personalized Networking Assistant",
    description="AI-powered networking assistant using DistilBERT, GPT-2, FastAPI and Streamlit.",
    version="1.0.0"
)

app.include_router(event_router)
app.include_router(conversation_router)
app.include_router(fact_router)


@app.get("/")
def home():
    return {
        "message": "Personalized Networking Assistant API is running successfully."
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }