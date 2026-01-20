from fastapi import HTTPException, Header

def get_tenant_id(x_tenant_id: str = Header(None)):
    if not x_tenant_id:
        raise HTTPException(status_code=400, detail="Missing tenant header")
    return x_tenant_id
