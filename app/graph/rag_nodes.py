from retrieval.hybrid import HybridRetriever
from retrieval.grader_filter import GradedRetrival
from retrieval.query_rewriter import QueryRewritter
from llm.client import load_llm


retriever = HybridRetriever()

grader = GradedRetrival()

query_rewriter = QueryRewritter()

llm = load_llm()



def retrieve_node(state):

    question = state["question"]

    documents = retriever.retrieve(
        question
    )

    # for i, doc in enumerate(documents):
    #     print("\n========== DOCUMENT", i, "==========")
    #     print(doc.metadata)
    #     print(doc.page_content[:500])

    return {
        "documents": documents
    }



def grade_node(state):

    question = state["question"]

    documents = state["documents"]

    filtered_documents = grader.filter_document(
        question,
        documents
    )

    return {
        "documents": filtered_documents
    }



def rewrite_node(state):

    question = state["question"]

    new_question = query_rewriter.rewrite(
        question
    )

    return {
        "question": new_question,
        "rewrite_count": state["rewrite_count"] + 1
    }



def generate_node(state):

    question = state["question"]

    documents = state["documents"]


    context = "\n\n".join(
        doc.page_content
        for doc in documents
    )


    prompt = f"""
    Answer using only this context.

    Context:
    {context}

    Question:
    {question}
    """


    response = llm.invoke(prompt)


    return {
        "answer": response.content
    }



def decide_next(state):

    documents = state["documents"]

    if len(documents) > 0:
        return "generate"


    if state["rewrite_count"] >= 2:
        return "generate"


    return "rewrite"