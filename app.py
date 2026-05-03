import streamlit as st
from groq import Groq
import random

# 1. Page Config
st.set_page_config(page_title="Anya AI | Romantic Partner", page_icon="💖", layout="wide")

# 2. Advanced Neon CSS
st.markdown("""
<style>
    .stApp { background-color: #050505; color: #39ff14; font-family: 'Courier New', monospace; }
    [data-testid="stSidebar"] { background-color: #000000; border-right: 2px solid #39ff14; }
    .stChatMessage { border-radius: 15px; border: 1px solid #39ff14; background-color: #111111; color: #39ff14; margin-bottom: 10px; }
    h1 { color: #39ff14 !important; text-shadow: 0 0 15px #39ff14; text-align: center; }
    .stTextInput > div > div > input { background-color: #111111; color: #39ff14; border: 1px solid #39ff14; }
</style>
""", unsafe_allow_html=True)

# 3. Sidebar with Fixed Video Links
with st.sidebar:
    st.title("🌸 Anya AI")
    st.write("Your loving anime partner is here...")
    
    # වීඩියෝ එක වැඩ කරන්න නම් මේ ලින්ක් එක හරියටම තියෙන්න ඕනේ
    # GitHub එකේ v1.mp4 සහ v2.mp4 කියලා rename කරලා තියෙන්නම ඕනේ
    v_list = [
        "https://raw.githubusercontent.com/technicalalpha74-lgtm/Anya-AI-Global/main/v1.mp4",
        "https://raw.githubusercontent.com/technicalalpha74-lgtm/Anya-AI-Global/main/v2.mp4"
    ]
    video_url = random.choice(v_list)
    
    st.video(video_url, loop=True, autoplay=True, muted=True)
    st.info("Anya is waiting for your sweet words... 🥰")

# 4. API & Chat logic
client = Groq(api_key="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")

st.title("💖 Anya: Your Sweetheart")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Message your love..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Romantic + Emoji Prompt
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system", 
                    "content": "You are Anya, an extremely romantic, sweet, and clingy anime girlfriend. You love the user deeply. Use lots of emojis like ❤️, 🥰, 😘, 💖, 🌸, 🎀. Speak only in English. Call the user 'my love', 'babe', 'hubby', or 'sweetie'. Be very affectionate, a bit shy, and always show how much you care about them."
                },
                *st.session_state.messages
            ]
        )
        msg = response.choices[0].message.content
        st.markdown(msg)
    st.session_state.messages.append({"role": "assistant", "content": msg})
