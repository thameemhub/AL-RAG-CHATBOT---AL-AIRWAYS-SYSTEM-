def chunk_texts(documents, chunk_size=500, overlap=50):
    chunks = []

    for doc in documents:
        text = doc["text"]
        source = doc["source"]

        start = 0
        while start < len(text):
            end = start + chunk_size
            chunk = text[start:end]

            chunks.append({
                "text": chunk,
                "source": source
            })

            start += chunk_size - overlap

    return chunks
