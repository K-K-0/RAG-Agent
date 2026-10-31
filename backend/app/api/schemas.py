from pydantic import BaseModel

class AskRequest(BaseModel):
    question: str

class Source(BaseModel):
    source: str
    text: str

class AskResponse(BaseModel):
    answer: str
    source: list[Source]