# tests/test_services/test_ai_service_dispatcher.py
from app.services.v2.ai_service_dispatcher import generate_narrative

def test_generate_narrative():
    result = generate_narrative(game_id=1, context="Entering the haunted library.")
    assert "dimly lit library" in result
