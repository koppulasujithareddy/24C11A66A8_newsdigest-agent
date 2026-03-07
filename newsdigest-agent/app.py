from flask import Flask, render_template, request
from news_fetcher import fetch_news
from summarizer import summarize_article
from sentiment import analyze_sentiment

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    results = {}

    if request.method == "POST":

        topics = request.form["topics"].split(",")

        for topic in topics:

            topic = topic.strip()

            articles = fetch_news(topic)

            processed = []

            for article in articles:

                summary = summarize_article(article["content"])

                sentiment = analyze_sentiment(summary)

                processed.append({
                    "title": article["title"],
                    "summary": summary,
                    "sentiment": sentiment
                })

            results[topic] = processed

    return render_template("index.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)