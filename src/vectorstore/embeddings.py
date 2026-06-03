# Imports
from langchain_openai import OpenAIEmbeddings
from src.config import OPENAI_API_KEY, EMBEDDING_MODEL

# Function to create OpenAI embedding model
def get_embedding_model():
    """
    Create OpenAI embedding model.
    """

    embeddings = OpenAIEmbeddings(
        model=EMBEDDING_MODEL,
        api_key=OPENAI_API_KEY
    )

    return embeddings
