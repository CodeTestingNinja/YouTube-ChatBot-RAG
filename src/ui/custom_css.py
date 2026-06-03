import streamlit as st

def load_custom_css():

    st.markdown(
        """
        <style>

        .main {
            padding-top: 1rem;
        }

        .block-container {
            padding-top: 1rem;
            padding-bottom: 2rem;
            max-width: 1200px;
        }

        div[data-testid="stMetric"] {
            border: 1px solid rgba(128,128,128,0.2);
            padding: 15px;
            border-radius: 12px;
        }

        div[data-testid="stChatMessage"] {
            border-radius: 12px;
        }

        .video-card {
            border: 1px solid rgba(128,128,128,0.2);
            border-radius: 12px;
            padding: 20px;
            margin-bottom: 20px;
        }

        </style>
        """,
        unsafe_allow_html=True
    )
