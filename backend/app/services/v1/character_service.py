# backend/app/services/character_service.py

from sqlalchemy.orm import Session
from app.models.v1.character import Character

class CharacterService:
    def __init__(self, db: Session):
        self.db = db

    def create_character(self, character_data: dict) -> tuple:
        # Unpack the dictionary and pass each key as a keyword argument to Character
        character = Character(
            name=character_data["name"],
            class_type=character_data["class_type"],
            attributes=character_data["attributes"],
            inventory=character_data.get("inventory", []),
            level=character_data.get("level", 1),
            experience=character_data.get("experience", 0)
        )
        self.db.add(character)
        self.db.commit()
        self.db.refresh(character)
        return character.id, character_data  # Returning ID and data for immediate retrieval

    def get_character(self, character_id: int) -> dict:
        character = self.db.query(Character).filter(Character.id == character_id).first()
        if character:
            return {
                "name": character.name,
                "class_type": character.class_type,
                "attributes": character.attributes,
                "inventory": character.inventory,
                "level": character.level,
                "experience": character.experience
            }
        return None
