from langchain_core.output_parsers import StrOutputParser

from retrieval.vector_store import VectorStore
from prompts.rag_prompt import rag_prompt
from llm.client import load_llm

class RAG:
    def __init__(self):
        self.retriever = VectorStore().get_retriever()
        self.llm = load_llm()
        self.chain = (
            rag_prompt | self.llm | StrOutputParser()
        )

    def ask(self, question):
        docs = self.retriever.invoke(question)
        context = '\n\n'.join(doc.page_content for doc in docs)

        return self.chain.invoke(
            {
                "context": context,
                "question": question
            }
        )