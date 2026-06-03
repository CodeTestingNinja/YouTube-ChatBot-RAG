# Imports
from src.ingestion.youtube_fetcher import extract_video_id, get_youtube_transcript, get_video_metadata
from src.ingestion.whisper_fallback import generate_transcript_using_whisper
from src.splitting.document_builder import create_documents
from src.vectorstore.faiss_store import create_vectorstore, save_vectorstore, load_vectorstore, vectorstore_exists
from src.retrieval.retriever import get_retriever
from src.chains.rag_chain import build_rag_chain

# Main video processing function
def process_video(url: str):
    # Extract Video ID
    video_id = extract_video_id(url)

    if not video_id:
        raise ValueError("Invalid YouTube URL.")

    # Metadata
    metadata = get_video_metadata(url)

    # Check Cached Vector Store
    if vectorstore_exists(video_id):
        vectorstore = load_vectorstore(video_id)
        retriever = get_retriever(vectorstore)
        chain = build_rag_chain(retriever)

        return {
            "video_id": video_id,
            "metadata": metadata,
            "chain": chain,
            "retriever": retriever,
            "cached": True
        }

    # Transcript
    transcript = get_youtube_transcript(video_id)

    if transcript is None:
        transcript = (generate_transcript_using_whisper(url))

    # Documents
    documents = create_documents(
        transcript=transcript,
        video_id=video_id,
        url=url,
        title=metadata["title"],
        channel=metadata["channel"]
    )

    # Vector Store
    vectorstore = create_vectorstore(documents)
    save_vectorstore(vectorstore, video_id)

    # Retriever
    retriever = get_retriever(vectorstore)

    # Chain
    chain = build_rag_chain(retriever)

    return {
        "video_id": video_id,
        "metadata": metadata,
        "chain": chain,
        "retriever": retriever,
        "cached": False,
    }
