# Imports
import streamlit as st

def render_sources(documents):
    st.subheader("📚 Retrieved Sources")

    for i, doc in enumerate(documents, start=1):
        chunk_id = (
            doc.metadata.get(
                "chunk_id",
                "N/A"
            )
        )

        preview = (
            doc.page_content[:400]
            + "..."
        )

        with st.expander(f"Source #{i}"):
            st.caption(f"Chunk ID: {chunk_id}")

            st.write(preview)
