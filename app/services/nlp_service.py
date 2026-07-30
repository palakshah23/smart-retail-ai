from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(review: str):

    scores = analyzer.polarity_scores(review)

    compound = scores["compound"]

    if compound >= 0:
        sentiment = "POSITIVE"
    else:
        sentiment = "NEGATIVE"

    confidence = abs(compound)

    return {
        "review": review,
        "sentiment": sentiment,
        "confidence": round(confidence, 4)
    }