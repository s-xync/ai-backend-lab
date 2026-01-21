from fastapi import APIRouter, Depends, HTTPException
from uuid import uuid4

from sqlalchemy.orm import Session
from app.core.auth import get_current_user
from app.core.tenant import get_tenant_id
from app.db.dependencies import get_db
from app.db.models.document import Document
from app.models.document import DocumentCreate, DocumentResponse

router = APIRouter(tags=["Documents"])

DB = {}


@router.post("/documents", response_model=DocumentResponse)
def create_document(
    payload: DocumentCreate,
    user=Depends(get_current_user),
    tenant_id=Depends(get_tenant_id),
    db: Session = Depends(get_db),
):
    # doc_id = uuid4()
    # document = {
    #     "id": doc_id,
    #     "title": payload.title,
    #     "content": payload.content
    # }
    # DB[str(doc_id)] = document
    # return document
    doc = Document(tenant_id=tenant_id, title=payload.title, content=payload.content)
    db.add(doc)
    db.flush()
    return doc


@router.get("/documents/{doc_id}", response_model=DocumentResponse)
def get_document(
    doc_id: str, tenant_id=Depends(get_tenant_id), db: Session = Depends(get_db)
):
    # if doc_id not in DB:
    #     raise HTTPException(status_code=404, detail="Document not found")
    # return DB[doc_id]
    doc = db.query(Document).filter(
        Document.id == doc_id, Document.tenant_id == tenant_id
    ).first()

    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    return doc
