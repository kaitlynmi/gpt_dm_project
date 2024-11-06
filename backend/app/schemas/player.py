# schemas/player.py
from pydantic import BaseModel
from .character import CharacterResponse

class PlayerResponse(BaseModel):
    id: int
    name: str
    character: CharacterResponse
