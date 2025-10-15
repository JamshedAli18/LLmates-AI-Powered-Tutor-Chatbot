# sidebar.py
import streamlit as st
from src.rag_pipeline import process_pdf
from src.session_manager import save_chat, load_chat, new_chat
import os
from datetime import datetime

def render_sidebar():
    st.sidebar.header("🧑‍Student Setup")

    # Class Level
    level = st.sidebar.selectbox("Class Level", ["School", "College", "University"])

    # Subjects based on level
    subjects_dict = {
        "School": ["Math", "Science", "History"],
        "College": ["Physics", "Chemistry", "Mathematics", "Computer Science", "Economics"],
        "University": ["Data Science", "AI", "Machine Learning", "Engineering", "Computer Science"]
    }
    st.session_state.subject = st.sidebar.selectbox("Subject", subjects_dict.get(level, ["Math", "Science", "History"]))
    st.session_state.level = level

    # Understanding Level
    st.session_state.understanding = st.sidebar.selectbox("Understanding Level", ["Beginner", "Intermediate", "Advanced"])

    # PDF Upload
    uploaded_file = st.sidebar.file_uploader("📘 Upload Lecture Notes (PDF)", type=["pdf"])
    if uploaded_file:
        with st.spinner("📖 Processing your notes..."):
            st.session_state.vectorstore = process_pdf(uploaded_file)
        st.sidebar.success("☑️ Notes uploaded successfully!")

    # Chat Sessions
    st.sidebar.markdown("---")
    st.sidebar.subheader("💬 Chat Sessions")

    # Save chat
    st.session_state.chat_name = st.sidebar.text_input("Save Chat As", st.session_state.chat_name)
    if st.sidebar.button("💾 Save Chat"):
        save_chat(st.session_state.chat_name)

    # Load previous chat
    existing_chats = [f.replace(".json", "") for f in os.listdir("saved_chats") if f.endswith(".json")]
    selected_chat = st.sidebar.selectbox("📂 Load Previous Chat", ["Select..."] + existing_chats)
    if st.sidebar.button("📥 Load Chat") and selected_chat != "Select...":
        load_chat(selected_chat)

    # New Chat
    if st.sidebar.button("🔄 New Chat"):
        new_chat()


