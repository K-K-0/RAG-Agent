from langchain_community.document_loaders import PyPDFLoader

class PDFLoader:

    def __init__(self, path: str):
        self.path = path

    def load(self):
        loader = PyPDFLoader(self.path)
        return loader.load()
    