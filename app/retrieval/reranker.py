from sentence_transformers import CrossEncoder


class Reranker:

    def __init__(self):
        self.model = CrossEncoder(
            "BAAI/bge-reranker-base"
        )

    def rerank(self, query, documents, top_k=5):
        pairs = []

        for doc in documents:
            pairs.append([
                query, doc.page_content
            ])

        scores = self.model.predict(pairs)

        ranked = sorted(
            zip(documents, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return [
            doc for doc in ranked[:top_k]
        ]
