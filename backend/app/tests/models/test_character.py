# backend/app/tests/models/test_character.py

# RUN： 
# alembic revision --autogenerate -m "Create Character Table"
# alembic upgrade head
# pytest app/tests/models/test_character.py
from app.models.character import Character
from app.db.session import SessionLocal

def test_create_character():
    db = SessionLocal()
    character = Character(
        name="Test Character",
        class_type="Warrior",
        attributes={"strength": 10, "dexterity": 12},
        inventory=["sword", "shield"]
    )
    db.add(character)
    db.commit()
    db.refresh(character)
    assert character.id is not None
    db.close()
