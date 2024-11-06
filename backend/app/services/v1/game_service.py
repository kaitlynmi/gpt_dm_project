# backend/app/services/game_service.py
from datetime import datetime
from sqlalchemy.orm import Session
from app.models.v1.game_session import GameSession
from app.models.v1.game_state import GameState
from app.database.session import SessionLocal
from app.services.v1.character_service import CharacterService
from app.services.v1.game_state_service import GameStateService
# from app.services.v1.ai.ai_service_dispatcher import AIServiceDispatcher
from uuid import uuid4

class GameSessionNotFoundError(Exception):
    """Custom exception for missing GameSession."""
    pass

class GameService:
    def __init__(self, db: Session = SessionLocal()):
        self.db = db
        self.game_state_service = GameStateService(self.db)
        # self.dispatcher = AIServiceDispatcher()

    def generate_session_id(self) -> str:
        """Generate a unique session ID using UUID."""
        return str(uuid4())

    @staticmethod
    async def start_game(request_data: dict) -> dict:
        """
        Starts a new game session with the given character and configuration.
        
        Parameters:
        - request_data (dict): Contains character_id, language, llm_provider, and game_config.

        Returns:
        - dict: Initial game state and narrative.
        """
        db: Session = SessionLocal()

        # Step 1: Create a new game session entry in the database
        session_id = str(uuid4())
        character_id = request_data["character_id"]
        language = request_data.get("language", "Chinese")
        llm_provider = request_data.get("llm_provider", "zhipu_glm")
        game_config = request_data.get("game_config", {})

        new_game_session = GameSession(
            session_id=session_id,
            character_id=character_id,
            language=language,
            llm_provider=llm_provider,
            game_config=game_config,
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        db.add(new_game_session)
        db.commit()
        db.refresh(new_game_session)

        # Step 2: Initialize a basic game state
        initial_game_state = {
            "location": "Starting Town",
            "inventory": [],
            "health": 100,
            "story_context": "You arrive in a bustling medieval town."
        }

        # Create the GameState entry in the database
        new_game_state = GameState(
            game_session_id=new_game_session.id,
            state_data=initial_game_state,
            last_updated=datetime.now()
        )
        db.add(new_game_state)
        db.commit()
        db.refresh(new_game_state)

        # Step 3: Mock initial narrative using AIServiceDispatcher (mocking GLM-4-Long response)
        ai_response = {"narrative": "You find yourself in a bustling medieval town...", "additional_data": {}}

        # Step 4: Return initial game state and narrative
        return {
            "session_id": session_id,
            "narrative": ai_response["narrative"],
            "game_state": initial_game_state
        }

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
        
    async def process_action(self, session_id: str, action_data: dict) -> dict:
        """
        Processes a player's action by:
        1. Determining the type of task (e.g., narrative, rule enforcement).
        2. Routing the task to the appropriate AI model.
        3. Updating the game state based on the response.

        Parameters:
        - session_id (str): Identifier for the current game session.
        - action_data (dict): Contains the action and additional context.

        Returns:
        - dict: Updated narrative and game state.
        """
        # Step 1: Determine task type based on action or context (placeholder logic)
        task_type = "narrative" if "story" in action_data.get("action", "").lower() else "rule_enforcement"
        
        # Step 2: Route the action to the appropriate AI model via the dispatcher
        ai_response = self.dispatcher.route_task(task_type, action_data)

        # Step 3: Update game state (placeholder logic for now)
        updated_game_state = self.update_game_state(session_id, ai_response)

        return {
            "narrative": ai_response.get("narrative"),
            "game_state": updated_game_state
        }

    def update_game_state(self, session_id: str, ai_response: dict) -> dict:
        """
        Updates the game state based on AI model response.
        TODO: Implement state update logic in Sprint 2, such as adjusting player health, inventory, etc.
        """
        # Placeholder logic for game state update
        db: Session = SessionLocal()
        game_state = db.query(GameState).filter(GameState.session_id == session_id).first()
        if game_state:
            # Modify game_state based on ai_response
            # This could include changes to inventory, location, NPCs, etc.
            game_state.state_data.update(ai_response.get("additional_data", {}))
            db.commit()
            db.refresh(game_state)
        return game_state.state_data if game_state else {}