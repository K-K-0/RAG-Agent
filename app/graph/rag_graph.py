from typing import TypedDict
from langgraph.graph import StateGraph, START, END
from app.retrieval.retriever import retrieve
from app.prompts.rag_prompt import build_prompt
from app.llm.client import generate

class RAGState(TypedDict):
    question: str
    docs: list[dict]
    answer: str

def retrieve_node(state: RAGState) -> dict:
    return {"docs": retrieve(state["question"])}

def generate_node(state: RAGState) -> dict:
    prompt = build_prompt(state["question"])
    return {"answer": generate(prompt)}

def build_graph():
    g = StateGraph(RAGState)
    g.add_node("retrieve", retrieve_node)
    g.add_node("generate", generate_node)
    g.add_edge(START, "retrieve")
    g.add_edge("retrieve", "generate")
    g.add_edge("generate", END)
    return g.compile()

rag_graph = build_graph()