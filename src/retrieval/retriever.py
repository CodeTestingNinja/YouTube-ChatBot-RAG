# Imports
from src.config import TOP_K

# Retriever function
def get_retriever(vectorstore):
    """
    Create MMR retriever from vectorstore.
    """

    retriever = vectorstore.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": TOP_K,
            "fetch_k": 20,
            "lambda_mult": 0.7
        }
    )

    return retriever
