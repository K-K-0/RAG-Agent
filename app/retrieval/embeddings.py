from langchain_openai import OpenAIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

class Embedder:

    def __init__(self):
        self.embedding = OpenAIEmbeddings(
            model="text-embedding-3-small",
            openai_api_base="https://aipipe.org/openai/v1",  
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

    def get_embedding(self):
        return self.embedding