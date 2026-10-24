from llm.grader import  DocumentGrader

class GradedRetrival:

    def __init__(self):
        self.grader = DocumentGrader()


    def filter_document(self, question, documents):

        good_document = []

        for doc in documents:
            result = self.grader.grade(question, doc.page_content)

            if "yes" in result:
                good_document.append(doc)

        return good_document