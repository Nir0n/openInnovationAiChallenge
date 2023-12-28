from abc import ABC, abstractmethod
from typing import Dict, Any, List
from core.interfaces import ModelInterface


class DatabaseInterface(ABC):

    @abstractmethod
    def save(self, model: ModelInterface):
        """Save or update an entity in the database."""
        pass

    @abstractmethod
    def delete(self, entity_id):
        """Delete an entity from the database."""
        pass

    @abstractmethod
    def get_by_id(self, entity_id):
        """Retrieve an entity by its ID."""
        pass

    @abstractmethod
    def get_all(self):
        """Retrieve all entities."""
        pass

    @abstractmethod
    def filter_by(self, model:ModelInterface, criteria: Dict[str, Any]) -> List[ModelInterface]:
        """
        Retrieve entities based on filtering criteria.
        
        Args:
            criteria (Dict[str, Any]): A dictionary where keys are column names 
                                       and values are the criteria for filtering.

        Returns:
            List[Any]: A list of entities that match the criteria.
        """
        pass
