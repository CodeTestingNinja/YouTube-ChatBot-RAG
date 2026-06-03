# Imports
import streamlit as st
from src.ui.header import render_header
from src.ui.sidebar import render_sidebar
from src.ui.video_section import render_video_input, render_video_metadata
from src.ui.session import initialize_session
from src.services.video_processor import process_video
from src.ui.chat_section import render_chat_input, render_user_message, render_assistant_message, render_chat_history
from src.ui.metrics_section import render_metrics
from src.ui.source_section import render_sources
from src.ui.custom_css import load_custom_css
from src.ui.footer import render_footer

# Initialize Session
initialize_session()

# Page Config
st.set_page_config(
    page_title="YouTube ChatBot",
    page_icon="🎥",
    layout="wide"
)

# Load Custom CSS
load_custom_css()

# Render Sidebar
clear_session = render_sidebar()

if clear_session:
    st.session_state.clear()
    st.rerun()

# Render Header
render_header()

youtube_url, process_clicked = (render_video_input())

if process_clicked:
    try:
        with st.spinner("Processing video..."):

            result = process_video(youtube_url)

            st.session_state.chain = (result["chain"])
            st.session_state.retriever = (result["retriever"])
            st.session_state.metadata = (result["metadata"])
            st.session_state.video_id = (result["video_id"])
            st.session_state.processed = True
            st.session_state.cached = (result["cached"])

        if result["cached"]:
            st.success("Loaded cached vector store.")

        else:
            st.success("Video processed successfully.")

    except Exception as e:
        st.error(f"Processing failed: {str(e)}")

if (st.session_state.processed and st.session_state.metadata):
    render_video_metadata(st.session_state.metadata)

# Render Metrics
if st.session_state.metadata is not None:
    render_metrics(
        metadata = st.session_state.metadata,
        chat_count = len(st.session_state.chat_history),
        cache_status = st.session_state.cached
    )

if st.session_state.chain:
    render_chat_history(st.session_state.chat_history)
    question = render_chat_input()

    if question:
        render_user_message(question)

        try:
            with st.spinner("Generating answer..."):
                docs = st.session_state.retriever.invoke(question)
                response = st.session_state.chain.invoke(question)

            render_assistant_message(response)
            render_sources(docs)

            st.session_state.chat_history.append(
                {
                    "question": question,
                    "answer": response.answer,
                    "confidence": response.confidence,
                    "found_in_video": response.found_in_video,
                    "sources": docs
                }
            )

        except Exception as e:
            st.error(f"Error: {str(e)}")

# Render Footer
render_footer()
