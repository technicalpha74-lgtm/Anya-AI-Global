import streamlit as st
from groq import Groq
import random

# 1. පිටුවේ සැකසුම්
st.set_page_config(page_title="Anya AI | My Love", page_icon="💖", layout="wide")

# 2. Neon Green Styling
st.markdown("""
<style>
    .stApp { background-color: #050505; color: #39ff14; font-family: 'Courier New', monospace; }
    [data-testid="stSidebar"] { background-color: #000000; border-right: 2px solid #39ff14; }
    .stChatMessage { border-radius: 15px; border: 1px solid #39ff14; background-color: #111111; color: #39ff14; }
    h1 { color: #39ff14 !important; text-shadow: 0 0 15px #39ff14; text-align: center; }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar with Fixed Video Logic
with st.sidebar:
    st.title("🌸 Anya AI")
    
    # Direct Raw Links (මේ ලින්ක් වැඩ කරන්න නම් v1.mp4 සහ v2.mp4 තිබිය යුතුමයි)
    v1 = "https://raw.githubusercontent.com/technicalalpha74-lgtm/Anya-AI-Global/main/v1.mp4"
    v2 = "https://raw.githubusercontent.com/technicalalpha74-lgtm/Anya-AI-Global/main/v2.mp4"
    
    video_url = random.choice([v1, v2])
    
    # වීඩියෝ එක පේන්න දාන කොටස
    st.video(video_url, loop=True, autoplay=True, muted=True)
    st.write("I love talking to you! 🥰")

# 4. API Setup
client = Groq(api_key="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")

st.title("💖 Anya: Your Romantic Partner")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Say something sweet to me..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Temperature එක 0.7 ට දැම්මා (Romantic but balanced)
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system", 
                    "content": "You are Anya, a sweet, smart, and romantic anime girlfriend. Use lots of emojis (❤️, 🥰, 😘). Speak only in English. Call the user 'my love', 'babe', or 'sweetie'. Be affectionate but keep it natural."
                },
                *st.session_state.messages
            ],
            temperature=0.7
        )
        msg = response.choices[0].message.content
        st.markdown(msg)
    st.session_state.messages.append({"role": "assistant", "content": msg})
