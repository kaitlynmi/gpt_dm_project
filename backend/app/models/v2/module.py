# models/module.py
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import relationship
from app.database.base import Base

class Module(Base):
    __tablename__ = "modules"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    module_data = Column(JSON, nullable=True)  # JSONB with story nodes, NPCs, locations, etc.

    # Relationship to GameSession
    game_sessions = relationship("GameSession", back_populates="module")
