from infra import RepositoryInterface


class ImageRepository(RepositoryInterface):
    def save(self, image_entity):
        # Implement adding an image entity to the database
        pass

    def delete(self, image_id):
        # Implement removing an image entity from the database
        pass

    def get_by_id(self, image_id):
        # Implement retrieving an image entity by ID
        pass

    def get_all(self):
        # Implement retrieving all image entities
        pass