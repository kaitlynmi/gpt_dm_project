from sqlalchemy import Column, Integer, String
from app.db.session import Base

class GameState(Base):
    __tablename__ = "game_state"

    id = Column(Integer, primary_key=True, index=True)
    state_name = Column(String, index=True)
    description = Column(String)
