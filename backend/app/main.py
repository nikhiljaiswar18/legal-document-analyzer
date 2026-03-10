from fastapi import FastAPI, UploadFile, File
import shutil
import os

from backend.app.utils import extract_text_from_pdf
from backend.app.chunking import split_text_into_chunks
from backend.app.vector_store import create_vector_store
from backend.app.retriever import retrieve_relevant_chunks
from backend.app.embedding import create_embeddings



app = FastAPI()

UPLOAD_FOLDER = "uploads"

# Global variables to store document data
chunks = []
vector_db = None


@app.get("/")
def home():
    return {"message": "Legal Document Analyzer Backend Running"}


@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    global chunks
    global vector_db

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    # Save uploaded file
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Extract text from PDF
    text = extract_text_from_pdf(file_path)

    # Split document into chunks
    chunks = split_text_into_chunks(text)

    # Create embeddings for chunks
    embeddings = create_embeddings(chunks)

    # Store embeddings in FAISS vector database
    vector_db = create_vector_store(embeddings)

    return {
        "message": "Document processed successfully",
        "chunks_created": len(chunks),
        "embeddings_created": len(embeddings)
    }


@app.post("/ask")
async def ask_question(question: str):

    if vector_db is None:
        return {"error": "No document uploaded yet"}

    # Retrieve relevant chunks
    relevant_chunks = retrieve_relevant_chunks(question, vector_db, chunks)

    return {
        "question": question,
        "relevant_chunks": relevant_chunks
    }