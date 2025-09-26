# RAG Q&A Chatbot

This repository demonstrates how to build a **Retrieval-Augmented Generation (RAG) chatbot** using **Python + Jupyter Notebooks**.  
The chatbot can answer questions grounded in your own documents instead of hallucinating answers.

It’s built with modern tools like **LangChain**, **FAISS**, and **uv** (for fast, reliable dependency management).

---

## 🚀 Features

- 🔎 Document retrieval with **FAISS** (dense search) and **BM25** (sparse search)
- 🤖 Q&A chatbot powered by **LLMs** (Ollama, OpenAI, Hugging Face)
- 📚 Source citation alongside answers
- 📝 Step-by-step Jupyter notebooks for learning
- ⚡  Simple evaluation of RAG vs. non-RAG answers
- 🌐 Streamlit demo app

---

## 📂 Project Structure

```bash
├── README.md
├── pyproject.toml
├── main.py
├── data/knowledge/
│   └── example.txt
├── src/rag_chatbot/
│   ├── __init__.py
│   ├── retriever.py
│   ├── pipeline.py
├── notebooks/
│   ├── 01_intro_rag.ipynb
│   ├── 02_build_index.ipynb
│   ├── 03_chatbot_pipeline.ipynb
│   └── ...
```

---

## 🛠️ Tech Stack

- **Languages:** Python  
- **AI/ML:** LangChain, FAISS, BM25, SentenceTransformers
- **LLMs:** Ollama (local), OpenAI, Hugging Face
- **Tools:** Jupyter, Streamlit, GitHub
- **Package Management:** [uv](https://docs.astral.sh/uv/)

---

## ⚡ Quickstart (with uv)

### 1. Clone the repo

```bash
git clone https://github.com/<thrawk>/rag-chatbot.git
cd rag-chatbot
```

### 2. Install dependencies

```bash
uv sync
```

### 3. Launch Jupyter

```bash
uv run jupyter lab
```

### 4. Explore notebooks

```bash
notebooks/01_intro_rag.ipynb
```

### 🎯 Example

```bash
Query: What is Retrieval-Augmented Generation?
Chatbot: Retrieval-Augmented Generation (RAG) is a technique that combines document retrieval with large language models. Instead of generating answers purely from memory, the model retrieves relevant knowledge chunks and uses them to generate more accurate responses.

📖 Sources: [RAG.txt, line 12–27]
```
