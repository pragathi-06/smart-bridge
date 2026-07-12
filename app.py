
# Smart Bridge v2.0 (starter)
import streamlit as st
from google import genai
from dotenv import load_dotenv
import os, wikipedia

load_dotenv()
api_key=os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("Gemini API key not found.")
    st.stop()

client=genai.Client(api_key=api_key)

st.set_page_config(page_title="Smart Bridge v2.0",
                   page_icon="🤝",
                   layout="wide",
                   initial_sidebar_state="expanded")

if "history" not in st.session_state:
    st.session_state.history=[]

with st.sidebar:
    st.title("🤝 Smart Bridge v2.0")
    st.markdown("AI-Powered Personalized Networking Assistant")
    st.divider()
    st.write("✅ Conversation Starters")
    st.write("✅ Networking Tips")
    st.write("✅ Wikipedia Search")
    st.write("✅ Download Results")

st.title("🤝 AI Personalized Networking Assistant")

c1,c2=st.columns(2)
with c1:
    name=st.text_input("Name")
    profession=st.selectbox("Profession",["Student","Professional","Entrepreneur"])
    experience=st.selectbox("Experience",["Student","Fresher","1-3 Years","Experienced"])
with c2:
    goal=st.selectbox("Networking Goal",["Internship","Job","Learning","Collaboration"])
    tone=st.selectbox("Conversation Style",["Professional","Friendly","Confident","Casual"])
    company=st.text_input("Company (Optional)")

event=st.text_input("Event Name")
desc=st.text_area("Event Description")

def generate():
    prompt=f"""
You are an AI Networking Assistant.

Name:{name}
Profession:{profession}
Experience:{experience}
Goal:{goal}
Tone:{tone}
Company:{company}
Event:{event}
Description:{desc}

Generate:
1. Five personalized conversation starters.
2. Three networking tips.
3. Two questions to ask attendees.
4. One LinkedIn connection message.
"""
    return client.models.generate_content(model="gemini-flash-latest",contents=prompt).text
if st.button("✨ Generate"):
    if event and desc:
        with st.spinner("🤖 Generating..."):
            try:
                result=generate()
                st.session_state.history.append(result)
                st.success("Done!")
                st.markdown(result)
                st.download_button("📥 Download",result,file_name="networking_suggestions.txt")
            except Exception as e:
                st.error(e)
    else:
        st.warning("Enter event details.")

st.divider()
topic=st.text_input("Wikipedia Topic")
if st.button("Search Wikipedia"):
    if topic:
        try:
            st.info(wikipedia.summary(topic,sentences=3))
        except Exception:
            st.error("No information found.")

if st.session_state.history:
    st.divider()
    st.subheader("History")
    for i,h in enumerate(reversed(st.session_state.history),1):
        with st.expander(f"Response {i}"):
            st.markdown(h)

st.divider()
st.caption("Developed by Pragathi & Pravallika")
