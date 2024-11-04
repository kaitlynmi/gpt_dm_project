from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import openai
from app.api.v1.endpoints import game, character # Adjusted import path
from app.db.session import engine      # Adjusted import path
from app.db.base import Base            # Adjusted import path

# 

Base.metadata.create_all(bind=engine)

app = FastAPI()



# Configure CORS to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Update with your frontend origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(game.router, prefix="/api/v1/game")
app.include_router(character.router, prefix="/api/v1", tags=["character"])
print([route.path for route in app.routes])

@app.get("/")
def read_root():
    return {"message": "GPT-DM Backend is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
