import pickle

from langchain_community.retrievers import BM25Retriever


class BM25Indexer:

    INDEX_PATH = "storage/bm25.pkl"


    @classmethod
    def build(cls, documents):

        retriever = BM25Retriever.from_documents(
            documents
        )

        retriever.k = 5


        with open(cls.INDEX_PATH, "wb") as f:

            pickle.dump(
                retriever,
                f
            )