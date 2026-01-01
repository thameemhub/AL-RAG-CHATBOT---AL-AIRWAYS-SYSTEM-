import os
from pypdf import PdfReader

def load_pdfs(folder):
    documents = []

    if not os.path.exists(folder):
        raise FileNotFoundError(f"Data folder not found: {folder}")

    for file in os.listdir(folder):
        if file.endswith(".pdf"):
            path = os.path.join(folder, file)
            reader = PdfReader(path)

            text = ""
            for page in reader.pages:
                text += page.extract_text() or ""

            documents.append({
                "source": file,
                "text": text
            })

    return documents
