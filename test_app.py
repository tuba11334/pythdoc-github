import sys
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_root():
    if sys.version_info < (3, 13):
        import pytest
        pytest.skip("Requires Python 3.13 or higher")
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}

def test_read_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == {"items": ["item1", "item2", "item3"]}
