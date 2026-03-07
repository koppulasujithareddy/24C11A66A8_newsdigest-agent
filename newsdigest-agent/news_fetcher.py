import requests

API_KEY = "f4a484a7916ba2246e623ea88f3acd95"

def fetch_news(topic):

    url = f"https://gnews.io/api/v4/search?q={topic}&lang=en&max=5&token={API_KEY}"

    response = requests.get(url)

    data = response.json()

    articles = []

    for article in data.get("articles", []):

        articles.append({
            "title": article["title"],
            "content": article["description"]
        })

    return articles