from fastapi import APIRouter
from app.core.auth import issue_dev_token

router = APIRouter(tags=["Dev Auth"])

@router.post("/dev/token")
def get_dev_token(user_id: str, tenant_id: str):
    token = issue_dev_token(user_id, tenant_id)
    return {"access_token": token, "token_type": "bearer"}
