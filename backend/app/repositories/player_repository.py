# repositories/player_repository.py
from sqlalchemy.orm import Session
from app.models.v2.player import Player

def create_player(db: Session, name: str, game_session_id: int):
    new_player = Player(name=name, game_session_id=game_session_id)
    db.add(new_player)
    db.commit()
    db.refresh(new_player)
    return new_player
