# Personalized Networking Assistant

## Overview

Personalized Networking Assistant is an AI-powered web application that helps users generate personalized conversation starters for networking events. The application analyzes event descriptions, extracts important themes, generates context-aware networking prompts, verifies information using Wikipedia, and stores conversation history and user feedback.

The project is built using FastAPI, Streamlit, DistilBERT, GPT-2, and Wikipedia API.

---

## Features

- Event theme analysis using DistilBERT
- AI-powered conversation starter generation using GPT-2
- Fact checking using Wikipedia API
- Conversation history tracking
- User feedback collection
- FastAPI backend services
- Streamlit frontend interface
- Local JSON-based data storage
- API documentation with Swagger UI

---

## Technologies Used

- Python 3.13
- FastAPI
- Streamlit
- Hugging Face Transformers
- DistilBERT
- GPT-2
- Wikipedia API
- Pytest
- HTTPX
- JSON

---

## Project Structure

```text
personalized-networking-assistant/

├── app/
│   ├── services/
│   │   ├── event_analyzer.py
│   │   ├── topic_generator.py
│   │   ├── fact_checker.py
│   │   ├── history_logger.py
│   │   └── feedback_logger.py
│   │
│   ├── routes/
│   │   ├── event_routes.py
│   │   ├── conversation_routes.py
│   │   └── fact_routes.py
│   │
│   ├── data/
│   │   ├── history.json
│   │   └── feedback.json
│   │
│   ├── schemas.py
│   └── main.py
│
├── frontend/
│   └── streamlit_app.py
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd personalized-networking-assistant
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running FastAPI Backend

```bash
uvicorn app.main:app --reload
```

Backend URL:

```
http://127.0.0.1:8000
```
---

## Running Streamlit Frontend

```bash
streamlit run frontend/streamlit_app.py
```

Frontend URL:

```
http://localhost:8501
```

---

## API Endpoints

### Analyze Event

**POST**

```
/analyze-event/
```

Extracts themes from event descriptions.

### Generate Conversation

**POST**

```
/generate-conversation/
```

Generates networking conversation starters.

### Fact Check

**POST**

```
/fact-check/
```

Retrieves verified information from Wikipedia.

---

## Example Workflow

1. User enters an event description.
2. DistilBERT analyzes the event and identifies themes.
3. GPT-2 generates personalized conversation starters.
4. User can verify topics using the Fact Checker.
5. Generated conversations are stored in history.
6. User feedback is recorded for future improvements.

---

## Testing

Run all tests:

```bash
pytest
```

---

## Future Enhancements

- Database integration
- Advanced recommendation system
- User authentication
- Personalized AI profiles
- Cloud deployment

---

## Conclusion

The Personalized Networking Assistant demonstrates the integration of Natural Language Processing, Artificial Intelligence, FastAPI, and Streamlit to help users prepare for professional networking events through intelligent conversation suggestions and fact verification.