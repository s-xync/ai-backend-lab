from fastapi import FastAPI
from app.api.documents import router as document_router
from app.api.dev_auth import router as dev_auth_router
from app.core.middleware import audit_middleware
# from app.core.errors import register_exception_handlers

app = FastAPI(title="AI Backend Lab")

# register_exception_handlers(app)
app.middleware("http")(audit_middleware)
app.include_router(document_router, prefix="/v1")

# DEV ONLY — replace with external IdP in production
app.include_router(dev_auth_router, prefix="/v1")
