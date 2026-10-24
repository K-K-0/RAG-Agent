from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

class QueryRewritter:

    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

        self.prompt = ChatPromptTemplate.from_template(
            """
            You are a search query optimizer.

            Rewrite the user question into a better
            query for document retrieval.

            Make it:
            - specific
            - descriptive
            - keyword rich

            Original question:
            {question}

            Improved search query:
            """
        )

        self.chain = ( self.llm | self.prompt )

    def rewrite(self, question):

        response = self.chain.invoke(
            {
                "question": question
            }
        )

        return response.content