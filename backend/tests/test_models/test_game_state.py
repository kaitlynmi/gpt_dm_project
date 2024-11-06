# tests/test_models/test_game_state.py
from app.models.v2.game_session import GameSession
from app.models.v2.game_state import GameState
from sqlalchemy.orm import Session

def test_game_state_creation(db_session: Session):
    # Step 1: Create a GameSession to associate with GameState
    game_session = GameSession(language="English", llm_provider="Zhipu GLM", module_id=None)
    db_session.add(game_session)
    db_session.commit()

    # Step 2: Create a GameState associated with the GameSession
    state_data = {
        "location": "Library",
        "description": "A dusty library with shelves of old books.",
        "events": []
    }
    game_state = GameState(game_session_id=game_session.id, state_data=state_data)
    db_session.add(game_state)
    db_session.commit()

    # Step 3: Retrieve GameState and verify data
    retrieved_state = db_session.query(GameState).filter(GameState.id == game_state.id).first()
    assert retrieved_state is not None
    assert retrieved_state.state_data["location"] == "Library"
    assert retrieved_state.state_data["description"] == "A dusty library with shelves of old books."
    assert retrieved_state.session.id == game_session.id

    # Step 4: Add additional GameState and verify relationship with GameSession
    another_state_data = {
        "location": "Study Room",
        "description": "A small, dimly lit room with a desk and some scattered papers.",
        "events": []
    }
    another_game_state = GameState(game_session_id=game_session.id, state_data=another_state_data)
    db_session.add(another_game_state)
    db_session.commit()

    # Ensure that the GameSession has two GameStates
    states = db_session.query(GameState).filter(GameState.game_session_id == game_session.id).all()
    assert len(states) == 2
    assert states[0].state_data["location"] == "Library"
    assert states[1].state_data["location"] == "Study Room"
