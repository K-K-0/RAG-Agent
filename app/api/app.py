from fastapi import FastAPI
from pydantic import BaseModel

from graph.rag_graph import rag_graph

app = FastAPI()


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    question: str
    answer: str
    retrieved_chunks: list


@app.post("/chat", response_model=QueryResponse)
def chat(request: QueryRequest):

    result = rag_graph.invoke(
        {
            "question": request.question,
            "documents": [],
            "answer": "",
            "rewrite_count": 0
        }
    )

    chunks = []

    for doc in result["documents"]:
        chunks.append({
            "content": doc.page_content,
            "metadata": doc.metadata
        })

    return QueryResponse(
        question=request.question,
        answer=result["answer"],
        retrieved_chunks=chunks
    )