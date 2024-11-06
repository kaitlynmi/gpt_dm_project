from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.v1.game_service import GameService

router = APIRouter()

class StartGameRequest(BaseModel):
    character_id: int
    language: str = "Chinese"
    llm_provider: str = "zhipu_glm"
    game_config: dict = None

@router.post("/game/start")
async def start_game(request: StartGameRequest):
    """
    Starts a new game session using mock AI responses.
    """
    try:
        result = await GameService.start_game(request.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/roll_dice")
async def roll_dice(sides: int = 20):
    import random
    if sides < 2:
        raise HTTPException(status_code=400, detail="Dice must have at least 2 sides.")
    return {"result": random.randint(1, sides)}

class ActionRequest(BaseModel):
    action: str
    context: dict  # Additional context for the AI model

@router.post("/game/{session_id}/action")
async def perform_action(session_id: str, request: ActionRequest):
    """
    Processes a player's action by routing the task to the AI models.

    TODO: Integrate with the AIServiceDispatcher in Sprint 2.
    """
    try:
        # Process action using GameService (which calls AIServiceDispatcher)
        result = await GameService.process_action(session_id, request.dict())
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))