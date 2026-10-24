from langchain_core.output_parsers import StrOutputParser

from retrieval.vector_store import VectorStore
from prompts.rag_prompt import rag_prompt
from llm.client import load_llm
from retrieval.query_rewriter import QueryRewritter

class RAG:
    def __init__(self):
        self.retriever = VectorStore().get_retriever()
        self.llm = load_llm()
        self.chain = (
            rag_prompt | self.llm | StrOutputParser()
        )

    def ask(self, question):
        rewritter = QueryRewritter()
        rerwitten_query = rewritter.rewrite(question)
        docs = self.retriever.invoke(rerwitten_query)
        context = '\n\n'.join(doc.page_content for doc in docs)

        return self.chain.invoke(
            {
                "context": context,
                "question": question
            }
        )