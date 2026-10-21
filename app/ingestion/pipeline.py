from app.core.config import settings
from app.ingestion.loader import load_document
from app.ingestion.chunker import chunk_text
from app.retrieval.embeddings import embed_texts
from app.retrieval.vector_store import get_collection

def ingest() -> int:
    collection = get_collection()
    ids, texts, metas = [], [], []

    for doc in load_document(settings.data_dir):
        for i, chunk in enumerate(chunk_text["text"], settings.chund_size, settings.chunk_overlap):
            ids.append(f"{doc["source"]}-{i}")
            texts.append(chunk)
            metas.append({"source": doc["source"], "chunk": i})

    collection.upsert(ids=ids, documents=texts, metadata=metas, embeddings=embed_texts(texts))
    print(f"Ingested {len(texts)} chunks")
    return len(texts)

if __name__ == "__main__":
    ingest()

