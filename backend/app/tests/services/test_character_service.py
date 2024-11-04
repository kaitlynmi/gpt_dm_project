# backend/app/tests/services/test_character_service.py

from app.services.character_service import CharacterService
from app.db.session import SessionLocal

def test_create_and_get_character():
    db = SessionLocal()
    service = CharacterService(db)
    character_data = {
        "name": "Test Character",
        "class_type": "Mage",
        "attributes": {"intelligence": 10, "wisdom": 12},
        "inventory": ["magic staff"]
    }
    # Test character creation
    character_id, data = service.create_character(character_data)
    assert character_id is not None

    # Test retrieving character
    character = service.get_character(character_id)
    assert character is not None
    assert character["name"] == "Test Character"
    assert character["class_type"] == "Mage"
    db.close()
