from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, JSON
from sqlalchemy.orm import relationship
from app.database.base import Base
from datetime import datetime

class GameSession(Base):
    __tablename__ = 'game_sessions'

    id = Column(Integer, primary_key=True)
    session_id = Column(String, unique=True, nullable=False)
    character_id = Column(Integer, ForeignKey('characters.id', name='fk_user_character_id'), nullable=False)
    language = Column(String, default="English")  # Language preference for session
    llm_provider = Column(String, default="zhipu_glm")  # LLM provider for session
    game_config = Column(JSON, nullable=True)  # Configurations like setting, story arc

    character = relationship('Character', back_populates="game_sessions")
    game_state = relationship('GameState', back_populates="game_session", uselist=False)
    
    created_at = Column(DateTime, default=datetime.now)  # Use datetime.now for default
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now) 
