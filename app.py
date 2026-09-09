import streamlit as st
from bot import QuickBot

st.set_page_config(page_title="Mental Health Bot", page_icon="🧠", layout="centered")

if 'bot' not in st.session_state:
    st.session_state.bot = QuickBot()
    st.session_state.messages = []

with st.sidebar:
    st.title("Mental Health Bot")
    st.write("Not therapy! Call 988 for crisis.")
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

st.title("Mental Health Support")

if len(st.session_state.messages) == 0:
    with st.chat_message("assistant"):
        st.write("Hello! How are you feeling today?")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["text"])
        if msg.get("emotion"):
            emojis = {"happy":"😊","sad":"😢","anxious":"😰","angry":"😠","crisis":"CRISIS","neutral":"😐"}
            st.caption(f"{emojis.get(msg['emotion'])} - {msg['emotion']}")

if prompt := st.chat_input("How are you feeling?"):
    st.session_state.messages.append({"role":"user","text":prompt,"emotion":None})
    with st.chat_message("user"):
        st.write(prompt)
    
    response, emotion = st.session_state.bot.get_response(prompt)
    
    if emotion == 'crisis':
        st.error("CRISIS - CALL 988!")
    
    st.session_state.messages.append({"role":"assistant","text":response,"emotion":emotion})
    
    with st.chat_message("assistant"):
        st.write(response)
        emojis = {"happy":"😊","sad":"😢","anxious":"😰","angry":"😠","crisis":"CRISIS","neutral":"😐"}
        st.caption(f"{emojis.get(emotion)} - {emotion}")

st.write("---")
st.caption("AI Mental Health Chatbot")
