# models/player.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database.base import Base

class Player(Base):
    __tablename__ = "players"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    game_session_id = Column(Integer, ForeignKey("game_sessions.id"))
    
    # Relationship to Character
    character = relationship("Character", back_populates="player", uselist=False)

    # Relationship to GameSession
    game_session = relationship("GameSession", back_populates="players")
