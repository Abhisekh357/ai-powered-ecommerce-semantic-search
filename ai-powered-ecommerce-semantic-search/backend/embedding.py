from sentence_transformers import SentenceTransformer

print("Loading embedding model...")

model = SentenceTransformer("all-MiniLM-L6-v2")

print("Embedding model loaded successfully.")

def create_embedding(text: str):
    """
    Converts text into a vector embedding.
    """
    return model.encode(text).tolist()