# tests/test_api/test_game_session.py
import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_start_game_endpoint():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.post("/api/v2/game/start", json={
            "language": "English",
            "llm_provider": "Zhipu GLM",
            "module": "Book Chaser"
        })
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Game started successfully."
