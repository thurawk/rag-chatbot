# src/rag_chatbot/retriever.py
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

def build_retriever(knowledge_path="data/knowledge", k=3):
    """Builds a retriever from local knowledge documents."""
    loader = DirectoryLoader(knowledge_path, glob="*.txt")
    docs = loader.load()

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectordb = FAISS.from_documents(docs, embeddings)
    retriever = vectordb.as_retriever(search_kwargs={"k": k})
    return retriever
