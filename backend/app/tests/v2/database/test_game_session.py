# tests/test_game_session.py
from app.models.v2.game_session import GameSession

def test_create_game_session(db_session):
    # Arrange
    new_session = GameSession(language="English", llm_provider="Zhipu GLM", module_id=None)

    # Act
    db_session.add(new_session)
    db_session.commit()
    db_session.refresh(new_session)

    # Assert
    assert new_session.id is not None
    assert new_session.language == "English"
    assert new_session.llm_provider == "Zhipu GLM"
