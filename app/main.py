from fastapi import FastAPI
from app.api.documents import router
# from app.core.errors import register_exception_handlers

app = FastAPI(title="AI Backend Lab")

# register_exception_handlers(app)
app.include_router(router, prefix="/v1")
