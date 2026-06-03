# Imports
import streamlit as st

def render_chat_input():
    return st.chat_input("Ask a question about the video...")

def render_user_message(question):
    with st.chat_message("user"):
        st.markdown(question)

def render_assistant_message(response):
    with st.chat_message("assistant"):
        st.markdown(response.answer)
        st.caption(f"Confidence: {response.confidence}")

        if response.found_in_video:
            st.success("Information found in video.")
        
        else:
            st.warning("Information not found in video.")

def render_chat_history(chat_history):
    for item in chat_history:
        with st.chat_message("user"):
            st.markdown(item["question"])

        with st.chat_message("assistant"):
            st.markdown(item["answer"])

            st.caption(
                f"Confidence: "
                f"{item['confidence']}"
            )
