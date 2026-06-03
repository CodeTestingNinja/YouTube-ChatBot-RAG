# Imports
import streamlit as st

def render_header():
    st.markdown("""
    <div style="text-align:center;padding:20px;">
        <h1>🎥 YouTube ChatBot using RAG</h1>
        <p style="font-size:20px;">
            Chat with any YouTube video using Retrieval-Augmented Generation
        </p>
        <p>
            Extract transcripts • Retrieve context • Ask intelligent questions
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()
