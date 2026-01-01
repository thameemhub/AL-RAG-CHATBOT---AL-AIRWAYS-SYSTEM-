from flask import Flask, request, jsonify
from flask_cors import CORS
from vector_store import load_store
from answer_generator import generate_answer
from metrics import metrics
import numpy as np

app = Flask(__name__)
CORS(app)   # ✅ FIXES FRONTEND FETCH ERROR

vectorizer, X, chunks = load_store()

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "query" not in data:
        return jsonify({"answer": "⚠️ Invalid request"}), 400

    q = data["query"]
    start = metrics.start()

    vec = vectorizer.transform([q])
    scores = np.dot(X, vec.T).toarray().flatten()
    top = scores.argsort()[-3:][::-1]
    retrieved = [chunks[i] for i in top]

    answer = generate_answer(q, retrieved)

    metrics.end(start)
    return jsonify({"answer": answer})

@app.route("/metrics")
def get_metrics():
    return jsonify(metrics.stats())

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
