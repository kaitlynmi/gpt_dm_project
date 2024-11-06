# schemas/game_session.py
from pydantic import BaseModel
from typing import List, Optional
from .character import CharacterResponse
from .player import PlayerResponse

class GameSessionRequest(BaseModel):
    language: str
    llm_provider: str
    module: Optional[str] = None

class GameSessionResponse(BaseModel):
    id: int
    language: str
    llm_provider: str
    module: Optional[str] = None
    players: List[PlayerResponse]
    characters: List[CharacterResponse]
