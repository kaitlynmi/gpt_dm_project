# gpt_service.py

import openai

class GPTService:
    
    def __init__(self, api_key: str):
        openai.api_key = api_key

    async def validate_action(self, action: str, game_state: dict):
        """
        Validate if a player's action is allowed by the game mechanics and context.
        """
        prompt = [
            {"role": "system", "content": "You are a dnd Dungeon Master."},
            {"role": "user", "content": f"Player wants to '{action}'. Is this action valid given the game state: {game_state} and game rules? Yes or no?"}
        ]
        response = await openai.ChatCompletion.create(
            model="gpt-4",
            messages=prompt,
            functions=[
                {"name": "validate_action", "description": "Validate if action is possible"}
            ]
        )
        return response['choices'][0]['message']['content']

    async def request_roll(self, action: str, game_state: dict):
        """
        Ask the backend to calculate a dice roll based on action.
        """
        prompt = [
            {"role": "system", "content": "You are a Dungeon Master."},
            {"role": "user", "content": f"Player attempts '{action}'. What type of roll is required?"}
        ]
        response = await openai.ChatCompletion.create(
            model="gpt-4",
            messages=prompt,
            functions=[
                {"name": "roll_dice", "description": "Request dice roll for action"}
            ]
        )
        roll_type = response['choices'][0]['message']['content']
        # Assuming your backend has a dice roll method you can call:
        roll_result = await self.backend_roll_dice(roll_type)
        return roll_result

    async def generate_narrative(self, action: str, roll_result: dict, game_state: dict):
        """
        Generate narrative based on the action and the dice roll outcome.
        """
        prompt = [
            {"role": "system", "content": "You are a Dungeon Master."},
            {"role": "user", "content": f"Player attempted to '{action}'. The roll result was {roll_result}. Narrate the outcome."}
        ]
        response = await openai.ChatCompletion.create(
            model="gpt-4",
            messages=prompt
        )
        return response['choices'][0]['message']['content']
