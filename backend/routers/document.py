from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

from database import get_db
from models.document import Document

import os

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


# Upload Document
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


# List Documents
@router.get("/list")
def list_documents(
    db: Session = Depends(get_db)
):

    documents = db.query(Document).all()

    return documents


# Download Document
@router.get("/download/{document_id}")
def download_document(
    document_id: int,
    db: Session = Depends(get_db)
):

    document = db.query(Document).filter(
        Document.id == document_id
    ).first()

    if not document:
        return {
            "message": "Document not found"
        }

    return FileResponse(
        path=document.filepath,
        filename=document.filename
    )