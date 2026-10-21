import pytest
from app.ingestion.chunker import chunk_text


def test_chunks_overlaps():
    chunks = chunk_text("a" * 1000, chunk_size=500, chunk_overlap=100)
    assert len(chunks) == 3
    assert all(len(c) <= 500 for c in chunks)

def test_bad_overlap():
    with pytest.raises(ValueError):
        chunk_text("hello", chunk_size=10, chunk_overlap=10)