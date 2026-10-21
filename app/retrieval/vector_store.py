import chromadb
from app.core.config import settings

def get_collection():
    client = chromadb.PersistentClient(path=settings.vector_store_dir)
    return client.get_or_create_collection(
        name = "docs", metadata={"hnsw:space": "cosine"}
    )