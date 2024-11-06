# tests/test_services/test_game_state_service.py
from app.services.v2.game_state_service import add_game_state, fetch_game_states
from app.services.v2.game_state_service import fetch_last_game_state
from app.models.v2.game_session import GameSession

def test_add_game_state_service(db_session):
    # Create a test GameSession first
    session = GameSession(language="English", llm_provider="Zhipu GLM", module_id=None)
    db_session.add(session)
    db_session.commit()

    # Add a GameState using the service
    state_data = {"location": "Haunted Forest", "description": "Foggy and eerie"}
    game_state = add_game_state(db_session, game_session_id=session.id, state_data=state_data)
    assert game_state.state_data["location"] == "Haunted Forest"

def test_fetch_game_states_service(db_session):
    # Create a GameSession and multiple GameStates
    session = GameSession(language="English", llm_provider="Zhipu GLM", module_id=None)
    db_session.add(session)
    db_session.commit()

    add_game_state(db_session, game_session_id=session.id, state_data={"location": "Castle"})
    add_game_state(db_session, game_session_id=session.id, state_data={"location": "Dungeon"})

    # Fetch GameStates
    game_states = fetch_game_states(db_session, session.id)
    assert len(game_states) == 2
    assert game_states[0].state_data["location"] == "Castle"
    assert game_states[1].state_data["location"] == "Dungeon"

def test_fetch_last_game_state_service(db_session):
    # Create a GameSession and multiple GameStates
    session = GameSession(language="English", llm_provider="Zhipu GLM", module_id=None)
    db_session.add(session)
    db_session.commit()

    add_game_state(db_session, game_session_id=session.id, state_data={"location": "Castle"})
    add_game_state(db_session, game_session_id=session.id, state_data={"location": "Dungeon"})

    # Fetch the last GameState
    last_state = fetch_last_game_state(db_session, session.id)
    assert last_state.state_data["location"] == "Dungeon"