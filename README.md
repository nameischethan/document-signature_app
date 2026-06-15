# Document Signature App

## Features

- User Registration
- User Login with JWT Authentication
- Upload Documents
- Store Document Metadata in SQLite
- List Uploaded Documents

## Tech Stack

- FastAPI
- SQLAlchemy
- SQLite
- JWT Authentication
- Python

## API Endpoints

### Authentication

POST /api/auth/register

POST /api/auth/login

### Documents

POST /api/document/upload

GET /api/document/list

## Run Project

pip install -r requirements.txt

uvicorn main:app --reload