import sys
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(project_root))

# Ingestion Imports
from src.ingestion.youtube_fetcher import extract_video_id, get_youtube_transcript, get_video_metadata
from src.ingestion.whisper_fallback import generate_transcript_using_whisper

# Splitting Imports
from src.splitting.document_builder import create_documents

# Vector Store Imports
from src.vectorstore.faiss_store import create_vectorstore

# Retrieval Imports
from src.retrieval.retriever import get_retriever

# Chain Imports
from src.chains.rag_chain import build_rag_chain


def main():

    print("=" * 60)
    print("YouTube ChatBot using RAG")
    print("=" * 60)

    # Get YouTube URL
    yt_url = input("\nEnter YouTube URL: ").strip()

    # Extract Video ID
    video_id = extract_video_id(yt_url)

    if not video_id:
        print("❌ Invalid YouTube URL")
        return

    print(f"\n🎥 Video ID: {video_id}")

    # Fetch Metadata
    metadata = get_video_metadata(yt_url)

    print("\n📌 Video Information")
    print(f"Title    : {metadata['title']}")
    print(f"Channel  : {metadata['channel']}")
    print(f"Duration : {metadata['duration']} sec")

    # Fetch Transcript
    transcript = get_youtube_transcript(video_id)

    if transcript is None:
        print("\n⚠ Falling back to Whisper...")

        transcript = generate_transcript_using_whisper(
            yt_url
        )

    if not transcript:
        print("❌ Failed to obtain transcript.")
        return

    print("\n✅ Transcript Ready")

    # Create Documents
    documents = create_documents(
        transcript=transcript,
        video_id=video_id,
        url=yt_url,
        title=metadata["title"],
        channel=metadata["channel"]
    )

    print(f"\n📄 Documents Created: {len(documents)}")

    # Create Vector Store
    print("\n🔄 Creating Vector Store...")

    vectorstore = create_vectorstore(documents)

    print("✅ Vector Store Ready")

    # Create Retriever
    retriever = get_retriever(vectorstore)

    print("✅ Retriever Ready")

    # Build RAG Chain
    chain = build_rag_chain(retriever)

    print("✅ RAG Chain Ready")

    print("\nType 'exit' to quit.\n")

    # Question Loop
    while True:
        question = input("\nAsk: ")

        if question.lower() == "exit":
            break

        try:
            response = chain.invoke(question)

            print("\n" + "=" * 60)

            print(f"Answer:\n{response.answer}")

            print(
                f"\nConfidence: "
                f"{response.confidence}"
            )

            print(
                f"Found In Video: "
                f"{response.found_in_video}"
            )

            print("=" * 60)

        except Exception as e:
            print(f"\n❌ Error: {str(e)}")


if __name__ == "__main__":
    main()
