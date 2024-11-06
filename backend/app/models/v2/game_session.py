# models/game_session.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database.base import Base

class GameSession(Base):
    __tablename__ = "game_sessions"

    id = Column(Integer, primary_key=True, index=True)
    language = Column(String, nullable=False)
    llm_provider = Column(String, nullable=False)
    module_id = Column(Integer, ForeignKey("modules.id"), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # Relationship to Players (one-to-many)
    players = relationship("Player", back_populates="game_session")

    # Relationship to GameStates (one-to-many)
    game_states = relationship("GameState", back_populates="session")
    
    # Relationship to Characters (one-to-many)
    characters = relationship("Character", back_populates="session")

    # Relationship to Module (one-to-one)
    module = relationship("Module", back_populates="game_sessions")