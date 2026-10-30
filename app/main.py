from graph.rag_graph import rag_graph


result = rag_graph.invoke(
    {
        "question": "what are the new rules in the programme?",

        "documents":[],

        "answer":"",

        "rewrite_count":0
    }
)
for i, doc in enumerate(result["documents"]):
    print("=" * 80)
    # print(f"Document {i}")
    # print(doc.metadata)
    print(doc.page_content)

print("Answer get: ", result["answer"])