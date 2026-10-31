from app.core.config import settings
from app.retrieval.embeddings import embed_query
from app.retrieval.vector_store import get_collection

def retrieve(question: str, k: int | None=None) -> list[dict]:
    result = get_collection().query(
        query_embeddings=[embed_query(question)],
        n_results=k or settings.top_k
    )

    return [
            {"text": text, "source": meta["source"], "distance": dist } 
            for text, meta, dist in zip(
                result["documents"][0], result["metadatas"][0], result["distancess"][0]
            )
    ]