# backend/app/services/game_service.py

from sqlalchemy.orm import Session
from app.models.game_session import GameSession
from app.models.character import Character
from app.db.session import SessionLocal
from app.services.game_state_service import GameStateService
import uuid

class GameSessionNotFoundError(Exception):
    """Custom exception for missing GameSession."""
    pass

class GameService:
    def __init__(self):
        self.db = SessionLocal()

    def generate_session_id(self) -> str:
        """Generate a unique session ID using UUID."""
        return str(uuid.uuid4())

    def start_new_game(self, character_id: int) -> GameSession:
        """Starts a new game session and initializes GameState."""
        character_service = CharacterService(self.db)
        character = character_service.get_character_by_id(character_id)

        session_id = self.generate_session_id()
        new_session = GameSession(session_id=session_id, character_id=character.id)
        self.db.add(new_session)
        self.db.commit()
        self.db.refresh(new_session)

        initial_state = self._get_initial_game_state()
        game_state_service = GameStateService(self.db)
        game_state_service.create_initial_game_state(new_session.id, initial_state)

        return new_session
    
    def start_new_game(self, character_id: int) -> GameSession:
        """Starts a new game session and initializes GameState."""
        character_service = CharacterService(self.db)
        character = character_service.get_character_by_id(character_id)

        session_id = self.generate_session_id()
        new_session = GameSession(session_id=session_id, character_id=character.id)
        self.db.add(new_session)
        self.db.commit()
        self.db.refresh(new_session)

        initial_state = self._get_initial_game_state()
        game_state_service = GameStateService(self.db)
        game_state_service.create_initial_game_state(new_session.id, initial_state)

        return new_session

    def get_session_by_id(self, session_id: str) -> GameSession:
        """Retrieve a game session by its session ID."""
        session = self.db.query(GameSession).filter(GameSession.session_id == session_id).first()
        if not session:
            raise GameSessionNotFoundError(f"GameSession with id {session_id} not found.")
        return session

    def save_game(self, session_id: str):
        """Save the current game state for a session."""
        session = self.db.query(GameSession).filter_by(session_id=session_id).first()
        if not session:
            return False, f"GameSession with id {session_id} not found."

        self.db.commit()  # Commit current session changes
        return True, "Game state saved successfully"

    def _get_initial_game_state(self) -> dict:
        """Get the initial state for a new game session."""
        return {"status": "initialized"} 
        # placeholder for initial game state. Customize later for specific campaigns