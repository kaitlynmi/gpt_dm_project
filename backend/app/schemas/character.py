# backend/app/schemas/character.py

from pydantic import BaseModel
from typing import Dict, List, Any

class CharacterCreate(BaseModel):
    name: str
    class_type: str
    attributes: Dict[str, int]

class CharacterResponse(BaseModel):
    id: int
    name: str
    class_type: str
    attributes: Dict[str, int]
    inventory: List[Any]
    level: int
    experience: int

    class Config:
        orm_mode = True
