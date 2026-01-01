from transformers import pipeline
from intent_classifier import detect_intent
from metrics import metrics

# Load Hugging Face model once
llm = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",
    max_length=256
)


def build_prompt(query, context):
    return f"""
You are AL Bot, a polite and professional airline assistant for AL Airways.

Answer the question ONLY using the information provided below.
Summarize clearly.
Use a friendly airline tone with emojis.

Context:
{context}

Question:
{query}

Answer:
"""


def generate_answer(query, chunks):
    metrics.requests += 1
    intent = detect_intent(query)

    # ===== GREETING =====
    if intent == "greeting":
        return (
            "👋 **Hello from AL Airways!** ✈️\n\n"
            "This is **AL Bot**, your virtual assistant. "
            "I’m here to help you with flights, baggage, food, refunds, and travel assistance.\n\n"
            "How may I assist you today?"
        )

    # ===== FOOD =====
    if intent == "food":
        return (
            "🍽️ **Food & Catering at AL Airways**\n\n"
            "• Complimentary meals or snacks depending on route\n"
            "• Special meals (vegetarian, halal, diabetic) available on request\n"
            "• Baby food permitted onboard\n\n"
            "😊 Let me know if you need help with meal options."
        )

    # ===== LOGISTICS =====
    if intent == "logistics":
        return (
            "🚍 **Logistics & Ground Support**\n\n"
            "• Airport ground assistance\n"
            "• Hotel accommodation for overnight disruptions (if applicable)\n"
            "• Transport between airport and hotel\n\n"
            "🙂 Tell me your situation and I’ll guide you."
        )

    # ===== COST =====
    if intent == "cost":
        return (
            "💰 **Ticket Cost & Fare Information**\n\n"
            "Ticket prices depend on:\n"
            "• Route and destination\n"
            "• Travel date and demand\n"
            "• Fare type and booking time\n\n"
            "✈️ For exact pricing, please check the official AL Airways booking portal.\n\n"
            "🙂 I can help explain fare rules or refund conditions."
        )

    # ===== POLICY (LLM-POWERED RAG) =====
    if not chunks:
        metrics.fallbacks += 1
        return (
            "⚠️ I couldn’t find the relevant policy information right now.\n"
            "Please contact AL Airways customer support for assistance."
        )

    # Combine top chunks as context
    context = "\n".join(chunk["text"] for chunk in chunks[:2])

    prompt = build_prompt(query, context)

    response = llm(prompt)[0]["generated_text"]

    return response.strip()
