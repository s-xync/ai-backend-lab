from pydantic import BaseModel
from uuid import UUID, uuid4

class DocumentCreate(BaseModel):
    title: str
    content: str

class DocumentResponse(BaseModel):
    id: UUID
    title: str
    content: str
