import os
from PyPDF2 import PdfReader
from typing import List

def load_txt_file(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def load_pdf_file(filepath: str) -> str:
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

def load_documents(directory: str) -> str:
    all_text = ""
    for filename in os.listdir(directory):
        path = os.path.join(directory, filename)
        if filename.endswith(".txt"):
            all_text += load_txt_file(path)
        elif filename.endswith(".pdf"):
            all_text += load_pdf_file(path)
    return all_text

def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> List[str]:
    chunks = []
    start = 0
    while start < len(text):
        chunks.append(text[start:start+chunk_size].strip())
        start += chunk_size - overlap
    return chunks

def ingest_data(data_path: str) -> List[str]:
    full_text = load_documents(data_path)
    return chunk_text(full_text)
