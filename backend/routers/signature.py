from fastapi import APIRouter, UploadFile, File
import os

router = APIRouter()

SIGNATURE_DIR = "signatures"

os.makedirs(SIGNATURE_DIR, exist_ok=True)

@router.post("/upload")
async def upload_signature(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        SIGNATURE_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    return {
        "message": "Signature uploaded successfully",
        "filename": file.filename
    }