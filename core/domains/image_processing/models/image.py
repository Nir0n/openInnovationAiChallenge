from numpy import ndarray
from core.interfaces.model_interface import ModelInterface


class Image(ModelInterface):
    def __init__(self, depth: float, image_data: ndarray):
        self.depth = depth
        self.image_data = image_data

    def to_dict(self) -> dict:
        return {'depth': self.depth, 'image_data': self.image_data}



