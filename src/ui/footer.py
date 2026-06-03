# Imports
import streamlit as st

def render_footer():
    st.divider()

    st.markdown(
        """
        <div style="text-align:center; color:gray;">

        Built using LangChain • OpenAI • FAISS • Streamlit

        All rights reserved. © 2026

        Version 1.0

        by SAYANTAN DUTTA
        </div>
        """,
        unsafe_allow_html=True
    )







# YouTube ChatBot using RAG
# st.caption("Built using LangChain • OpenAI • FAISS • Streamlit")
# st.caption("© 2026 YouTube ChatBot by SAYANTAN DUTTA.")
# st.caption("All rights reserved.")
# st.caption("Source code available on GitHub: "
#             "[https://github.com/sayantandutta/youtube-chatbot](https://github.com/sayantandutta/youtube-chatbot)")
# st.caption("Version 1.0")