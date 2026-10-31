from pydantic import BaseModel


class DocumentMetadata(BaseModel):

    course_name: str | None = None
    course_code: str | None = None
    document_type: str | None = None
    level: str | None = None
    topic: str | None = None