import streamlit as st
import requests
import json
import os

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Personalized Networking Assistant")

st.title("🤝 Personalized Networking Assistant")

event_description = st.text_area(
    "Event Description",
    placeholder="AI for Sustainable Cities Conference"
)

interests = st.text_input(
    "Interests (comma separated)",
    placeholder="AI, Climate Change, Urban Planning"
)

if st.button("Generate Conversation Starters"):

    if event_description:

        interest_list = [
            i.strip()
            for i in interests.split(",")
            if i.strip()
        ]

        payload = {
            "event_description": event_description,
            "interests": interest_list
        }

        try:
            response = requests.post(
                f"{API_URL}/generate-conversation/",
                json=payload
            )

            if response.status_code == 200:

                data = response.json()

                st.subheader("Detected Themes")

                for theme in data["themes"]:
                    st.write(f"• {theme}")

                st.subheader("Conversation Starters")

                for starter in data["conversation_starters"]:

                    st.success(starter)

                    col1, col2 = st.columns(2)

                    with col1:
                        if st.button(
                            "👍 Useful",
                            key=f"u_{starter}"
                        ):
                            feedback = {
                                "conversation_starter": starter,
                                "feedback": "Useful"
                            }

                            file_path = "app/data/feedback.json"

                            if os.path.exists(file_path):
                                with open(file_path, "r", encoding="utf-8") as f:
                                    data_list = json.load(f)
                            else:
                                data_list = []

                            data_list.append(feedback)

                            with open(file_path, "w", encoding="utf-8") as f:
                                json.dump(data_list, f, indent=4)

                            st.success("Feedback Saved")

                    with col2:
                        if st.button(
                            "👎 Not Useful",
                            key=f"d_{starter}"
                        ):
                            feedback = {
                                "conversation_starter": starter,
                                "feedback": "Not Useful"
                            }

                            file_path = "app/data/feedback.json"

                            if os.path.exists(file_path):
                                with open(file_path, "r", encoding="utf-8") as f:
                                    data_list = json.load(f)
                            else:
                                data_list = []

                            data_list.append(feedback)

                            with open(file_path, "w", encoding="utf-8") as f:
                                json.dump(data_list, f, indent=4)

                            st.success("Feedback Saved")

            else:
                st.error("Failed to generate conversation starters")

        except Exception as e:
            st.error(str(e))

st.header("Fact Checker")

topic = st.text_input(
    "Enter Topic",
    placeholder="Blockchain in Healthcare"
)

if st.button("Fact Check"):

    try:
        response = requests.post(
            f"{API_URL}/fact-check/",
            json={"topic": topic}
        )

        if response.status_code == 200:

            result = response.json()

            st.write(result["summary"])
            st.caption(f"Source: {result['source']}")

        else:
            st.error("Fact Check Failed")

    except Exception as e:
        st.error(str(e))

st.header("Conversation History")

history_file = "app/data/history.json"

if os.path.exists(history_file):

    with open(history_file, "r", encoding="utf-8") as f:
        history = json.load(f)

    if history:
        for item in reversed(history):
            with st.expander(item["event_description"]):
                st.json(item)
    else:
        st.info("No history available")

st.header("Feedback History")

feedback_file = "app/data/feedback.json"

if os.path.exists(feedback_file):

    with open(feedback_file, "r", encoding="utf-8") as f:
        feedback_data = json.load(f)

    if feedback_data:
        st.json(feedback_data)
    else:
        st.info("No feedback available")