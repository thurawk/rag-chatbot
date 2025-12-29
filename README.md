# RAG Q&A Chatbot

This repository demonstrates how to build a **Retrieval-Augmented Generation (RAG) chatbot** using **Python**. The chatbot can answer questions grounded in your own documents instead of hallucinating answers.

---

## 🚀 Features

- 🔎 Document retrieval with **FAISS** (dense search)
- 🤖 Q&A chatbot powered by **LLMs** (Ollama, compatible with OpenAI)
- 📚 Source citation alongside answers
- 🌐 Streamlit demo app

---

## 📂 Project Structure

```bash
├── data/knowledge/           # Place your text documents here
├── notebooks/
│   └── RAG_QA_Chatbot.ipynb  # Jupyter notebook
├── src/rag_chatbot/
│   ├── __init__.py
│   ├── app.py                # Streamlit app
│   ├── pipeline.py           # Chatbot pipeline
│   ├── retriever.py          # Document retriever
├── main.py                   # CLI entry point
├── pyproject.toml
├── README.md
└── requirements.txt          # Project dependencies
```

---

## 🛠️ Tech Stack

- **Languages:** Python
- **AI/ML:** LangChain, FAISS, SentenceTransformers
- **LLMs:** Ollama (default: llama3)
- **Web App:** Streamlit

---

## ⚡ Quickstart

### 1. Prerequisites

- **Python 3.9+**
- **Ollama**: [Download and install Ollama](https://ollama.com/).
  - Pull the default model:

      ```bash
      ollama pull llama3
      ```

### 2. Installation

1. **Clone the repo** (if you haven't already):

    ```bash
    git clone https://github.com/thurawk/rag-chatbot.git
    cd rag-chatbot
    ```

2. **Create and activate a virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

    *Note: This project includes `unstructured` for file processing, which may require system dependencies like `libmagic` depending on your OS.*

### 3. Usage

#### CLI Chatbot

Run the simple command-line interface:

```bash
python main.py
```

*Note: Make sure your `venv` is active!*

#### Streamlit Web App

Launch the interactive web UI:

```bash
streamlit run src/rag_chatbot/app.py
```

### 4. Custom Data

Place your `.txt` files in the `data/knowledge/` directory. The chatbot will automatically ingest them when it initializes.

---

## 🐛 Troubleshooting

- **ModuleNotFoundError**: Ensure you have activated your virtual environment (`source venv/bin/activate`).
- **Ollama Connection Error**: Make sure the Ollama app is running in the background.
