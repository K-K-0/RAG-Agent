from langchain_openai import ChatOpenAI
from llm.client import load_llm
from langchain_core.prompts import ChatPromptTemplate

class DocumentGrader:

    def __init__(self):
        self.llm = self.llm = load_llm()

        self.prompt = ChatPromptTemplate.from_template(
            """
            You are a document relevance grader.

            Question:
            {question}

            Document:
            {document}


            Decide if the document is useful.

            Reply only:
            yes
            or
            no
            """
        )

        self.chain = ( self.prompt | self.llm )

    def grade(self, question, document):

        response = self.chain.invoke(
            {
                "question": question,
                "document": document
            }
        )

        return response.content.lower()