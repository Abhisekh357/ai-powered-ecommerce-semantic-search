from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from chromadb_client import add_product
from rag import ask

app = FastAPI(
    title="Semantic Product Search API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Product(BaseModel):
    id: int
    name: str
    description: str


class SearchRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {
        "message": "Semantic Product Search API Running"
    }


@app.post("/add-product")
def insert_product(product: Product):

    add_product(
        product.id,
        product.name,
        product.description
    )

    return {
        "message": "Product Added Successfully"
    }


@app.post("/search")
def search(request: SearchRequest):

    answer = ask(request.query)

    return {
        "answer": answer
    }