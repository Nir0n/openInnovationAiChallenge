from abc import ABC, abstractmethod


class ModelInterface(ABC):
    @abstractmethod
    def to_dict(self) -> dict:
        pass
