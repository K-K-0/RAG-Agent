RAG_PROMPT = """You are a helpful assistant. Answer the question using ONLY the context below.
If the answer is not in the context, say "I don't know based on the provided documents."

Context:
{context}

Question: {question}

Answer:"""

def build_prompt(question: str, docs: list[dict]) -> str:
    context = '\n\n'.join(f"[{d["source"]}], [{d["text"]}]" for d in docs)
    return RAG_PROMPT.format(context=context, question=question)