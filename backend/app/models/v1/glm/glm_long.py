# backend/app/models/glm/glm_long.py

from app.models.v1.glm.glm_base import GLMBase

class GLM4LongModel(GLMBase):
    def execute_task(self, payload: dict) -> dict:
        """
        Mock AI response for narrative generation.
        """
        return {
            "narrative": f"Mock narrative generated for action: {payload.get('action')}"
        }
