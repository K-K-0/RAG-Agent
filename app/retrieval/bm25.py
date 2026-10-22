from langchain_community.retrievers import BM25Retriever

class BM25Search:
    def __init__(self, documents):
        self.retriver = BM25Retriever.from_documents(documents)
        self.retriver.k = 5

    def get_retriever(self):
        return self.retriver
        