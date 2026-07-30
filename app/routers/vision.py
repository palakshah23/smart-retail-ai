from fastapi import APIRouter, UploadFile, File
from app.services.vision_service import detect_faces

router = APIRouter(
    prefix="/vision",
    tags=["Vision"]
)


@router.post("/detect-face")
async def detect_face(file: UploadFile = File(...)):
    return await detect_faces(file)