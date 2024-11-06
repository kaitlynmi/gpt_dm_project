# tests/test_repositories/test_character_repository.py
import pytest
from sqlalchemy.orm import Session
from app.models.v2.character import Character
from app.repositories.character_repository import (
    create_character,
    get_character_by_id,
    get_characters_by_session,
    get_player_character
)

def test_create_character(db_session: Session):
    character_data = {"health": 100, "strength": 10}
    character = create_character(db_session, game_session_id=1, player_id=1, character_data=character_data, type="player")
    assert character.id is not None
    assert character.game_session_id == 1
    assert character.player_id == 1
    assert character.character_data == character_data
    assert character.type == "player"

def test_get_character_by_id(db_session: Session):
    character_data = {"health": 100, "strength": 10}
    character = create_character(db_session, game_session_id=1, player_id=1, character_data=character_data, type="player")
    retrieved_character = get_character_by_id(db_session, character.id)
    assert retrieved_character is not None
    assert retrieved_character.id == character.id
    assert retrieved_character.character_data == character_data

def test_get_characters_by_session(db_session: Session):
    character_data_1 = {"health": 100, "strength": 10}
    character_data_2 = {"health": 80, "intelligence": 15}
    create_character(db_session, game_session_id=1, player_id=1, character_data=character_data_1, type="player")
    create_character(db_session, game_session_id=1, player_id=None, character_data=character_data_2, type="npc")
    characters = get_characters_by_session(db_session, game_session_id=1)
    assert len(characters) == 2

def test_get_player_character(db_session: Session):
    character_data = {"health": 100, "strength": 10}
    character = create_character(db_session, game_session_id=1, player_id=1, character_data=character_data, type="player")
    retrieved_character = get_player_character(db_session, player_id=1)
    assert retrieved_character is not None
    assert retrieved_character.id == character.id
    assert retrieved_character.player_id == 1
