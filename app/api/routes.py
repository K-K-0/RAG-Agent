from fastapi import APIRouter
from app.api.schemas import AskRequest, AskResponse, Source
from app.graph.rag_graph import rag_graph
from app.ingestion.pipeline import ingest

router = APIRouter()

@router.post("/ask", response_model=AskResponse)
def ask(req: AskRequest):
    result = rag_graph.invoke({"question": req.question})
    return AskResponse(
        answer=result["answer"],
        source=[Source(source=d["source"], text=d["text"]) for d in result["docs"]]
    )

@router.post("ingest")
def run_ingest():
    return {"chunks_ingested": ingest()}

@router.get("/health")
def health():
    return {"status": "ok"}