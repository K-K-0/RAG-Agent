import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from retrieval.vector_store import VectorStore


vector_db = VectorStore()

retriever = vector_db.get_retriever()

query = "Who is the prof?"

docs = retriever.invoke(query)

for i, doc in enumerate(docs, start=1):
    print(f"\nDocument {i}")
    print("-" * 50)
    print(doc.page_content)