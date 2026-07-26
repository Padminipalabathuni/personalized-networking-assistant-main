import json
import os
from datetime import datetime

HISTORY_FILE = "app/data/history.json"


def _ensure_file_exists():
    """
    Create history.json if it does not exist.
    """
    os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)

    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


def save_history(event_description, interests, themes, conversation_starters):
    """
    Save generated conversation history.
    """

    _ensure_file_exists()

    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "event_description": event_description,
        "interests": interests,
        "themes": themes,
        "conversation_starters": conversation_starters
    }

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        history = json.load(file)

    history.append(entry)

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def get_history():
    """
    Return all saved conversation history.
    """

    _ensure_file_exists()

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)