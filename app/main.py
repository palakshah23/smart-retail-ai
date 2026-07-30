from fastapi import FastAPI

from app.routers import vision
from app.routers import nlp
from app.routers import chatbot

app = FastAPI(title="Smart Retail AI")

app.include_router(vision.router)
app.include_router(nlp.router)
app.include_router(chatbot.router)

@app.get("/")
def home():
    return {"message": "Smart Retail AI API is running"}