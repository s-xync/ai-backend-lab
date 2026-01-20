
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_document():
    response = client.post("/v1/documents",json={
        "title":"Test Doc",
        "content":"Test Doc Content"
    })

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Doc"
