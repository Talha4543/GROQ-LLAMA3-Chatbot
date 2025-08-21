import streamlit as st
import requests

# 🔑 Replace with your Groq API key from https://console.groq.com/keys
GROQ_API_KEY = "your_api_key"
API_URL = "https://api.groq.com/openai/v1/chat/completions"

st.set_page_config(page_title="Groq ChatBot", page_icon="⚡", layout="centered")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("🤖 Groq ChatBot (LLaMA 3)")

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input
user_prompt = st.chat_input("Ask Groq (LLaMA 3)...")

if user_prompt:
    st.chat_message("user").markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    headers = {"Authorization": f"Bearer {GROQ_API_KEY}"}
    payload = {
        "model": "llama3-8b-8192",  # free Groq model
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            *st.session_state.chat_history
        ]
    }

    response = requests.post(API_URL, headers=headers, json=payload)
    data = response.json()
    assistant_response = data["choices"][0]["message"]["content"]

    st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})

    with st.chat_message("assistant"):
        st.markdown(assistant_response)
