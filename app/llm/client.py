import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv() 

def load_llm():
    return ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        openai_api_base="https://aipipe.org/openai/v1", 
        openai_api_key=os.getenv("OPENAI_API_KEY") 
    )
