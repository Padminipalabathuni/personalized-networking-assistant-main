import json
import os
from datetime import datetime

FEEDBACK_FILE = "app/data/feedback.json"


def _ensure_file_exists():
    """
    Create feedback.json if it does not exist.
    """

    os.makedirs(os.path.dirname(FEEDBACK_FILE), exist_ok=True)

    if not os.path.exists(FEEDBACK_FILE):
        with open(FEEDBACK_FILE, "w", encoding="utf-8") as file:
            json.dump([], file, indent=4)


def save_feedback(conversation_starter, feedback):
    """
    Save user feedback.
    feedback should be:
    - Useful
    - Not Useful
    """

    _ensure_file_exists()

    entry = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "conversation_starter": conversation_starter,
        "feedback": feedback
    }

    with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
        feedback_data = json.load(file)

    feedback_data.append(entry)

    with open(FEEDBACK_FILE, "w", encoding="utf-8") as file:
        json.dump(feedback_data, file, indent=4)


def get_feedback():
    """
    Return all stored feedback.
    """

    _ensure_file_exists()

    with open(FEEDBACK_FILE, "r", encoding="utf-8") as file:
        return json.load(file)