# Imports
import streamlit as st

def render_video_input():
    st.subheader("📺 Video Processing")

    youtube_url = st.text_input(
        "Enter YouTube Video URL",
        placeholder="https://www.youtube.com/watch?v=..."
    )

    process_clicked = st.button(
        "🚀 Process Video",
        use_container_width=True
    )

    return youtube_url, process_clicked

def render_video_metadata(metadata):
    st.subheader("📌 Video Information")

    col1, col2 = st.columns([1, 3])

    with col1:
        if metadata.get("thumbnail"):
            st.image(
                metadata["thumbnail"],
                use_container_width=True
            )

    with col2:
        st.markdown(
            f"### {metadata['title']}"
        )

        st.write(
            f"**Channel:** "
            f"{metadata['channel']}"
        )

        st.write(
            f"**Duration:** "
            f"{metadata['duration']} seconds"
        )

        if metadata.get("view_count"):
            st.write(
                f"**Views:** "
                f"{metadata['view_count']:,}"
            )

        if metadata.get("upload_date"):
            st.write(
                f"**Upload Date:** "
                f"{metadata['upload_date']}"
            )
