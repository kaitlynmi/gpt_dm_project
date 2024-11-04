# backend/app/services/game_state_service.py

from sqlalchemy.orm import Session
from app.models.game_state import GameState
from app.db.session import SessionLocal

class GameStateService:
    def __init__(self, db: Session = SessionLocal()):
        self.db = db

    def create_initial_game_state(self, game_session_id: int, state_data: dict) -> GameState:
        # Create a default initial state for a new game session
        if state_data is None:
            state_data = {
                "status": "initialized",
                "location": "dummy village",  # Placeholder for the initial location
                "treats": [],
                "quests": []  # Placeholder for potential quests
            }

        new_game_state = GameState(
            game_session_id=game_session_id,
            state_data=state_data
        )
        self.db.add(new_game_state)
        self.db.commit()
        return new_game_state

    def get_game_state(self, game_session_id: int) -> GameState:
        # Retrieve the current game state by session id
        game_state = self.db.query(GameState).filter(GameState.game_session_id == game_session_id).first()
        if not game_state:
            raise Exception(f"GameState for session {game_session_id} not found.")
        return game_state

    def update_game_state(self, game_session_id: int, new_state_data: dict) -> GameState:
        # Retrieve the current game state
        game_state = self.db.query(GameState).filter(GameState.game_session_id == game_session_id).first()
        if not game_state:
            raise Exception(f"GameState for session {game_session_id} not found.")

        # Update the game state with new data
        game_state.state_data.update(new_state_data)
        self.db.commit()
        return game_state
