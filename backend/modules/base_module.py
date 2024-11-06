from abc import ABC, abstractmethod

class BaseModule(ABC):
    @abstractmethod
    def load_module(self):
        """Load module-specific data like NPCs, settings, and initial story state."""
        pass

    @abstractmethod
    def advance_story(self, action: str, context: dict):
        """Progress the story based on player action and current context."""
        pass

    @abstractmethod
    def get_current_narrative(self) -> str:
        """Get the current narrative to be presented to the player."""
        pass

    @abstractmethod
    def get_npc_details(self, npc_id: str) -> dict:
        """Retrieve specific NPC information."""
        pass

    @abstractmethod
    def get_location_info(self, location_id: str) -> dict:
        """Retrieve details for a particular setting or location."""
        pass
