from graph.rag_graph import rag_graph


result = rag_graph.invoke(
    {
        "question":
        "What is context in RAG?",

        "documents":[],

        "answer":"",

        "rewrite_count":0
    }
)


print(result["answer"])