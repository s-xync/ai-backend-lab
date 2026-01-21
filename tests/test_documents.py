from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def get_auth_token(user_id: str = "test_user", tenant_id: str = "test_tenant"):
    response = client.post(
        "/v1/dev/token", params={"user_id": user_id, "tenant_id": tenant_id}
    )
    assert response.status_code == 200
    return response.json()["access_token"]


def get_headers(tenant_id: str = "test_tenant", user_id: str = "test_user"):
    token = get_auth_token(user_id=user_id, tenant_id=tenant_id)
    return {"Authorization": f"Bearer {token}", "x-tenant-id": tenant_id}


def create_document():
    headers = get_headers()
    response = client.post(
        "/v1/documents",
        json={"title": "Test Doc", "content": "Test Doc Content"},
        headers=headers,
    )
    return response


def test_create_document():
    response = create_document()

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Doc"


def test_tenant_isolation():
    create_response = create_document()
    create_response_data = create_response.json()
    headers = get_headers()
    headers["x-tenant-id"] = "malicious_tenant"
    get_response = client.get(
        f"/v1/documents/{create_response_data["id"]}", headers=headers
    )
    assert get_response.status_code == 404
