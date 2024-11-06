# backend/app/schemas/character.py

from pydantic import BaseModel
from typing import Dict, List, Any, Optional

class CharacterCreate(BaseModel):
    name: str
    class_type: str
    attributes: Dict[str, int]
class CharacterResponse(BaseModel):
    id: int
    game_session_id: int
    player_id: Optional[int] = None
    character_data: Dict
    type: str  # 'player' or 'npc'

    class Config:
        orm_mode = True
