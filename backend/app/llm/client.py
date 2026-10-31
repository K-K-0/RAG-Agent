from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()


def load_llm():

    return ChatGroq(
        model="openai/gpt-oss-120b",
        temperature=0,
        api_key=os.getenv("GROQ_API_KEY")
    )