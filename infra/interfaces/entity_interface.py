from abc import ABCMeta, abstractmethod


class EntityInterface(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def from_dict(cls, data: dict) -> 'EntityInterface':
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass
