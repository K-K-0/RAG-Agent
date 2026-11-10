import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)


from retrieval.hybrid import HybridRetriever
from retrieval.grader_filter import GradedRetrival
from retrieval.query_rewriter import QueryRewritter
from llm.client import load_llm


retriever = None
grader = None
rewriter = None
llm = None



def get_retriever():

    global retriever

    if retriever is None:
        retriever = HybridRetriever()

    return retriever



def get_grader():

    global grader

    if grader is None:
        grader = GradedRetrival()

    return grader



def get_rewriter():

    global rewriter

    if rewriter is None:
        rewriter = QueryRewritter()

    return rewriter



def get_llm():

    global llm

    if llm is None:
        llm = load_llm()

    return llm



def retrieve_node(state):

    retriever = get_retriever()

    docs = retriever.retrieve(
        state["question"]
    )
    print(docs)

    return {
        "documents": docs
    }




def grade_node(state):

    grader = get_grader()

    filtered_documents = grader.filter_document(
        state["question"],
        state["documents"]
    )

    return {
        "documents": filtered_documents
    }



def rewrite_node(state):

    rewriter = get_rewriter()

    new_question = rewriter.rewrite(
        state["question"]
    )

    return {
        "question": new_question,
        "rewrite_count": state["rewrite_count"] + 1
    }



def generate_node(state):

    llm = get_llm()

    context = "\n\n".join(
        doc.page_content
        for doc in state["documents"]
    )


    prompt = f"""
    Answer using only this context.

    Context:
    {context}

    Question:
    {state["question"]}
    """


    response = llm.invoke(prompt)


    return {
        "answer": response.content
    }



def decide_next(state):

    if len(state["documents"]) > 0:
        return "generate"


    if state["rewrite_count"] >= 2:
        return "generate"


    return "rewrite"