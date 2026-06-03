# Imports
import streamlit as st

def render_metrics(metadata, chat_count, cache_status):
    st.subheader("📊 Session Analytics")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Messages",
            chat_count
        )

    with col2:
        st.metric(
            "Duration",
            f"{metadata.get('duration', 'N/A')}s"
        )

    with col3:
        st.metric(
            "Views",
            f"{metadata.get('view_count', 0):,}"
        )

    with col4:
        st.metric(
            "Cache",
            "Hit" if cache_status else "Miss"
        )
