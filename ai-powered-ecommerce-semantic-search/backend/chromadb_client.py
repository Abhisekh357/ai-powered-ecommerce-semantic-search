import chromadb
from embedding import create_embedding

# Create a persistent ChromaDB database
client = chromadb.PersistentClient(path="./chroma_db")

# Create or get collection
collection = client.get_or_create_collection(
    name="products"
)

def add_product(product_id, name, description):
    """
    Store a product and its embedding in ChromaDB.
    """

    embedding = create_embedding(description)

    collection.add(
        ids=[str(product_id)],
        documents=[description],
        embeddings=[embedding],
        metadatas=[
            {
                "name": name
            }
        ]
    )

def search_products(query, top_k=3):

    query_embedding = create_embedding(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    products = []

    ids = results["ids"][0]
    docs = results["documents"][0]
    metadata = results["metadatas"][0]

    for i in range(len(ids)):
        products.append({
            "id": ids[i],
            "name": metadata[i]["name"],
            "description": docs[i]
        })

    return products