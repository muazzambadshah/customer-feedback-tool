from textblob import TextBlob

print("Customer Feedback Sentiment Analyzer")
print("-----------------------------------")

feedback = input("Enter customer feedback: ")

analysis = TextBlob(feedback)

score = analysis.sentiment.polarity

if score > 0:
    sentiment = "Positive"

elif score < 0:
    sentiment = "Negative"

else:
    sentiment = "Neutral"

print("\nSentiment:", sentiment)
print("Polarity Score:", round(score, 2))