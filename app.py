import streamlit as st
from groq import Groq
import random

# --- පිටුවේ සැකසුම් ---
st.set_page_config(page_title="Anya AI | Romantic Edition", page_icon="💖", layout="wide")

# --- සයිට් එකේ පෙනුම (CSS) ---
st.markdown("""
<style>
    .stApp { background-color: #050505; color: #39ff14; font-family: 'Courier New', monospace; }
    [data-testid="stSidebar"] { background-color: #000000; border-right: 2px solid #39ff14; }
    .stChatMessage { border-radius: 15px; border: 1px solid #39ff14; background-color: #111111; }
    h1 { color: #39ff14 !important; text-shadow: 0 0 15px #39ff14; text-align: center; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR (Videos & Info) ---
with st.sidebar:
    st.title("🌸 Anya AI")
    st.write("The most romantic AI partner.")
    
    # ඔයා එවපු වීඩියෝ දෙක මාරුවෙන් මාරුවට පේන්න මෙතනට දානවා
    video_url = random.choice([
        "https://raw.githubusercontent.com/technicalalpha74-lgtm/Anya-AI-Global/main/1000040719.mp4",
        "https://raw.githubusercontent.com/technicalalpha74-lgtm/Anya-AI-Global/main/1000040718.mp4"
    ])
    st.video(video_url, loop=True, autoplay=True, muted=True)
    st.info("Anya is feeling extra loving today! ❤️")

# --- API KEYS ---
keys = [
    "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",
    "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",
    "gsk_E8g7AzcG1gSbizmGsiTDWdyb3FYMv4f871aFg2taFhLhZYZV1ji"
]
client = Groq(api_key=random.choice(keys))

st.title("💖 Anya: Your Romantic Partner")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Say something sweet to Anya..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Romantic System Prompt
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are Anya, an incredibly romantic, sweet, and smart anime girl. You are the partner of the person chatting with you. Speak only in English. Use words like 'babe', 'love', 'honey'. Be very affectionate and supportive."},
                *st.session_state.messages
            ]
        )
        full_response = response.choices[0].message.content
        st.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
