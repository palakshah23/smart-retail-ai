from transformers import pipeline

sentiment_pipeline = None


def analyze_sentiment(review: str):
    global sentiment_pipeline

    if sentiment_pipeline is None:
        sentiment_pipeline = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english"
        )

    result = sentiment_pipeline(review)[0]

    return {
        "review": review,
        "sentiment": result["label"],
        "confidence": round(result["score"], 4)
    }