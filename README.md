# 📱 Multi-Document RAG System for Smartphone Manuals

A simple but scalable **Retrieval-Augmented Generation (RAG)** project that answers user questions by retrieving relevant information from multiple smartphone PDF manuals.

This project demonstrates how to build a **multi-document semantic search + QA system** using FAISS and HuggingFace embeddings — without a backend, UI, or complex infrastructure.

I did this project for learning purposes, the project does not represet a real-life work.

---

## Features

* Multi-PDF support (each document = one phone model)
* Semantic search using FAISS
* Metadata-based filtering (`phone_model`)
* Automatic phone model detection from user query
* Interactive CLI chat interface

---

## Project Structure

```
multi_doc_rag/
│── data/                  # PDF manuals
│   ├── note20.pdf
│   ├── zfold7.pdf
│   ├── s23fe.pdf
│   ├── s26ultra.pdf
│
│── vectordb/             # FAISS index (generated in ingest.py)
│
│── embedder.py           # Embedding model
│── ingest.py             # PDF ingestion & indexing
│── retriever.py          # Retrieval logic
│── rag.py                # Prompt + generation
│── utils.py              # Query processing
│── main.py               # CLI interface
│── requirements.txt
```

---

## How It Works

### 1. Ingestion Pipeline

* Load PDF files
* Split into chunks
* Attach metadata (`phone_model`)
* Generate embeddings
* Store in FAISS vector database

---

### 2. Query Flow

```
User Query
   ↓
Phone Model Detection
   ↓
FAISS Retrieval (Top-K)
   ↓
Metadata Filtering (phone_model)
   ↓
Context Construction
   ↓
LLM Generation
   ↓
Final Answer
```

---

## Installation

```bash
git clone https://github.com/ismailavcu/Multi_Documents_RAG_Smartphone_Manuals.git
cd Multi_Documents_RAG_Smartphone_Manuals
pip install -r requirements.txt
```

---

## Add Your PDFs

Place your PDF manuals inside the `data/` folder and map them in `ingest.py`:

```python
PDF_MAP = {
    "file.pdf": "phone_model_name"
}
```

---

## Build the Vector Database

```bash
python ingest.py
```

This will:

* Process PDFs
* Create embeddings
* Save FAISS index in `/vectordb`

---

## Run the Assistant

```bash
python main.py
```

---

## Example Usage

### Case 1: No model specified

```
You: How to take screenshot?
Assistant: I'm here to answer your smartphone questions. What is your phone model? For example: s26 ultra?
```

---

### Case 2: Model detected automatically

```
You: How to take screenshot on S23 FE?
Assistant: [Answer from S23 FE manual]
```

---


### Normalized Model Detection

Handles variations like:

* `s23fe`
* `s 23 fe`
* `S-23 FE`

---

### FAISS for Simplicity

* Fast local vector search
* No external database required

---

## Limitations

* Uses an ollama LLM (llama3.1:8b) → maybe limited answer quality ?
* No UI (CLI only)
* No hybrid search
* No re-ranking or query rewriting

---

## Future Improvements

* Better LLM 
* Query rewriting
* Re-ranking for higher accuracy
* Web interface
* PostgreSQL + pgvector instead of FAISS
* Conversation memory

---
