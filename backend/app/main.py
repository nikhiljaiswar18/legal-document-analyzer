from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Legal Document Analyzer Backend Running"}