from abc import ABC, abstractmethod


class RepositoryInterface(ABC):
    def __init__(self, database_session):
        self.database_session = database_session

    @abstractmethod
    def save(self, entity):
        pass

    @abstractmethod
    def delete(self, entity_id):
        pass

    @abstractmethod
    def get_by_id(self, entity_id):
        pass

    @abstractmethod
    def get_all(self):
        pass