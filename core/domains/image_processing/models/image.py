import numpy as np
from core.interfaces.model_interface import ModelInterface


class Image(ModelInterface):
    def __init__(self, depth: float, image: np.ndarray):
        self.depth = depth
        self.image = image

    @classmethod
    def from_dict(cls, data: dict) -> ModelInterface:
        if 'depth' in data and 'image' in data and isinstance(data['image'], list):
            return cls(depth=float(data['depth']), image=np.array(data['image']))
        else:
            raise ValueError("Required data missing for image model creation")

    def to_dict(self) -> dict:
        return {'depth': self.depth, 'image': self.image}



