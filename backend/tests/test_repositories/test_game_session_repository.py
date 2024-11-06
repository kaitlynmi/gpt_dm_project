# tests/test_repositories/test_game_session_repository.py
from app.repositories.game_session_repository import create_game_session
from app.repositories.player_repository import create_player
from app.repositories.character_repository import create_character

def test_create_game_session(db_session):
    session = create_game_session(db_session, language="English", llm_provider="Zhipu GLM", module="Test Module")
    assert session.language == "English"
    assert session.llm_provider == "Zhipu GLM"

    player = create_player(db_session, name="Test Player", game_session_id=session.id)
    character = create_character(db_session, game_session_id=session.id, player_id=player.id, character_data={}, type="player")

    assert player.game_session_id == session.id
    assert character.player_id == player.id
