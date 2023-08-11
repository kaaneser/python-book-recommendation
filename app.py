import requests
import random
from flask import Flask, render_template, request

app = Flask(__name__)

API_BASE_URL = "https://www.googleapis.com/books/v1/volumes"
MAX_RESULTS = 25

def get_books(query):
    params = {
        "q": query,
        "maxResults": MAX_RESULTS
    }
    response = requests.get(API_BASE_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        books = data.get("items", [])
        return books
    else:
        return []

def get_random_book(books):
    if books:
        return random.choice(books)
    else:
        return None
    
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query_type = request.form["query_type"]
        query = request.form["query"]

        if query_type == "genre":
            query = f"+subject:{query}"
        elif query_type == "title":
            query = f"+intitle:{query}"

        books = get_books(query)
        book = get_random_book(books)

        if book:
            title = book["volumeInfo"]["title"]
            author = book["volumeInfo"].get("authors", ["Unknown Author"])[0]
            thumbnail = book["volumeInfo"]["imageLinks"]["thumbnail"] if "imageLinks" in book["volumeInfo"] else None
            retail_price = book["saleInfo"].get("retailPrice", {}).get("amount") if "saleInfo" in book else None
            buy_link = book["saleInfo"].get("buyLink") if "saleInfo" in book else None
            
            recommendation = {
                "title": title,
                "author": author,
                "image": thumbnail,
                "retail_price": f"${retail_price}" if retail_price else None,
                "buy_link": buy_link
            }
        else:
            recommendation = None
        
        return render_template("index.html", recommendation=recommendation)

    return render_template("index.html", recommendation=None)

if __name__ == "__main__":
    app.run(debug=True)