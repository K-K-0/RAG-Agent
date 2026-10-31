from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from graph.rag_graph import rag_graph

import os
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)


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

if __name__ == "__main__":
    # Fallback to 10000 if PORT environment variable isn't found
    port = int(os.environ.get("PORT", 10000)) 
    uvicorn.run("main:app", host="0.0.0.0", port=port)
