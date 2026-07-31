import os

def ask_chatbot(question: str):
    api_key = os.getenv("GROQ_API_KEY")

    return {
        "question": question,
        "api_key_exists": api_key is not None,
        "api_key_length": len(api_key) if api_key else 0,
        "api_key_prefix": api_key[:8] if api_key else "NOT FOUND"
    }