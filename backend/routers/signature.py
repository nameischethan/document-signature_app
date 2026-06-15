from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.signature import Signature

import os

router = APIRouter()

SIGNATURE_DIR = "signatures"

os.makedirs(SIGNATURE_DIR, exist_ok=True)


@router.post("/upload")
async def upload_signature(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_path = os.path.join(
        SIGNATURE_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    signature = Signature(
        filename=file.filename,
        filepath=file_path
    )

    db.add(signature)
    db.commit()
    db.refresh(signature)

    return {
        "message": "Signature uploaded successfully",
        "id": signature.id,
        "filename": signature.filename
    }
@router.get("/list")
def list_signatures(
    db: Session = Depends(get_db)
):

    signatures = db.query(Signature).all()

    return signatures