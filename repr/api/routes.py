from fastapi import APIRouter, Depends
from core.domains.image_processing import ImageProcessingService
# TODO start using
router = APIRouter()

# Dependency injection for ImageProcessingService
def get_image_processing_service(service: ImageProcessingService = Depends()):
    return service


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


@router.post('/start-processing/{file_path}')
async def start_processing(file_path: str, image_processing_service: ImageProcessingService = Depends(get_image_processing_service)):
    try:
        await image_processing_service.initial_image_processing(file_path)
        return {"message": "Processing started in the background."}
    except Exception as e:
        return {"error": str(e)}
