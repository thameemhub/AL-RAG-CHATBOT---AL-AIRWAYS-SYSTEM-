import hashlib
import numpy as np

def get_embedding(text, dim=384):
    hash_bytes = hashlib.sha256(text.encode("utf-8")).digest()
    vector = np.frombuffer(hash_bytes, dtype=np.uint8).astype(float)

    if len(vector) < dim:
        vector = np.pad(vector, (0, dim - len(vector)))

    return vector.tolist()
