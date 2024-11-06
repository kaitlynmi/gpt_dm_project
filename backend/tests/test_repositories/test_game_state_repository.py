# tests/test_repositories/test_game_state_repository.py
from app.repositories.game_state_repository import create_game_state, get_game_states_by_session
from app.models.v2.game_session import GameSession

def test_create_game_state(db_session):
    # Create a GameSession for testing
    session = GameSession(language="English", llm_provider="Zhipu GLM", module_id=None)
    db_session.add(session)
    db_session.commit()

    # Create a GameState
    state_data = {"location": "Mysterious Forest", "description": "The forest is quiet, with an eerie fog hanging low."}
    game_state = create_game_state(db_session, game_session_id=session.id, state_data=state_data)

    # Assertions
    assert game_state.game_session_id == session.id
    assert game_state.state_data["location"] == "Mysterious Forest"

def test_get_game_states_by_session(db_session):
    # Set up GameSession and multiple GameStates
    session = GameSession(language="English", llm_provider="Zhipu GLM", module_id=None)
    db_session.add(session)
    db_session.commit()

    state_data_1 = {"location": "Castle Gate", "description": "An ancient gate stands tall."}
    state_data_2 = {"location": "Dungeon", "description": "Dark and damp, with the faint sound of dripping water."}
    create_game_state(db_session, game_session_id=session.id, state_data=state_data_1)
    create_game_state(db_session, game_session_id=session.id, state_data=state_data_2)

    # Retrieve all GameStates for this session
    game_states = get_game_states_by_session(db_session, session.id)

    # Assertions
    assert len(game_states) == 2
    assert game_states[0].state_data["location"] == "Castle Gate"
    assert game_states[1].state_data["location"] == "Dungeon"
