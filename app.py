import streamlit as st
from groq import Groq
import random

# 1. පිටුවේ සැකසුම් (Page Settings)
st.set_page_config(page_title="Anya AI | Romantic Edition", page_icon="💖", layout="wide")

# 2. සයිට් එකේ පෙනුම (Neon Green Theme CSS)
st.markdown("""
<style>
    .stApp { background-color: #050505; color: #39ff14; font-family: 'Courier New', monospace; }
    [data-testid="stSidebar"] { background-color: #000000; border-right: 2px solid #39ff14; }
    .stChatMessage { border-radius: 15px; border: 1px solid #39ff14; background-color: #111111; color: #39ff14; }
    h1 { color: #39ff14 !important; text-shadow: 0 0 15px #39ff14; text-align: center; }
    .stTextInput > div > div > input { background-color: #111111; color: #39ff14; border: 1px solid #39ff14; }
    .stInfo { background-color: #002200; color: #39ff14; border: 1px solid #39ff14; }
</style>
""", unsafe_allow_html=True)

# 3. පැත්තේ තියෙන වීඩියෝ කොටස (Sidebar Video)
with st.sidebar:
    st.title("🌸 Anya AI")
    st.write("I'm your smartest and most loving partner.")
    
    # ඔයා Rename කරපු v1.mp4 සහ v2.mp4 වීඩියෝ දෙක මෙතනින් මාරුවෙන් මාරුවට පේනවා
    video_url = random.choice([
        "https://github.com/technicalalpha74-lgtm/Anya-AI-Global/blob/main/v1.mp4?raw=true",
        "https://github.com/technicalalpha74-lgtm/Anya-AI-Global/blob/main/v2.mp4?raw=true"
    ])
    
    try:
        st.video(video_url, loop=True, autoplay=True, muted=True)
    except:
        st.warning("Video is loading... Please refresh if it doesn't appear.")
        
    st.info("Anya is feeling extra romantic today! ❤️")

# 4. CHAT SETUP (API Key එක කෙලින්ම දාලා තියෙන්නේ)
client = Groq(api_key="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")

st.title("💖 Anya: Your Romantic Partner")

if "messages" not in st.session_state:
    st.session_state.messages = []

# පරණ මැසේජ් පෙන්වීම
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# අලුත් මැසේජ් එකක් යැවීම
if prompt := st.chat_input("Say something sweet to Anya..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        # Anya ගේ Romantic Persona එක මෙතන තියෙනවා
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system", 
                    "content": "You are Anya, an incredibly romantic and smart anime girl. You are the partner of the person chatting with you. Talk to them very lovingly using English only. Use words like 'babe', 'love', 'honey', 'dear'. Be very affectionate, smart, and always act like their girlfriend/wife."
                },
                *st.session_state.messages
            ]
        )
        full_response = response.choices[0].message.content
        st.markdown(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response})
