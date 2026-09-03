from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse # <-- 1. ADD THIS IMPORT
from fastapi.middleware.cors import CORSMiddleware
from pypdf import PdfReader
from typing import Optional
from groq import Groq
import os
import json
from dotenv import load_dotenv

# Load your GROQ_API_KEY from the .env file
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.post("/api/generate-notes")
async def generate_notes(
    file: Optional[UploadFile] = File(None),
    pasted_text: Optional[str] = Form(None) 
):
    # ... (Keep all your existing Groq API code here exactly the same) ...
    if not file and not pasted_text:
        raise HTTPException(status_code=400, detail="Please provide either a PDF file or pasted text.")

    extracted_text = ""

    if file:
        try:
            pdf_reader = PdfReader(file.file)
            for page in pdf_reader.pages:
                extracted_text += page.extract_text()
        except Exception as e:
            raise HTTPException(status_code=400, detail="Could not read the PDF file.")
    else:
        extracted_text = pasted_text
        
    extracted_text = extracted_text[:25000]  # Limit to first 25,000 characters to avoid overwhelming the model

    prompt = f"""
    Read the following text and return a JSON object with two keys:
    1. "summary": A well-formatted HTML string summarizing the main points (use <h3>, <p>, <ul> tags).
    2. "flashcards": An array of objects, each with a "q" (question) and "a" (answer) key.
    
    Return ONLY valid JSON.
    
    Text: {extracted_text}
    """

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.3-70b-versatile", # <-- THIS IS THE ONLY LINE YOU CHANGE
        response_format={"type": "json_object"}, 
    )

    return json.loads(response.choices[0].message.content)

@app.get("/")
async def serve_frontend():
    # This finds exactly where your index.html file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(current_dir)
    html_path = os.path.join(project_root, "frontend", "index.html")
    
    return FileResponse(html_path)