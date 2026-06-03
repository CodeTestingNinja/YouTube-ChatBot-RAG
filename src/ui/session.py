# Imports
import streamlit as st

def initialize_session():
    defaults = {
        "chain": None,
        "retriever": None,
        "metadata": None,
        "video_id": None,
        "processed": False,
        "cached": False,
        "chat_history": []
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
