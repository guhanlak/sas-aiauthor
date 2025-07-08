# Ai Author Backend (FastAPI)

## Overview
This is the backend for the Ai Author micro SaaS app. It provides authentication, book upload, chat, and admin APIs, integrates with OpenAI, and stores book embeddings in a vector database.

## Setup
1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy `.env.example` to `.env` and fill in your secrets.
4. Run the server:
   ```bash
   uvicorn main:app --reload
   ```
