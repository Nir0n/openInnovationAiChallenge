from fastapi import FastAPI, APIRouter, BackgroundTasks
import uvicorn
from core.domains.image_processing import ImageProcessingService
from infra import SqlDatabaseService
from config import configure_logger
from alembic.config import Config
from alembic import command
from core.domains.image_processing import ImageModel
from infra import ImageEntity

app = FastAPI()
# TODO rework main

def upgrade_database():
    alembic_cfg = Config("infra/databases/sql/alembic.ini")
    command.upgrade(alembic_cfg, "head")


model_to_entity_mapping = {
    ImageModel: ImageEntity,
}
db_service = SqlDatabaseService(logger=configure_logger("sql_database_logger"),
                                db_url='postgresql+psycopg2://pguser:pgpassword@db:5432/pgdatabase',
                                model_to_entity_mapping=model_to_entity_mapping)
image_processing_service = ImageProcessingService(configure_logger("image_processing_logger"),
                                                  db_service)
app.image_processing_service = image_processing_service
upgrade_database()

# --------------- router # TODO move to separate file after establish dependencies
router = APIRouter()


@router.get('/get_image_frames')
async def image_frames_route(depth_min: int = None, depth_max: int = None):
    try:
        if depth_min is None or depth_max is None:
            return {"error": "depth_min and depth_max are required"}
        if depth_min > depth_max:
            return {"error": "depth_min cannot be greater than depth_max"}
        # Add logic to get image frames
        return {"result": "Image frames"}
    except Exception as e:
        return {"error": str(e)}


@router.post('/start-processing/{file_name}')
async def start_processing(file_name: str, background_tasks: BackgroundTasks):
    try:
        background_tasks.add_task(app.image_processing_service.initial_image_processing,
                                  file_name)
        return {"message": "Processing started in the background."}
    except Exception as e:
        return {"error": str(e)}

app.include_router(router, prefix='/api')

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)