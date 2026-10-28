from retrieval.vector_store import VectorStore
from retrieval.bm25 import BM25Search
from retrieval.reranker import Reranker

class HybridRetriever:

    def __init__(self):

        self.vector_retriever = (
            VectorStore().get_retriever()
        )

        self.bm25_retriever = (
            BM25Search.load()
        )

        self.reranker = Reranker()


    def retrieve(self, query):

        vector_docs = (
            self.vector_retriever.invoke(query)
        )


        bm25_docs = (
            self.bm25_retriever.invoke(query)
        )
        
        results = []

        seen = set()


        for doc in vector_docs + bm25_docs:

            if doc.page_content not in seen:

                results.append(doc)

                seen.add(doc.page_content)


        reranked_docs = self.reranker.rerank(
            query=query,
            documents=results,
            top_k=5
        )


        return reranked_docs