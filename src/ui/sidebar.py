# Imports
import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.markdown("## 🎥 YouTube RAG")

        st.divider()

        st.markdown("### Model")
        st.caption("GPT-5.4-mini")

        st.markdown("### Embeddings")
        st.caption("text-embedding-3-small")

        st.markdown("### Retriever")
        st.caption("MMR")

        st.divider()

        st.markdown("### Current Session")

        video_loaded = (
            "Yes"
            if st.session_state.get("processed")
            else "No"
        )

        st.write(f"**Video Loaded:** {video_loaded}")

        st.write(
            f"**Messages:** "
            f"{len(st.session_state.chat_history)}"
        )

        if not st.session_state.get("processed"):
            cache_status = "N/A"
        else:
            cache_status = (
                "Hit"
                if st.session_state.get("cached")
                else "Miss"
            )

        st.write(f"**Cache:** {cache_status}")

        st.divider()

        st.markdown("### Actions")

        clear_clicked = st.button(
            "🗑 Clear Session",
            use_container_width=True
        )

        st.divider()

        st.markdown("### Tech Stack")

        st.markdown(
            """
            - LangChain
            - OpenAI
            - FAISS
            - Streamlit
            """
        )

        st.divider()

        st.caption("Version 1.0")

        return clear_clicked
