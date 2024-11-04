# backend/app/models/character.py

from sqlalchemy import Column, Integer, String, JSON
from app.db.session import Base

class Character(Base):
    __tablename__ = 'characters'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)  # Character's name
    class_type = Column(String, nullable=False)  # Character's class (e.g., Warrior, Mage)
    attributes = Column(JSON, nullable=False)  # JSON for attributes (e.g., {"strength": 10, "dexterity": 12})
    inventory = Column(JSON, default=[])  # JSON for inventory (e.g., ["sword", "shield"])
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)

    # TODO: Consider adding skills/abilities in Sprint 2
