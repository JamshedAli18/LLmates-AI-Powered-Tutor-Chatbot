# chat_ui.py
import streamlit as st
from src.tutor_chain import build_prompt, get_tutor_response
from src.rag_pipeline import retrieve_context


def render_chat_interface():
    st.title("🎓 Tutorix")
    st.markdown("Ask your AI tutor anything — upload notes for personalized answers!")

    # Display previous messages
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    # Chat input
    if user_input := st.chat_input("💬 Type your question here..."):
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Prepare context
        has_notes = st.session_state.vectorstore is not None
        context = retrieve_context(st.session_state.vectorstore, user_input) if has_notes else ""

        # Build prompt and get response
        final_prompt = build_prompt(
            st.session_state.subject,
            st.session_state.level,
            st.session_state.understanding,
            has_notes,
            context,
            user_input
        )
        system_context = "\n".join([f"{m['role'].capitalize()}: {m['content']}" for m in st.session_state.messages])
        full_prompt = f"{system_context}\n\n{final_prompt}"

        with st.chat_message("assistant"):
            with st.spinner("🧠 Thinking..."):
                response = get_tutor_response(full_prompt)
                st.markdown(response.content)

        st.session_state.messages.append({"role": "assistant", "content": response.content})

