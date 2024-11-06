# tests/test_schemas/test_game_session_schema.py
from app.schemas.game_session import GameSessionRequest, GameSessionResponse

def test_game_session_request_schema():
    request_data = {
        "language": "English",
        "llm_provider": "Zhipu GLM",
        "module": "Book Chaser"
    }
    request = GameSessionRequest(**request_data)
    assert request.language == "English"
    assert request.llm_provider == "Zhipu GLM"

def test_game_session_response_schema():
    response_data = {
        "id": 1,
        "language": "English",
        "llm_provider": "Zhipu GLM",
        "module": "Book Chaser",
        "players": [],
        "characters": []
    }
    response = GameSessionResponse(**response_data)
    assert response.id == 1
    assert response.language == "English"
