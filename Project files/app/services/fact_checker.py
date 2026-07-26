import wikipedia


def fact_check(topic: str):
    """
    Fetch a short verified summary from Wikipedia.
    """

    try:
        summary = wikipedia.summary(topic, sentences=3)

        return {
            "topic": topic,
            "summary": summary,
            "source": "Wikipedia"
        }

    except wikipedia.exceptions.DisambiguationError as e:
        return {
            "topic": topic,
            "summary": f"Multiple topics found. Try one of these: {', '.join(e.options[:5])}",
            "source": "Wikipedia"
        }

    except wikipedia.exceptions.PageError:
        return {
            "topic": topic,
            "summary": "No matching Wikipedia page found.",
            "source": "Wikipedia"
        }

    except Exception as e:
        return {
            "topic": topic,
            "summary": f"Error: {str(e)}",
            "source": "Wikipedia"
        }