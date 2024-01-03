from config import configure_logger
from infra import SqlDatabaseService
from core.domains.image_processing import ImageProcessingService, ImageProcessingInterface, ImageModel
from infra import ImageEntity

model_to_entity_mapping = {
    ImageModel: ImageEntity,
}


def get_image_processing_service() -> ImageProcessingInterface:
    db_service = SqlDatabaseService(
        logger=configure_logger("sql_database_logger"),
        db_url='postgresql+psycopg2://pguser:pgpassword@db:5432/pgdatabase',
        model_to_entity_mapping=model_to_entity_mapping
    )
    return ImageProcessingService(configure_logger("image_processing_logger"), db_service)


