from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session

from database import get_db
from models.document import Document

import os

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    document = Document(
        filename=file.filename,
        filepath=file_path
    )

    db.add(document)
    db.commit()
    db.refresh(document)

    return {
        "message": "File uploaded successfully",
        "id": document.id,
        "filename": document.filename
    }


@router.get("/list")
def list_documents(
    db: Session = Depends(get_db)
):

    documents = db.query(Document).all()

    return documents