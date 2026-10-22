from langchain_core.prompts import ChatPromptTemplate

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