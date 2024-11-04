# backend/app/api/v1/endpoints/character.py

from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from pydantic import BaseModel
from app.services.character_service import CharacterService

router = APIRouter()

class CharacterCreateRequest(BaseModel):
    name: str
    class_type: str
    attributes: dict

class CharacterCreateResponse(BaseModel):
    character_id: int
    character_data: dict

@router.post("/character/create", response_model=CharacterCreateResponse)
async def create_character(request: CharacterCreateRequest, db: Session = Depends(get_db)):
    character_id, character_data = CharacterService(db).create_character(request.dict())
    return CharacterCreateResponse(character_id=character_id, character_data=character_data)

@router.get("/character/{character_id}", response_model=dict)
async def get_character(character_id: int, db: Session = Depends(get_db)):
    character_data = CharacterService(db).get_character(character_id)
    if not character_data:
        raise HTTPException(status_code=404, detail="Character not found")
    return character_data
