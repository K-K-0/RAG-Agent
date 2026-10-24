from typing import TypedDict, List


class RAGState(TypedDict):

    question: str
    documents: List
    answer: str
    rewrite_count: int