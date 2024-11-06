# tests/test_services/test_game_service.py
from app.services.v2.game_session_service import create_game_session

def test_create_game_session_service(db_session):
    session = create_game_session(db_session, language="English", llm_provider="Zhipu GLM", module_id=1)
    assert session.language == "English"
    assert session.llm_provider == "Zhipu GLM"
    assert session.module_id == 1
