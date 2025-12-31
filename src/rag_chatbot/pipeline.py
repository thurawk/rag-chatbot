# src/rag_chatbot/pipeline.py
from langchain.chains import RetrievalQA
from langchain_community.llms import Ollama  # swap with OpenAI if needed
from src.rag_chatbot.retriever import build_retriever

def build_chatbot(knowledge_path="data/knowledge", k=3, model="llama3"):
    """Creates a Retrieval-Augmented Generation chatbot pipeline."""
    retriever = build_retriever(knowledge_path, k=k)
    llm = Ollama(model=model)

    qa = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )
    return qa
