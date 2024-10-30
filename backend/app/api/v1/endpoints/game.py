from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/roll_dice")
async def roll_dice(sides: int = 20):
    import random
    if sides < 2:
        raise HTTPException(status_code=400, detail="Dice must have at least 2 sides.")
    return {"result": random.randint(1, sides)}
