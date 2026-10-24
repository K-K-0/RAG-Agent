from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

class DocumentGrader:

    def __init__(self):
        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

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