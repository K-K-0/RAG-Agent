from langchain_community.document_loaders import PyMuPDFLoader

class PDFLoader:

    def __init__(self, path: str):
        self.path = path

    def load(self):
        loader = PyMuPDFLoader(self.path)
        documents = loader.load()

        for doc in documents:

            doc.metadata.update(
                {
                    "source": self.path,
                    "document_type": "pdf"
                }
            )


        return documents
    