import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer

STORE_PATH = "vector_store.pkl"


def save_store(chunks):
    """
    Create vector embeddings and save them locally
    """
    texts = [chunk["text"] for chunk in chunks]

    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(texts)

    with open(STORE_PATH, "wb") as f:
        pickle.dump((vectorizer, X, chunks), f)


def load_store():
    """
    Load vector embeddings from disk
    """
    if not os.path.exists(STORE_PATH):
        raise FileNotFoundError("Vector store not found. Please run ingest.py first.")

    with open(STORE_PATH, "rb") as f:
        return pickle.load(f)
