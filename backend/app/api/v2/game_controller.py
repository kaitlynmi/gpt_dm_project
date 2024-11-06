# game_controller.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.v2 import game_session_service

router = APIRouter()

class GameSessionRequest(BaseModel):
    language: str
    llm_provider: str
    module: str

class GameSessionResponse(BaseModel):
    game_id: int
    message: str
    narrative: str

@router.post("/start", response_model=GameSessionResponse)
async def start_game(request: GameSessionRequest):
    """
    Initialize a new game session with the specified configurations.

    - `language`: Preferred language for the session.
    - `llm_provider`: AI model provider for responses.
    - `module`: Game module selected for this session.
    """
    # TODO: Implement game session creation logic in game_service.py (Phase 2)
    mock_response = {
        "game_id": 1,  # Placeholder ID
        "message": "Game started successfully.",
        "narrative": "<Initial narrative text>"
    }
    return mock_response
