import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from retrieval.vector_store import VectorStore

# 1. Initialize your database instance
vector_store = VectorStore()
retriever = vector_store.get_retriever()

# 2. Test if Chroma actually holds data by executing a direct similarity search
query = "RAG"
print(f"Testing retrieval for: '{query}'...")

# Fetch the top matches
results = retriever.vectorstore.similarity_search(query, k=2)

if not results:
    print("❌ ERROR: Your database is completely empty! Ingestion is not saving data permanently.")
else:
    print(f"✅ SUCCESS! Found {len(results)} matching chunks in your database:")
    for idx, doc in enumerate(results):
        print(f"\nChunk {idx+1} Content:\n{doc.page_content}")
