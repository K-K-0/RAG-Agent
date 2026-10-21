from pathlib import Path
from pypdf import PdfReader

def load_document(data_dir: str) -> list[dict]:
    docs = []

    for path in Path(data_dir).glob("**/*"):
        if path.suffix.lower() in {".txt", ".md"}:
            text = path.read_text(encoding="utf-8")
        elif path.suffix.lower() == ".pdf":
            text = '\n'.join(p.extract_text() or "" for p in PdfReader(path).pages)
        else:
            continue
        docs.append({"source": path.name, "text": text})
    return docs