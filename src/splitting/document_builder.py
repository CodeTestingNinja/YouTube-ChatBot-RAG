# Imports
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# Function to create LangChain Documents from the transcript
def create_documents(
    transcript: str,
    video_id: str,
    url: str,
    title: str,
    channel: str,
    chunk_size: int = 1200,
    chunk_overlap: int = 200
):
    """
    Split transcript and create LangChain Documents.
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )

    chunks = splitter.split_text(transcript)

    documents = []

    for i, chunk in enumerate(chunks):
        documents.append(
            Document(
                page_content=chunk,
                metadata={
                    "chunk_id": i,
                    "title": title,
                    "channel": channel,
                    "video_id": video_id,
                    "source": url
                }
            )
        )

    return documents
