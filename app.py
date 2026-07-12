import streamlit as st
from google import genai
from dotenv import load_dotenv
import os
import wikipedia

# Load API Key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    st.error("Gemini API key not found. Please check your .env file.")
    st.stop()

# Gemini Client
client = genai.Client(api_key=api_key)


# Page Configuration
st.set_page_config(
    page_title="Smart Bridge",
    page_icon="🤝",
    layout="centered"
)
with st.sidebar:
    st.header("🤝 Smart Bridge")
    st.write("AI-Powered Personalized Networking Assistant")
    st.write("---")
    st.write("### Features")
    st.write("✅ AI Conversation Starters")
    st.write("✅ Networking Tips")
    st.write("✅ Wikipedia Search")


# Title
st.title("🤝 Smart Bridge")
st.markdown("### AI-Powered Personalized Networking Assistant")
st.write(
    "Build meaningful professional connections using AI-generated personalized networking suggestions."
)

st.write(
    "Generate smart conversation starters and networking tips "
    "for professional events using AI."
)

st.subheader("👤 Your Profile")

name = st.text_input(
    "Your Name",
    placeholder="Enter your name"
)

profession = st.selectbox(
    "Profession",
    ["Student", "Professional", "Entrepreneur"]
)

goal = st.selectbox(
    "Networking Goal",
    ["Internship", "Job", "Learning", "Collaboration"]
)

# Inputs
event_name = st.text_input(
    "Enter Event Name",
    placeholder="Example: AI Innovation Summit"
)

event_description = st.text_area(
    "Describe the Event",
    placeholder="Example: A conference about AI, ML and emerging technologies."
)


# Gemini Function
def generate_suggestions(event, description):

    prompt = f"""
You are an AI-powered Personalized Networking Assistant.

User Profile:
Name: {name}
Profession: {profession}
Networking Goal: {goal}

Event Name:
{event}

Event Description:
{description}

Generate:

1. Five personalized conversation starters based on the user's profession and networking goal.
2. Three networking tips specific to the user's goal.
3. Two interesting questions the user can ask other attendees.

Keep the response friendly, professional, and easy to use.
"""

    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=prompt
    )

    return response.text


# Generate Button
if st.button("✨ Generate Conversation Starters"):

    if event_name and event_description:

        with st.spinner("Generating suggestions..."):

            try:
                result = generate_suggestions(
                    event_name,
                    event_description
                )

                st.success("Suggestions Generated!")

                st.markdown(result)

            except Exception as e:
                st.error(f"Error: {e}")

    else:
        st.warning("Please enter event name and description.")


# Wikipedia Section
st.divider()

st.subheader("🔍 Explore Topics")

topic = st.text_input(
    "Enter a topic to search"
)

if st.button("Search Wikipedia"):

    if topic:
        try:
            summary = wikipedia.summary(
                topic,
                sentences=3
            )

            st.info(summary)

        except:
            st.error("No information found.")

    else:
        st.warning("Please enter a topic.")
st.divider()
st.caption("Developed by Pragathi & Pravallika")