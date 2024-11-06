# character_controller.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.v2 import character_service

router = APIRouter()

class CharacterCreateRequest(BaseModel):
    game_id: int
    name: str
    type: str  # 'player' or 'npc'
    stats: dict  # Placeholder for character stats and attributes

class CharacterResponse(BaseModel):
    character_id: int
    game_id: int
    name: str
    type: str
    stats: dict

@router.post("/create", response_model=CharacterResponse)
async def create_character(request: CharacterCreateRequest):
    """
    Endpoint to create a new character in the game session.

    - `game_id`: ID of the game session.
    - `name`: Name of the character.
    - `type`: Character type, either 'player' or 'npc'.
    - `stats`: Dictionary of character stats (e.g., health, skills).

    Returns the created character data.
    """
    # TODO: Implement character creation logic in character_service.py (Phase 2)
    mock_response = {
        "character_id": 1,  # Placeholder ID
        "game_id": request.game_id,
        "name": request.name,
        "type": request.type,
        "stats": request.stats
    }
    return mock_response
