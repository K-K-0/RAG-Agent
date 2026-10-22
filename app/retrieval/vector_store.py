from langchain_chroma import Chroma
from retrieval.embeddings import Embedder

class VectorStore:
    def __init__(self):
        self.embedding = Embedder().get_embedding()
        self.db = Chroma(
            persist_directory="storage",
            embedding_function=self.embedding
        )

    def add_document(self, documents):
        self.db.add_documents(documents)

    def get_retriever(self):
        return self.db.as_retriever()

