# backend/app/models/glm/glm_plus.py
from app.core.config import config
from app.models.v1.glm.glm_base import GLMBase

class GLM4PlusModel(GLMBase):
    def execute_task(self, payload: dict) -> dict:
        """
        Mock AI response for rule enforcement.
        """
        
        return {
            "validation": True,
            "roll_request": {
                "name": "Athletics",
                "dice": "d20",
                "dc": 15,
                "modifiers": [{"name": "strength", "value": 2}]
            }
        }
        
    def get_api_key():
        return config.ZHIPU_GLM_API_KEY
