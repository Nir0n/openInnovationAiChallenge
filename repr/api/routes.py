from fastapi import APIRouter, BackgroundTasks, Response, HTTPException, Depends
from dependencies import get_image_processing_service


router = APIRouter()

@router.get('/get_image_frames')
async def image_frames_route(depth_min: int, depth_max: int, image_processing_service=Depends(get_image_processing_service)):
    try:
        if depth_min is None or depth_max is None:
            return {"error": "depth_min and depth_max are required"}
        if depth_min > depth_max:
            return {"error": "depth_min cannot be greater than depth_max"}
        # Add logic to get image frames
        headers = {
            "Content-Disposition": f"attachment; filename=depth_{depth_min}_to_{depth_max}.png"
        }
        image_binary = image_processing_service.get_images_by_depth(depth_min=depth_min,
                                                                    depth_max=depth_max)
        if not image_binary:
            return Response(status_code=404, content="Images for this range not found")
        return Response(content=image_binary, media_type="image/png", headers=headers)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post('/start-processing/{file_name}')
async def start_processing(file_name: str, background_tasks: BackgroundTasks, image_processing_service=Depends(get_image_processing_service)):
    try:
        background_tasks.add_task(image_processing_service.initial_image_processing,
                                  file_name)
        return {"message": "Processing started in the background."}
    except Exception as e:
        return HTTPException(status_code=500, detail=str(e))
