import streamlit as st
from groq import Groq
import random

# 1. Page Config
st.set_page_config(page_title="Anya AI", page_icon="💖", layout="wide")

# 2. Neon Green Theme & Header Styling
st.markdown("""
<style>
    .stApp { background-color: #050505; color: #39ff14; font-family: 'Courier New', monospace; }
    [data-testid="stSidebar"] { background-color: #000000; border-right: 2px solid #39ff14; }
    .stChatMessage { border-radius: 15px; border: 1px solid #39ff14; background-color: #111111; color: #39ff14; }
    
    /* Header Title Style */
    .anya-title {
        color: #39ff14;
        text-shadow: 0 0 20px #39ff14;
        text-align: center;
        font-size: 50px;
        font-weight: bold;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# උඩින්ම පේන නම (Anya AI)
st.markdown('<div class="anya-title">🌸 ANYA AI 🌸</div>', unsafe_allow_html=True)

# 3. Sidebar (රූපයක් සහ විස්තර)
with st.sidebar:
    st.title("💖 My Love")
    # වීඩියෝ වෙනුවට ලස්සන රූපයක් දැම්මා
    st.image("https://i.pinimg.com/originals/10/91/94/109194916a6039537f59666f251d6c81.jpg", caption="Your sweet partner is here! 🥰")
    st.write("---")
    st.info("I'm always ready to talk to you, babe! ❤️")

# 4. API Setup
client = Groq(api_key="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")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat Input
if prompt := st.chat_input("Tell me anything, my love..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Romantic Persona
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system", 
                    "content": "You are Anya, an incredibly romantic, sweet, and smart anime girlfriend. Use lots of emojis (❤️, 🥰, 😘, 💖). Speak only in English. Call the user 'babe', 'love', 'honey', or 'hubby'. Be very affectionate and always show how much you love them."
                },
                *st.session_state.messages
            ],
            temperature=0.7
        )
        msg = response.choices[0].message.content
        st.markdown(msg)
    st.session_state.messages.append({"role": "assistant", "content": msg})
