# tests/test_player_character.py
from app.models.v2.player import Player
from app.models.v2.character import Character

def test_create_player_with_character(db_session):
    # Arrange
    new_player = Player(name="Alice")
    new_character = Character(game_session_id=1, player=new_player, character_data={"health": 100}, type="player")

    # Act
    db_session.add(new_player)
    db_session.add(new_character)
    db_session.commit()
    db_session.refresh(new_player)
    db_session.refresh(new_character)

    # Assert
    assert new_player.id is not None
    assert new_player.name == "Alice"
    assert new_character.id is not None
    assert new_character.type == "player"
    assert new_character.character_data["health"] == 100
