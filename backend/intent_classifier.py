def detect_intent(q):
    q = q.lower().strip()

    if any(x in q for x in ["hi", "hello", "hey", "good morning", "good evening"]):
        return "greeting"

    if any(x in q for x in ["food", "meal", "catering"]):
        return "food"

    if any(x in q for x in ["logistics", "transport", "hotel", "pickup"]):
        return "logistics"

    return "policy"
