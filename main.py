from fastapi import FastAPI
import uvicorn
from repr.api.routes import router

# Albemic configs
from alembic.config import Config
from alembic import command

app = FastAPI()


def upgrade_database():
    alembic_cfg = Config("infra/databases/sql/alembic.ini")
    command.upgrade(alembic_cfg, "head")

# def get_image_processing_service(app):
#     return app.image_processing_service
#
#
#
# db_service = SqlDatabaseService(logger=configure_logger("sql_database_logger"),
#                                 db_url='postgresql+psycopg2://pguser:pgpassword@db:5432/pgdatabase',
#                                 model_to_entity_mapping=model_to_entity_mapping)
# image_processing_service = ImageProcessingService(configure_logger("image_processing_logger"),
#                                                   db_service)
# app.image_processing_service = image_processing_service
upgrade_database()
app.include_router(router, prefix='/api')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
