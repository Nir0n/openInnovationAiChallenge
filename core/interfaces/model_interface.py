from abc import ABC, abstractmethod


class ModelInterface(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        pass

    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> 'ModelInterface':
        pass
