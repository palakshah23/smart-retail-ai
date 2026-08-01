import os
import traceback

import httpx
from groq import Groq


def ask_chatbot(question: str):
    try:
        api_key = os.getenv("GROQ_API_KEY", "").strip()

        # TEMPORARY DEBUG
        print(repr(api_key))

        client = Groq(
            api_key=api_key,
            http_client=httpx.Client(timeout=60)
        )

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
            "error": str(e),
            "traceback": traceback.format_exc()
        }