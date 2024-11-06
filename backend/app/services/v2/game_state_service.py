# services/game_state_service.py
from sqlalchemy.orm import Session
from app.repositories.game_state_repository import create_game_state, get_game_states_by_session, get_last_game_state_by_session

def add_game_state(db: Session, game_session_id: int, state_data: dict):
    """
    Service to add a new GameState to a session.
    """
    return create_game_state(db, game_session_id=game_session_id, state_data=state_data)

def fetch_game_states(db: Session, game_session_id: int):
    """
    Service to retrieve all GameStates for a specific GameSession.
    """
    return get_game_states_by_session(db, game_session_id=game_session_id)

def fetch_last_game_state(db: Session, game_session_id: int):
    """
    Service to retrieve the last GameState for a specific GameSession.
    """
    return get_last_game_state_by_session(db, game_session_id=game_session_id)