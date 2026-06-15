from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse

from database import get_db
from models.document import Document
from models.signature import Signature
from services.pdf_service import sign_pdf

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


# Sign Document
@router.post("/sign")
def sign_document(
    document_id: int,
    signature_id: int,
    db: Session = Depends(get_db)
):

    document = db.query(Document).filter(
        Document.id == document_id
    ).first()

    signature = db.query(Signature).filter(
        Signature.id == signature_id
    ).first()

    if not document:
        return {
            "message": "Document not found"
        }

    if not signature:
        return {
            "message": "Signature not found"
        }

    output_path = f"uploads/signed_{document.filename}"

    sign_pdf(
        document.filepath,
        signature.filepath,
        output_path
    )

    return {
        "message": "PDF signed successfully",
        "signed_file": output_path
    }


# Delete Document
@router.delete("/delete/{document_id}")
def delete_document(
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

    if os.path.exists(document.filepath):
        os.remove(document.filepath)

    db.delete(document)
    db.commit()

    return {
        "message": "Document deleted successfully"
    }