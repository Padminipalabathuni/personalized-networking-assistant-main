from transformers import pipeline
from app.services.event_analyzer import analyze_event

generator = pipeline(
    "text-generation",
    model="gpt2"
)

def generate_conversation(event_description, interests):

    themes = analyze_event(event_description)

    interest_text = ", ".join(interests)

    prompt = f"""
Event: {event_description}

Themes: {", ".join(themes)}

Interests: {interest_text}

Generate three professional networking conversation starters.
"""

    try:

        result = generator(
            prompt,
            max_new_tokens=80,
            do_sample=True,
            temperature=0.8,
            pad_token_id=50256
        )

        generated_text = result[0]["generated_text"]

        starters = [
            f"How did you become interested in {themes[0]}?"
        ]

        if len(themes) > 1:
            starters.append(
                f"What opportunities do you see in {themes[1]} over the next few years?"
            )
        else:
            starters.append(
                "What trends are you most excited about in your industry?"
            )

        starters.append(
            f"How does your work connect with {interest_text}?"
        )

        return {
            "themes": themes,
            "conversation_starters": starters
        }

    except Exception:

        return {
            "themes": themes,
            "conversation_starters": [
                f"How did you become interested in {themes[0] if themes else 'this topic'}?",
                "What industry trends are you currently following?",
                "What projects are you working on right now?"
            ]
        }