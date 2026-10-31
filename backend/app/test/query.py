import os
import sys
from dotenv import load_dotenv

# Ensure the root app directory is in Python's path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from retrieval.vector_store import VectorStore
from llm.client import load_llm  # Assuming your ChatOpenAI module is here

# 1. Load environment and components
load_dotenv()
vector_db = VectorStore()
retriever = vector_db.get_retriever()
llm = load_llm()

# 2. Define your strict RAG prompt
rag_prompt = ChatPromptTemplate.from_template("""
You are an AI assistant.

Answer ONLY from the provided context.

If the answer is not available in the context,
reply with:

"I don't know."

Context:
{context}

Question:
{question}

Answer:
""")

# 3. Build a helper function to format retrieved documents into raw text block
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# 4. Construct the LCEL RAG Chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
)

# 5. Run test queries
if __name__ == "__main__":
    print("\n--- Running Test Queries ---")
    
    # Test 1: Strict context test (Should answer correctly based on your document data)
    q1 = "Who is the security officer and what project is active?"
    print(f"\nQuestion: {q1}")
    response1 = rag_chain.invoke(q1)
    print(f"Response: {response1}")
    
    # Test 2: Out of context test (Should trigger your strict "I don't know" rule)
    q2 = "What is the capital of France?"
    print(f"\nQuestion: {q2}")
    response2 = rag_chain.invoke(q2)
    print(f"Response: {response2}")
