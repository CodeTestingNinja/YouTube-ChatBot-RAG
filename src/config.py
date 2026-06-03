import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

EMBEDDING_MODEL = "text-embedding-3-small"

CHUNK_SIZE = 1200
CHUNK_OVERLAP = 200

TOP_K = 5

FAISS_PATH = "data/faiss_indexes"
TRANSCRIPT_PATH = "data/transcripts"
AUDIO_PATH = "data/audio"
