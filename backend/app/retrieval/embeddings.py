from langchain_huggingface import HuggingFaceEmbeddings


class Embedder:

    def __init__(self):
        self.embedding = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2",
            encode_kwargs={"normalize_embeddings": True},
        )

    def get_embedding(self):
        return self.embedding