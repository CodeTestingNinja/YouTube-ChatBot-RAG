from src.vectorstore.embeddings import get_embedding_model

embeddings = get_embedding_model()

print(type(embeddings))