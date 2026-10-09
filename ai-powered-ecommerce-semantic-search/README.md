# AI-Powered E-Commerce Platform with Semantic Product Search

A storefront UI with a FastAPI semantic product-search API. Product descriptions are embedded using Sentence Transformers, stored in ChromaDB, retrieved by similarity, and passed as context to Gemini for recommendations.

## Tech stack
- Frontend: HTML, CSS, JavaScript
- Backend: Python, FastAPI
- Embeddings: Sentence Transformers (`all-MiniLM-L6-v2`)
- Vector database: ChromaDB
- Generative AI: Gemini API with a RAG workflow

## Project structure
```text
ai-powered-ecommerce-semantic-search/
├── backend/
│   ├── app.py
│   ├── rag.py
│   ├── chromadb_client.py
│   ├── embedding.py
│   ├── gemini_service.py
│   ├── requirements.txt
│   └── .env.example
├── frontend/
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── .gitignore
└── README.md
```

## Setup backend (Windows PowerShell)
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```
Open `backend/.env` and replace the placeholder with your own Gemini API key. Do not commit `.env`.

Start the API:
```powershell
uvicorn app:app --reload
```
API docs: http://127.0.0.1:8000/docs

## Add sample products
Send POST requests to `/add-product` using Swagger (`/docs`), with JSON like:
```json
{
  "id": 1,
  "name": "Lightweight running shoes",
  "description": "Breathable lightweight running shoes for daily jogging and long walks"
}
```
Add a few products before testing search.

## Run frontend
Open `frontend/index.html` in a browser. The search box sends queries to `http://127.0.0.1:8000/search`. Keep the backend running. If browser CORS/file restrictions occur, serve the frontend locally (for example, with VS Code Live Server).

## Notes
- The uploaded storefront references an `images/` directory that was not included in the supplied files; add your own licensed images under `frontend/images/` or update the image paths.
- This project currently wires the storefront search box to the semantic-search API. Features such as login, checkout, cart persistence, wishlist, and reviews should only be described as implemented if you add and test them.
- Never commit API keys, passwords, virtual environments, or the generated `chroma_db/` directory.
