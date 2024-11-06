# models/character.py
from sqlalchemy import Column, Integer, String, JSON, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    game_session_id = Column(Integer, ForeignKey("game_sessions.id"), nullable=False)
    player_id = Column(Integer, ForeignKey("players.id"), nullable=True)  # Nullable for NPCs
    character_data = Column(JSON, nullable=False)  # Store stats, skills, etc.
    type = Column(String, nullable=False)  # 'player' or 'npc'

    # Relationship back to Player (one-to-one)
    player = relationship("Player", back_populates="character")

    # Relationship back to GameSession (many-to-one)
    session = relationship("GameSession", back_populates="characters")
