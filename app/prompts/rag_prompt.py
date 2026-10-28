from langchain_core.prompts import ChatPromptTemplate

rag_prompt = ChatPromptTemplate.from_template("""

You are a RAG assistant.

Answer only from the given context.

Use this structure:

## Answer

## Key Points
- point 1
- point 2

## Important Dates
- date information

## Formula / Rules
- formulas or conditions

## Source
Mention the document section if available.

Context:

{context}

Question:

{question}

""")