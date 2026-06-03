from src.retrieval.retriever import get_retriever

retriever = get_retriever(vectorstore)

print(type(retriever))