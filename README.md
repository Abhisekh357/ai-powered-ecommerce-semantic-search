# AI-Powered E-Commerce Platform with Semantic Product Search

An AI-powered e-commerce platform that combines a responsive storefront with semantic product search and intelligent product recommendations using Retrieval-Augmented Generation (RAG).

## Features

- Responsive e-commerce storefront built with HTML and CSS
- Product search interface
- Semantic search based on the meaning of user queries
- Text embeddings generated using Sentence Transformers
- Vector storage and similarity-based retrieval using ChromaDB
- AI-powered product recommendations using the Gemini API
- REST API built with FastAPI

## Tech Stack

| Technology | Purpose |
|---|---|
| HTML, CSS, JavaScript | Frontend |
| Python | Backend programming |
| FastAPI | REST API |
| Sentence Transformers | Text embeddings |
| ChromaDB | Vector database |
| Gemini API | AI-generated recommendations |
| RAG | Retrieval-augmented generation |

## How It Works

1. Product information is submitted to the backend.
2. Sentence Transformers converts product descriptions into vector embeddings.
3. ChromaDB stores product descriptions and their embeddings.
4. When a user enters a query, the system generates a query embedding.
5. ChromaDB retrieves semantically relevant products.
6. The retrieved product information is passed to Gemini as context.
7. Gemini generates a natural-language product recommendation.

## Project Structure

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

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/Abhisekh357/ai-powered-ecommerce-semantic-search.git
cd ai-powered-ecommerce-semantic-search
```

### 2. Set Up the Backend

```bash
cd backend
python -m venv venv
```

Activate the virtual environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure the Gemini API Key

Copy `.env.example` to `.env` inside the `backend` folder.

```text
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your own API key. Never upload the actual `.env` file or API key to GitHub.

### 4. Start the Backend

From the `backend` directory, run:

```bash
uvicorn app:app --reload
```

Open the API documentation:

http://127.0.0.1:8000/docs

### 5. Add Products and Test Search

Use the `/add-product` endpoint in the API documentation to add sample products.

Example request:

```json
{
  "id": 1,
  "name": "Running Shoes",
  "description": "Lightweight and breathable shoes for jogging and daily walking"
}
```

Add a few products, then use the `/search` endpoint to test semantic product search and AI-generated recommendations.

### 6. Run the Frontend

Open `frontend/index.html` in a browser. Keep the backend running while testing the AI search feature.

If browser restrictions prevent API requests, run the frontend using a local development server such as VS Code Live Server.

## Future Improvements

- Hybrid keyword and semantic search
- Improved product ranking and filtering
- User authentication and persistent shopping carts
- Product recommendation history
- Deployment to a cloud platform

## License

This project is intended for learning and demonstration purposes. Add a suitable open-source license if you want others to reuse the code.
