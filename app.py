import streamlit as st
from groq import Groq
import random

st.set_page_config(page_title="Anya AI | My Love", page_icon="💖", layout="wide")

# Neon Green Style
st.markdown("""
<style>
    .stApp { background-color: #050505; color: #39ff14; font-family: 'Courier New', monospace; }
    [data-testid="stSidebar"] { background-color: #000000; border-right: 2px solid #39ff14; }
    .stChatMessage { border-radius: 15px; border: 1px solid #39ff14; background-color: #111111; color: #39ff14; }
    h1 { color: #39ff14 !important; text-shadow: 0 0 15px #39ff14; }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.title("🌸 Anya AI")
    # Working Direct Video Links
    v_url = random.choice([
        "https://statusparadiise.com/wp-content/uploads/2023/10/Anime-Girl-Edit-Status-Video-Download.mp4",
        "https://statusgood.com/wp-content/uploads/2023/06/Cute-Anime-Girl-Status-Video.mp4"
    ])
    st.video(v_url, loop=True, autoplay=True, muted=True)
    st.info("I'm always watching over you, babe! ❤️")

client = Groq(api_key="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")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Talk to your Anya..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system", "content": "You are Anya, a smart and incredibly romantic anime girl. Use lots of emojis (❤️, 🥰). English only. Call the user babe, love or hubby."},
                *st.session_state.messages
            ],
            temperature=0.7
        )
        msg = response.choices[0].message.content
        st.markdown(msg)
    st.session_state.messages.append({"role": "assistant", "content": msg})
