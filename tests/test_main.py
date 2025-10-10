import pytest
from fastapi.testclient import TestClient
from ..main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_chat():
    response = client.post("/chat", json={"prompt": "Hello"})
    assert response.status_code == 200
    assert "response" in response.json()