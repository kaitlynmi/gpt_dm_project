# backend/app/models/glm/glm_base.py

from abc import ABC, abstractmethod

class GLMBase(ABC):
    """
    Abstract base class for GLM models, ensuring consistent method signatures across models.
    """
    @abstractmethod
    def execute_task(self, payload: dict) -> dict:
        """
        Executes a task based on the input payload.
        """
        pass
