from fastapi import FastAPI, UploadFile, File
import shutil
import os

from backend.app.utils import extract_text_from_pdf

app = FastAPI()

UPLOAD_FOLDER = "uploads"

@app.get("/")
def home():
    return {"message": "Legal Document Analyzer Backend Running"}


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from PDF
    text = extract_text_from_pdf(file_path)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename,
        "text_preview": text[:500]
    }