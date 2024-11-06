# repositories/game_session_repository.py
from sqlalchemy.orm import Session
from app.models.v2.game_session import GameSession

from typing import Optional

def create_game_session(db: Session, language: str, llm_provider: str, module: Optional[int] = None):
    new_session = GameSession(language=language, llm_provider=llm_provider, module_id=module)
    db.add(new_session)
    db.commit()
    db.refresh(new_session)
    return new_session

def get_game_session(db: Session, session_id: int):
    return db.query(GameSession).filter(GameSession.id == session_id).first()

