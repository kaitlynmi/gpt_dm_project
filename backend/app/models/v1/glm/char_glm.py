# backend/app/models/glm/char_glm.py

from app.models.v1.glm.glm_base import GLMBase

class CharGLM3Model(GLMBase):
    def execute_task(self, payload: dict) -> dict:
        """
        Mock AI response for character interactions.
        """
        return {
            "dialogue": f"Mock character response for input: {payload.get('input')}"
        }
