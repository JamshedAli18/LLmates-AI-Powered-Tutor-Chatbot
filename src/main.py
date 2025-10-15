# main_app.py
import streamlit as st
from sidebar import render_sidebar
from chat_ui import render_chat_interface
from session_manager import init_session_state

# ------------------- SESSION INIT -------------------
init_session_state()

# ------------------- SIDEBAR -------------------
render_sidebar()

# ------------------- MAIN CHAT -------------------
render_chat_interface()
