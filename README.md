# Multi-Agent RAG System with Local LLM

A modular multi-agent Retrieval-Augmented Generation (RAG) system built using local LLMs, vector search, and API deployment.

## Features

- PDF ingestion and semantic chunking
- FAISS-based vector retrieval
- Local LLM answering using Ollama + Mistral
- Multi-agent architecture:
  - Retriever Agent
  - Answer Agent
  - Validator Agent
- Persistent conversation memory
- Confidence scoring
- Query logging and analytics endpoint
- PDF upload endpoint
- FastAPI deployment
- Docker-ready packaging

## Tech Stack

- Python
- LangChain
- FAISS
- HuggingFace Embeddings
- Ollama
- Mistral
- FastAPI

## Run Locally

```bash
pip install -r requirements.txt
uvicorn server:app --reload
