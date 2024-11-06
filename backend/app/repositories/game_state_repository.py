# repositories/game_state_repository.py
from sqlalchemy.orm import Session
from app.models.v2.game_state import GameState


def create_game_state(db: Session, game_session_id: int, state_data: dict):
    """
    Create a new game state for a specific game session.
    """
    new_state = GameState(
        game_session_id=game_session_id,
        state_data=state_data
    )
    db.add(new_state)
    db.commit()
    db.refresh(new_state)
    return new_state

def get_game_states_by_session(db: Session, game_session_id: int):
    return db.query(GameState).filter(GameState.game_session_id == game_session_id).all()

def get_last_game_state_by_session(db: Session, game_session_id: int):
    return db.query(GameState).filter(GameState.game_session_id == game_session_id).order_by(GameState.id.desc()).first()