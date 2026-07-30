import os
from dotenv import load_dotenv
from groq import Groq

# Load .env only once
load_dotenv()


def ask_chatbot(question: str):
    # Create the client only when this function is called
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY")
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful AI assistant for a smart retail store. "
                    "Answer customer shopping questions politely and briefly."
                )
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )

    return {
        "question": question,
        "answer": response.choices[0].message.content
    }