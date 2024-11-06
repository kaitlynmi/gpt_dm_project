# backend/app/models/glm/glm_air.py

from app.models.v1.glm.glm_base import GLMBase

class GLM4AirModel(GLMBase):
    def execute_task(self, payload: dict) -> dict:
        """
        Mock AI response for context summarization.
        """
        return {
            "summary": f"Mock summary for context: {payload.get('context')}"
        }
