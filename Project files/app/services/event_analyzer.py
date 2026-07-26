from transformers import pipeline

# DistilBERT-based text classification pipeline
classifier = pipeline(
    "text-classification",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)

# Predefined networking/event themes
CANDIDATE_THEMES = [
    "Artificial Intelligence",
    "Machine Learning",
    "Data Science",
    "Blockchain",
    "Healthcare",
    "Climate Change",
    "Sustainability",
    "Urban Planning",
    "Cybersecurity",
    "Cloud Computing",
    "Education",
    "Finance",
    "Marketing",
    "Entrepreneurship",
    "Technology"
]


def analyze_event(event_description: str):
    """
    Extract themes from an event description.
    Since DistilBERT is not a true zero-shot model,
    we combine it with keyword matching.
    """

    text = event_description.lower()

    detected_themes = []

    for theme in CANDIDATE_THEMES:
        words = theme.lower().split()

        for word in words:
            if word in text:
                detected_themes.append(theme)
                break

    if not detected_themes:
        result = classifier(event_description)

        if result[0]["label"] == "POSITIVE":
            detected_themes = ["Technology", "Innovation"]
        else:
            detected_themes = ["General Networking"]

    return list(set(detected_themes))