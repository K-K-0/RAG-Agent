import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from loader import PDFLoader
from splitter import DocumentSplitter
from retrieval.vector_store import VectorStore
from retrieval.bm25_indexin import BM25Indexer

def ingest(pdf_path):
    loader = PDFLoader(pdf_path)
    documents = loader.load()

    splitter = DocumentSplitter()
    chunks = splitter.split(documents)
    
    vector_store = VectorStore()
    vector_store.add_document(chunks)
    BM25Indexer.build(chunks)

    
    print(f"Pages Loaded: {len(documents)}")
    print(f"Chunks Created: {len(chunks)}")

    return vector_store

if __name__ == "__main__":
    chunks = ingest("/home/k-k/RAG/data/sample.pdf")
    print("\n--- First Chunk Content ---")
    print(chunks.embedding)
