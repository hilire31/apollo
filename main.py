from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import fitz  # PyMuPDF pour lire le PDF
import os

from pydantic import BaseModel

app = FastAPI()

# Configuration CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Autoriser ton frontend Angular
    allow_credentials=True,
    allow_methods=["*"],  # Autoriser toutes les méthodes HTTP
    allow_headers=["*"],  # Autoriser tous les en-têtes
)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    """Enregistre le PDF et extrait le texte"""
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    # Extraction de texte
    doc = fitz.open(file_path)
    text = "\n".join([page.get_text() for page in doc])

    return {"filename": file.filename, "text": text[:500]}  # Renvoie un extrait du texte

class TextRequest(BaseModel):
    text: str  # Définir la structure de la requête



@app.post("/process/")
async def process_text(request: TextRequest):
    """Exécute un traitement sur le texte"""
    processed_text = "ETXT"  # Exemple : mise en majuscules
    return {"processed_text": processed_text}
