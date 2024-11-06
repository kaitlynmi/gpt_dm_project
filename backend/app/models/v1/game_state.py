# backend/app/models/game_state.py

from sqlalchemy import Column, Integer, ForeignKey, String, JSON, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database.session import Base

class GameState(Base):
    __tablename__ = 'game_states'

    id = Column(Integer, primary_key=True)
    game_session_id = Column(Integer, ForeignKey('game_sessions.id'), nullable=False)
    state_data = Column(JSON, nullable=False, default={})
    last_updated = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    game_session = relationship("GameSession", back_populates="game_state")

    # TODO: Further refine state_data structure to include complex AI-driven data like NPC statuses.
