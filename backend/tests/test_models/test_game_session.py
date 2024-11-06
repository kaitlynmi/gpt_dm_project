# tests/test_models/test_game_session.py
from app.models.v2.game_session import GameSession
from app.models.v2.player import Player
from app.models.v2.character import Character
from app.models.v2.game_state import GameState
from app.models.v2.module import Module

def test_game_session_creation(db_session):
    module = Module(name="Test Module", module_data={})
    db_session.add(module)
    db_session.commit()

    # Create a GameSession
    session = GameSession(language="English", llm_provider="Zhipu GLM", module_id=module.id)
    db_session.add(session)
    db_session.commit()

    # Create a Player and associate it with the GameSession
    player = Player(name="Test Player", game_session_id=session.id)
    db_session.add(player)
    db_session.commit()

    # Create a Character and associate it with both the GameSession and Player
    character = Character(game_session_id=session.id, player_id=player.id, character_data={}, type="player")
    db_session.add(character)
    db_session.commit()

    # Explicitly set relationships to ensure proper linking
    player.character = character
    db_session.add(player)
    db_session.commit()

    # Check that all objects are created and linked correctly
    assert session.language == "English"
    assert player.game_session_id == session.id
    assert character.player_id == player.id
    assert session.players[0].name == "Test Player"
    assert session.module_id == module.id