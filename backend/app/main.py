from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai
from app.database import init_db, SessionLocal 
from .api.v2 import game_controller, character_controller , ai_controller

# load_dotenv()

# Base.metadata.create_all(bind=engine)
init_db()

app = FastAPI(
    title="AI Game Master",
    description="Backend for the AI Game Master project",
    version="2.0"
)


# Configure CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update with your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Past Version v1 endpoints
# app.include_router(game.router, prefix="/api/v1/game", tags=["v1/game"])
# app.include_router(character.router, prefix="/api/v1", tags=["v1/character"])

# Version in development
app.include_router(game_controller.router, prefix="/api/v2/game", tags=["game"])
app.include_router(character_controller.router, prefix="/api/v2/character", tags=["character"])
app.include_router(ai_controller.router, prefix="/api/v2/ai", tags=["ai"])

print([route.path for route in app.routes])

@app.get("/")
def read_root():
    return {"message": "Welcome to the AI Game Master API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
