from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import Base, engine

# Import models so tables are created
from models.user import User
from models.document import Document
from models.signature import Signature

# Import routers
from routers.auth import router as auth_router
from routers.document import router as document_router
from routers.signature import router as signature_router

app = FastAPI(
    title="Document Signature API"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(
    auth_router,
    prefix="/api/auth",
    tags=["Authentication"]
)

app.include_router(
    document_router,
    prefix="/api/document",
    tags=["Documents"]
)

app.include_router(
    signature_router,
    prefix="/api/signature",
    tags=["Signatures"]
)

@app.get("/")
def home():
    return {
        "message": "Document Signature API Running Successfully"
    }