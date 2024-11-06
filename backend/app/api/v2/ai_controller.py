# ai_controller.py
from fastapi import APIRouter
from pydantic import BaseModel
from app.services.v2 import ai_service_dispatcher

router = APIRouter()

class NarrativeRequest(BaseModel):
    game_id: int
    context: str  # Current game context for narrative generation

class NarrativeResponse(BaseModel):
    narrative: str

@router.post("/narrative", response_model=NarrativeResponse)
async def generate_narrative(request: NarrativeRequest):
    """
    Endpoint to generate narrative based on current game context.

    - `game_id`: ID of the game session.
    - `context`: Description of the current situation or context for AI to respond to.
    
    Returns AI-generated narrative text.
    """
    # TODO: Integrate AI model for narrative generation in ai_service_dispatcher (Phase 2)
    mock_response = {
        "narrative": "You find yourself in a dimly lit library, surrounded by ancient tomes and an eerie silence."
    }
    return mock_response
