def chunk_text(text: str, chunk_size: int = 500, chunk_overlap: int = 50):
    chunks, start = [], 0
    while start <= len(text):
        chunk = text[start: start + chunk_size].strip()
        chunks.append(chunk)
        start += chunk_size - chunk_overlap

    return chunks