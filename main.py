# main_app.py
from src.sidebar import render_sidebar
from src.chat_ui import render_chat_interface
from src.session_manager import init_session_state


# ------------------- SESSION INIT -------------------
init_session_state()

# ------------------- SIDEBAR -------------------
render_sidebar()

# ------------------- MAIN CHAT -------------------
render_chat_interface()
