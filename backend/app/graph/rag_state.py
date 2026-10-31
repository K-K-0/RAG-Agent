from typing import TypedDict, List
from langchain_core.messages import BaseMessage


class RAGState(TypedDict):

    question: str
    documents: List
    answer: str
    rewrite_count: int
    chat_history: List[BaseMessage]