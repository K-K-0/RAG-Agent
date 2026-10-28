from llm.client import load_llm
from langchain_core.prompts import ChatPromptTemplate

class QueryRewritter:

    def __init__(self):
        self.llm = load_llm()

        self.prompt = ChatPromptTemplate.from_template(
            """
            You are a query rewriting system for a RAG application.

            Rewrite the user question only to improve search.

            Rules:
            - Do not change the meaning.
            - Do not add new concepts.
            - Do not assume missing information.
            - Keep important keywords from the original question.

            Original question:
            {question}

            Return only the rewritten query.
            """
        )

        self.chain = ( self.prompt | self.llm )

    def rewrite(self, question):

        response = self.chain.invoke(
            {
                "question": question
            }
        )

        return response.content