from chromadb_client import search_products
from gemini_service import generate_response

def ask(query: str) -> str:
    """Retrieve relevant products, then ask Gemini to recommend from them."""
    products = search_products(query, top_k=3)
    if not products:
        return "No matching products were found. Please add products and try again."
    return generate_response(query, products)
