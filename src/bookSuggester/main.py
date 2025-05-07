import os
import requests
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from pyWrkspPackage import ai_response

engine = create_engine("mysql://root:password@192.168.86.2:3306/obsidian")

# Load environment variables
load_dotenv()
GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")
AI_API_KEY = os.getenv("AI_API_KEY")

# Set constants
AI_MODEL = "mistral-small-latest"
AI_URL = "http://192.168.86.4:4001"

# Fetch book data from Google Books API
def get_google_books_data(book_title):
    url = f"https://www.googleapis.com/books/v1/volumes"
    params = {"q": book_title, "key": GOOGLE_BOOKS_API_KEY}
    response = requests.get(url, params=params)
    data = response.json()
    if data.get("totalItems", 0) > 0:
        book = data["items"][0]["volumeInfo"]
        return {
            "title": book.get("title"),
            "authors": book.get("authors", []),
            "categories": book.get("categories", []),
            "description": book.get("description", ""),
            "publisher": book.get("publisher", ""),
            "published_date": book.get("publishedDate", ""),
        }
    return None

# Refactored: Find similar books by author and category, input is a DataFrame
def find_similar_books(df, rating_threshold=7):
    recommendations = []
    book_titles = df['title'].tolist()
    for _, row in df.iterrows():
        book_title = row['title']
        rating = row['rating']
        print(f"[Books API] Processing book: {book_title} with rating: {rating}")
        if rating < rating_threshold:
            continue  # Only look at highly rated books
        book_info = get_google_books_data(book_title)
        if not book_info:
            book_info = get_open_library_data(book_title)
        if book_info:
            authors = book_info["authors"]
            categories = book_info["categories"]
            # Get similar books by authors
            for author in authors:
                url = "https://www.googleapis.com/books/v1/volumes"
                params = {"q": f"inauthor:{author}", "key": GOOGLE_BOOKS_API_KEY}
                response = requests.get(url, params=params)
                results = response.json()
                for item in results.get("items", []):
                    volume_info = item["volumeInfo"]
                    recommended_title = volume_info.get("title")
                    if recommended_title and recommended_title.lower() != book_title.lower():
                        recommendations.append({
                            "title": recommended_title,
                            "authors": volume_info.get("authors", []),
                            "categories": volume_info.get("categories", []),
                            "description": volume_info.get("description", ""),
                            "reason": f"Same author: {author}"
                        })
            # Get similar books by categories
            for category in categories:
                url = "https://www.googleapis.com/books/v1/volumes"
                params = {"q": f"subject:{category}", "key": GOOGLE_BOOKS_API_KEY}
                response = requests.get(url, params=params)
                results = response.json()
                for item in results.get("items", []):
                    volume_info = item["volumeInfo"]
                    recommended_title = volume_info.get("title")
                    if recommended_title and recommended_title.lower() != book_title.lower():
                        recommendations.append({
                            "title": recommended_title,
                            "authors": volume_info.get("authors", []),
                            "categories": volume_info.get("categories", []),
                            "description": volume_info.get("description", ""),
                            "reason": f"Same category: {category}"
                        })
    # Removing duplicates
    unique_recommendations = {r['title']: r for r in recommendations}.values()
    unique_recommendations = list(unique_recommendations)

    for recommendation in unique_recommendations:
        if recommendation['title'] in book_titles:
            del recommendation  # Remove if already in the original list
            continue
        for book in book_titles:
            if book in recommendation['title']:
                del recommendation
                break

    return unique_recommendations

# Fetch book data from Open Library API
def get_open_library_data(book_title):
    url = "http://openlibrary.org/search.json"
    params = {"q": book_title}
    response = requests.get(url, params=params)
    data = response.json()
    if data.get("numFound", 0) > 0:
        book = data["docs"][0]
        return {
            "title": book.get("title"),
            "authors": book.get("author_name", []),
            "categories": book.get("subject", []),
            "description": "",
            "publisher": book.get("publisher", []),
            "published_date": book.get("first_publish_year", ""),
        }
    return None

def load_book_data():
    # Load book data from the database
    query = "SELECT title, rating FROM books"
    df = pd.read_sql(query, engine)
    print("Loaded book data from database.")
    return df

def get_book_sentiment(book_title):
    book_data = get_google_books_data(book_title)
    if not book_data:
        book_data = get_open_library_data(book_title)
    
    prompt = f"Based on this title: {book_data['title']}, authors: {', '.join(book_data['authors'])}, categories: {', '.join(book_data['categories'])}, and description: {book_data['description']}, Give me an overview of the book in 3 sentences."
    messages = [
        {"role": "user", "content": prompt}
    ]
    response, _ = ai_response(messages, AI_MODEL, AI_URL, AI_API_KEY)

    return response

def get_overall_book_sentiment(books):
    sentiments = []
    for book in books:
        print(f"[AI Based Sentiment] Processing book: {book['title']} with rating: {book['rating']}")
        if book['rating'] < 7:
            continue
        sentiment = get_book_sentiment(book['title'])
        sentiments.append({
            "title": book['title'],
            "sentiment": sentiment,
            "value": book['rating']
        })
    
    prompt = f"Based on the following summaries: {sentiments}, give me an overall understanding of what the books are. Chracterize the books in 3 sentences (Genre, etc). A higher value means that the book is more important to your summary. Just give me the summary, no other text."
    messages = [
        {"role": "user", "content": prompt}
    ]
    response, _ = ai_response(messages, AI_MODEL, AI_URL, AI_API_KEY)
    return response

def get_rating(book_title, book_description, overall_sentiment):
    prompt = f"Based on the following summary of what the user likes: {overall_sentiment}, rate on a scale from 1 to 100 how likely the user would like the book '{book_title}', here is the description: {book_description}. Include only the number, no other text."
    messages = [
        {"role": "user", "content": prompt}
    ]
    response, _ = ai_response(messages, AI_MODEL, AI_URL, AI_API_KEY)
    return int(response)

def find_best(overall_sentiment, recommendations):
    best_books = []
    for book in recommendations:
        print(f"[AI Based Rating] Processing book: {book['title']}")
        rating = get_rating(book['title'], book['description'], overall_sentiment)
        best_books.append({
            "title": book['title'],
            "rating": rating,
            "description": book['description'],
            "reason": book['reason']
        })
    
    # Sort by rating
    best_books.sort(key=lambda x: x['rating'], reverse=True)
    return best_books

# Example usage
if __name__ == "__main__":
    book_data = load_book_data()
    overall_sentiment = get_overall_book_sentiment(book_data.to_dict(orient='records'))
    recommendations = find_similar_books(book_data, rating_threshold=7)
    best = find_best(overall_sentiment, recommendations)
    print("Top 5 recommended books:")
    for book in best:
        print(f"Title: {book['title']}, Rating: {book['rating']}")
