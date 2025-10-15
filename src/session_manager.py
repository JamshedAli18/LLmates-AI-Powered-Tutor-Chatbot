# session_manager.py
import os
import json
from datetime import datetime
import streamlit as st

CHAT_DIR = "saved_chats"
os.makedirs(CHAT_DIR, exist_ok=True)

def init_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = None
    if "chat_name" not in st.session_state:
        st.session_state.chat_name = f"Chat_{datetime.now().strftime('%Y%m%d_%H%M%S')}"

def save_chat(name: str):
    """Save current chat session with overwrite confirmation if needed"""
    path = os.path.join(CHAT_DIR, f"{name}.json")

    # Check if file exists
    if os.path.exists(path):
        # Ask for confirmation
        if "overwrite_confirmed" not in st.session_state:
            st.session_state.overwrite_confirmed = False

        if not st.session_state.overwrite_confirmed:
            st.warning(f"A chat named '{name}' already exists.")
            col1, col2 = st.columns([1,1])
            with col1:
                if st.button("✅ Yes, Replace", key="replace_yes"):
                    st.session_state.overwrite_confirmed = True
                    save_chat(name)  # Call again to actually save
            with col2:
                if st.button("❌ No, Change Name", key="replace_no"):
                    st.info("Please change the chat name and try saving again.")
            return

    # Save the chat
    with open(path, "w", encoding="utf-8") as f:
        json.dump(st.session_state.messages, f, indent=4, ensure_ascii=False)
    st.success(f"💾 Chat saved as '{name}.json'")
    st.session_state.overwrite_confirmed = False  # reset for next save

def load_chat(name: str):
    """Load a previous chat session"""
    path = os.path.join(CHAT_DIR, f"{name}.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            st.session_state.messages = json.load(f)
        st.success(f"📂 Loaded chat '{name}'")
    else:
        st.error("❌ Chat not found.")

def new_chat():
    """Start a fresh chat session"""
    st.session_state.messages = []
    st.rerun()
