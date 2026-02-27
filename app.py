from flask import Flask, render_template
import requests

app = Flask(__name__)

API_KEY = "5b0ee952692119c125f2635341c691cc"   # your GNews API key
BASE_URL = "https://gnews.io/api/v4/top-headlines"

def get_news():
    params = {
        "country": "in",
        "lang": "en",
        "max": 10,
        "apikey": API_KEY
    }

    response = requests.get(BASE_URL, params=params)
    data = response.json()

    print("API RESPONSE:", data)   # debug (important)

    news_list = []
    for article in data.get("articles", []):
        news_list.append({
            "title": article.get("title", "No title"),
            "description": article.get("description", "No description available"),
            "url": article.get("url")
        })

    return news_list

@app.route("/")
def home():
    news = get_news()
    return render_template("index.html", news=news)

if __name__ == "__main__":
    app.run(debug=True)
