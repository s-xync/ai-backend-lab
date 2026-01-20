from fastapi import HTTPException, Depends
from datetime import datetime, timedelta
from jose import JWTError, jwt
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY="HIGHLY_SECRET"
JWT_ALGO="HS256"
security = HTTPBearer()

def create_access_token(data:dict, expiration_minutes:int=60):
    to_encode = data.copy()
    to_encode["exp"] = datetime.utcnow() + timedelta(minutes=expiration_minutes)
    return jwt.encode(to_encode, SECRET_KEY, algorithm=JWT_ALGO)

def get_current_user(credentials: HTTPAuthorizationCredentials=Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[JWT_ALGO])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def issue_dev_token(user_id: str, tenant_id: str, role: str = "user"):
    payload = {
        "sub": user_id,
        "tenant_id": tenant_id,
        "role": role,
        "iss":"dev-auth"
    }
    return create_access_token(payload)
