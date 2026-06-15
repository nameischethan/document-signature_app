# Document Signature App

A FastAPI-based application that allows users to upload PDF documents, upload signature images, and digitally sign PDF files.

## Features

* User Registration
* User Login with JWT Authentication
* Upload PDF Documents
* Upload Signature Images
* Store Document Metadata in SQLite Database
* List Uploaded Documents
* Digitally Sign PDF Documents
* Generate Signed PDF Files
* Download Documents

## Tech Stack

* Python
* FastAPI
* SQLAlchemy
* SQLite
* JWT Authentication
* PyMuPDF
* Pydantic

## Project Structure

backend/
├── models/
├── routers/
├── schemas/
├── services/
├── signatures/
├── uploads/
├── utils/
├── database.py
├── main.py
├── requirements.txt
└── signature.db

## API Endpoints

### Authentication

POST /api/auth/register

POST /api/auth/login

### Documents

POST /api/document/upload

GET /api/document/list

GET /api/document/download/{document_id}

POST /api/document/sign

DELETE /api/document/delete/{document_id}

### Signatures

POST /api/signature/upload

GET /api/signature/list

## How It Works

1. Register a user account.
2. Login using JWT Authentication.
3. Upload a PDF document.
4. Upload a signature image.
5. Select document ID and signature ID.
6. Generate a signed PDF.
7. Download the signed document.

## Installation

Install dependencies:

pip install -r requirements.txt

Run the server:

uvicorn main:app --reload

Open Swagger UI:

http://127.0.0.1:8000/docs

## Sample Workflow

* Upload test.pdf
* Upload signature.png
* Execute /api/document/sign
* Generate signed_test.pdf

## Future Improvements

* Signature placement selection
* Multiple signatures in a document
* Email notifications
* Cloud storage integration
* Frontend using React or Next.js

## Author

Chethan Sai Urumu

Built as a backend project using FastAPI and Python.
