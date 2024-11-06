# character_repository.py
from sqlalchemy.orm import Session
from app.models.v2.character import Character
from typing import Optional, List, Dict

def create_character(db: Session, game_session_id: int, player_id: Optional[int], character_data: Dict, type: str) -> Character:
    """
    Create a new character in the game session.

    - `game_session_id`: ID of the associated game session.
    - `player_id`: ID of the player controlling the character, or None for NPCs.
    - `character_data`: Dictionary containing the character's attributes and stats.
    - `char_type`: Type of the character ('player' or 'npc').

    Returns the created Character instance.
    """
    new_character = Character(
        game_session_id=game_session_id,
        player_id=player_id,
        character_data=character_data,
        type=type
    )
    db.add(new_character)
    db.commit()
    db.refresh(new_character)
    return new_character

def get_character_by_id(db: Session, character_id: int) -> Optional[Character]:
    """
    Retrieve a character by its ID.
    
    - `character_id`: The ID of the character to retrieve.
    
    Returns the Character instance if found, else None.
    """
    return db.query(Character).filter(Character.id == character_id).first()

def get_characters_by_session(db: Session, game_session_id: int) -> List[Character]:
    """
    Retrieve all characters in a given game session.
    
    - `game_session_id`: ID of the game session to retrieve characters for.
    
    Returns a list of Character instances associated with the session.
    """
    return db.query(Character).filter(Character.game_session_id == game_session_id).all()

def get_player_character(db: Session, player_id: int) -> Optional[Character]:
    """
    Retrieve the character controlled by a specific player.
    
    - `player_id`: ID of the player to retrieve the character for.
    
    Returns the Character instance if found, else None.
    """
    return db.query(Character).filter(Character.player_id == player_id).first()
