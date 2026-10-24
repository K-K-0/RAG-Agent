from langgraph.graph import StateGraph, END

from graph.rag_state import RAGState

from graph.rag_nodes import (
    retrieve_node,
    grade_node,
    rewrite_node,
    generate_node, decide_next
)

graph = StateGraph(RAGState)

graph.add_node("retrieve", retrieve_node)
graph.add_node("grade", grade_node)
graph.add_node("rewrite", rewrite_node)
graph.add_node("generate", generate_node)

graph.set_entry_point("retrieve")
graph.add_edge("retrieve", "grade")
graph.add_conditional_edges("grade", decide_next, {
    "generate": "generate",
    "rewrite": "rewrite"
})
graph.add_edge("rewrite", "retrieve")
graph.add_edge("generate", END)

rag_graph = graph.compile()