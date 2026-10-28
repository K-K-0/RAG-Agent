import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

from loader import PDFLoader
from splitter import DocumentSplitter
from retrieval.vector_store import VectorStore
from retrieval.bm25_indexing import BM25Indexer
from prompts.extractor import MetadataExtractor
from llm.client import load_llm


def ingest(pdf_path):

    loader = PDFLoader(pdf_path)
    documents = loader.load()
    llm = load_llm()
    extractor = MetadataExtractor(llm)
    document_text = "\n".join(
        [
            doc.page_content
            for doc in documents[:5]
        ]
    )
    metadata = extractor.extract(document_text)
    splitter = DocumentSplitter()
    chunks = splitter.split(documents)

    for chunk in chunks:
        chunk.metadata.update(metadata)
    
    vector_store = VectorStore()
    vector_store.add_document(chunks)

    BM25Indexer.build(chunks)

    print(f"\nFile: {pdf_path}")
    print(f"Pages Loaded: {len(documents)}")
    print(f"Chunks Created: {len(chunks)}")

    return chunks



def ingest_all(data_path):

    pdf_files = [
        file for file in os.listdir(data_path)
        if file.endswith(".pdf")
    ]

    all_chunks = []

    for pdf in pdf_files:

        pdf_path = os.path.join(
            data_path,
            pdf
        )

        chunks = ingest(pdf_path)

        all_chunks.extend(chunks)


    print("\nTotal Chunks:", len(all_chunks))

    return all_chunks



if __name__ == "__main__":

    chunks = ingest_all(
       '/home/k-k/RAG/data'
    )

    print("\n--- First Chunk ---")
    print(chunks[0].page_content)