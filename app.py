import streamlit as st
from huggingface_hub import InferenceClient
import os

# 1. Page Config
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

# 2. Sidebar - Setup & Clear Button
with st.sidebar:
    st.title("Settings")
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("Created by [Your Name]")

# 3. Setup Client
token = os.getenv("HF_API_TOKEN")
client = InferenceClient(token=token)
MODEL_ID = "Qwen/Qwen2.5-7B-Instruct"

st.title("My AI Assistant")

# 4. Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []

# 5. Display Chat History
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 6. Chat Input Logic
if prompt := st.chat_input("Ask me anything..."):
    # Show user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Show "Thinking..." spinner while waiting for API
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model=MODEL_ID,
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant."},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=500
                )
                full_response = response.choices[0].message.content
                st.markdown(full_response)
                st.session_state.messages.append({"role": "assistant", "content": full_response})
            except Exception as e:
                st.error(f"API Error: {e}")