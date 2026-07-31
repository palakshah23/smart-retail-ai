import os
from groq import Groq

def ask_chatbot(question: str):
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return {
            "answer": response.choices[0].message.content
        }

    except Exception as e:
        return {
            "error_type": type(e).__name__,
            "error": str(e)
        }