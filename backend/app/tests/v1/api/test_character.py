# backend/app/tests/api/test_character.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client  # The test client will be used across all test functions

def test_create_character(test_client):
    response = test_client.post("/api/v1/character/create", json={
        "name": "Test Character",
        "class_type": "Mage",
        "attributes": {
            "intelligence": 10,
            "wisdom": 12
        }
    })
    assert response.status_code == 200
    assert response.json()["character_id"] is not None

def test_get_character(test_client):
    response = test_client.get("/api/v1/character/1")  # Assuming character 1 exists from creation test
    assert response.status_code == 200
    assert "name" in response.json()

def test_create_character_missing_fields(test_client):
    response = test_client.post("/api/v1/character/create", json={"class_type": "Mage"})
    assert response.status_code == 422  # Unprocessable entity

# def test_create_character_negative_attributes(test_client):
#     response = test_client.post("/api/v1/character/create", json={
#         "name": "Test Character",
#         "class_type": "Mage",
#         "attributes": {"strength": -1, "dexterity": -2}
#     })
#     assert response.status_code == 422  # Custom validation error expected

def test_create_character_valid(test_client):
    response = test_client.post("/api/v1/character/create", json={
        "name": "Valid Character",
        "class_type": "Mage",
        "attributes": {"strength": 10, "dexterity": 12}
    })
    assert response.status_code == 200
    assert response.json()["character_id"] is not None

def test_get_character_not_found(test_client):
    response = test_client.get("/api/v1/character/9999")  # Assuming ID 9999 doesn't exist
    assert response.status_code == 404