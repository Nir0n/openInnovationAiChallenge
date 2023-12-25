from abc import ABC, abstractmethod


class DatabaseInterface(ABC):

    @abstractmethod
    def save(self, entity):
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
