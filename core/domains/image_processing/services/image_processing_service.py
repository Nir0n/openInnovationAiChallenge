import pandas as pd
import numpy as np
import os
from scipy.ndimage import zoom
import asyncio
from concurrent.futures import ThreadPoolExecutor
from logging import Logger
from config import STATIC_DATA_DIR, PROJECT_ROOT_PATH
from ..models.image import Image
from infra import DatabaseInterface


class ImageProcessingService:
    def __init__(self, logger: Logger, db_service: DatabaseInterface):
        self.logger = logger
        self.db_service = db_service


    async def initial_image_processing(self, file_name: str) -> int:
        self.logger.info(f"Start initial image processing for file {file_name}")
        file_name = os.path.join(PROJECT_ROOT_PATH, STATIC_DATA_DIR, file_name)
        if not os.path.exists(file_name):
            self.logger.warning(file_name + " doesn't exist")
            return -1

        loop = asyncio.get_event_loop()
        with open(file_name, 'r') as file:
            with ThreadPoolExecutor() as pool:
                tasks = []
                for line in file:
                    task = loop.run_in_executor(pool, self.process_image, line)
                    tasks.append(task)
        res = await asyncio.gather(*tasks)
        if -1 in set(res):
            self.logger.error("Errors were encountered during image processing stage")
        else:
            self.logger.info("Image processing succeeded")

 
    def process_image(self, row) -> int:
        try:
            row_elements = row.split(',')
            depth = float(row_elements[0])
            image_data = np.array(row_elements[1:], dtype=np.uint8)
            resized_image = self.resize_1d_image(image_data, 150)
            image = Image(depth, resized_image)
            self.db_service.save(image)
            return 0
        except Exception as e:
            self.logger.error(f"error: {e} occurred while processing row: {row}")
            return -1


    def resize_1d_image(self, image_array, target_size):
        """
        Resizes a 1D image array using interpolation.

        :param image_array: The original 1D image array.
        :param target_size: The desired size of the resized image.
        :return: Resized image array.
        """
        # Convert the 1D array into a 2D array with one row
        image_2d = image_array.reshape((1, -1))

        zoom_factor = target_size / image_2d.shape[1]

        resized_image = zoom(image_2d, (1, zoom_factor))

        # Flatten the 2D array back into 1D
        return resized_image.flatten()
    
    
