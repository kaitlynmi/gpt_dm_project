import pytest
from fastapi.testclient import TestClient
from app.main import app

# RUN: @gpt_dm_project: PYTHONPATH=./backend pytest backend/app/tests/test_api.py
# Set up a client to be used in tests
@pytest.fixture(scope="module")
def test_client():
    client = TestClient(app)
    yield client  # The test client will be used across all test functions

# Test the dice roll API with valid parameters
def test_roll_dice_success(test_client):
    response = test_client.get("/api/v1/game/roll_dice?sides=20")
    assert response.status_code == 200
    assert "result" in response.json()
    assert 1 <= response.json()["result"] <= 20  # Ensure result is between 1 and 20

# Test the dice roll API with invalid parameters (e.g., fewer than 2 sides)
def test_roll_dice_invalid_sides(test_client):
    response = test_client.get("/api/v1/game/roll_dice?sides=1")
    assert response.status_code == 400
    assert response.json() == {"detail": "Dice must have at least 2 sides."}

# Add more test cases here as you add more API endpoints
