from fastapi import APIRouter, Depends, HTTPException
from uuid import uuid4
from app.core.auth import get_current_user
from app.core.tenant import get_tenant_id
from app.models.document import DocumentCreate, DocumentResponse

router = APIRouter(tags=["Documents"])

DB = {}

@router.post("/documents", response_model=DocumentResponse)
def create_document(payload: DocumentCreate, user=Depends(get_current_user), tenant_id=Depends(get_tenant_id)):
    doc_id = uuid4()
    document = {
        "id": doc_id,
        "title": payload.title,
        "content": payload.content
    }
    DB[str(doc_id)] = document
    return document

@router.get("/documents/{doc_id}", response_model=DocumentResponse)
def get_document(doc_id: str ):
    if doc_id not in DB:
        raise HTTPException(status_code=404, detail="Document not found")
    return DB[doc_id]
