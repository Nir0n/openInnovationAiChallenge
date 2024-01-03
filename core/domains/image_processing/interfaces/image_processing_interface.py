from abc import ABC, abstractmethod


class ImageProcessingInterface(ABC):

    @abstractmethod
    def get_images_by_depth(self, depth_min: int, depth_max: int):
        pass

    @abstractmethod
    def initial_image_processing(self, file_name: str):
        pass
