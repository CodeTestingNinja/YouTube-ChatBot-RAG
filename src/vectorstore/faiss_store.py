# Imports
import os
from langchain_community.vectorstores import FAISS
from src.vectorstore.embeddings import get_embedding_model
from src.config import FAISS_PATH

# Function to create FAISS vector store
def create_vectorstore(documents):
    """
    Create FAISS vector store.

    Args:
        documents (list): List of documents to be added to the vector store.

    Returns:
        FAISS: The created FAISS vector store.
    """

    embeddings = get_embedding_model()

    vectorstore = FAISS.from_documents(
        documents=documents,
        embedding=embeddings
    )

    return vectorstore

# Function to save FAISS vector store
def save_vectorstore(vectorstore, video_id):
    """
    Save FAISS vector store.

    Args:
        vectorstore (FAISS): The FAISS vector store to be saved.
        video_id (str): The video ID to be used as the filename for the saved vector store.
    """

    save_path = os.path.join(FAISS_PATH, video_id)

    os.makedirs(save_path, exist_ok=True)

    vectorstore.save_local(save_path)

# Function to load FAISS vector store
def load_vectorstore(video_id):
    """
    Load FAISS vector store.

    Args:
        video_id (str): The video ID to be used as the filename for the vector store to be loaded.

    Returns:
        FAISS: The loaded FAISS vector store.
    """

    embeddings = get_embedding_model()
    
    load_path = os.path.join(FAISS_PATH, video_id)

    if not os.path.exists(load_path):
        return None

    vectorstore = FAISS.load_local(load_path, embeddings, allow_dangerous_deserialization=True)

    return vectorstore

# Function to check if FAISS vector store exists
def vectorstore_exists(video_id):
    """
    Check if FAISS vector store exists for a given video ID.

    Args:
        video_id (str): The video ID to check.

    Returns:
        bool: True if the vector store exists, False otherwise.
    """

    path = os.path.join(
        FAISS_PATH,
        video_id
    )

    return os.path.exists(path)
