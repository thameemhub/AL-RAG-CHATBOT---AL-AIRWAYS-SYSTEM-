from pdf_loader import load_pdfs
from chunker import chunk_texts
from vector_store import save_store

DATA_PATH = "../data"

if __name__ == "__main__":
    print("📄 Loading PDFs...")
    documents = load_pdfs(DATA_PATH)

    print("✂️ Chunking documents...")
    chunks = chunk_texts(documents)

    print("💾 Saving vector store...")
    save_store(chunks)

    print("✅ All PDFs processed and vector store created")
