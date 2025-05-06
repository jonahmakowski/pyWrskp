import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_BOOKS_API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")

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

# Find similar books by author and category
def find_similar_books(book_list, rating_threshold=7):
    recommendations = []
    for book_title, rating in book_list:
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
    return list(unique_recommendations)

# Example usage
if __name__ == "__main__":
    user_books_ratings = [
        ("The Hobbit", 10),
        ("1984", 8),
        ("Some Not-So-Great Book", 4),  # This one won't trigger recommendations
        ("Pride and Prejudice", 9),
    ]
    recommendations = find_similar_books(user_books_ratings)
    print("Recommended similar books:")
    for rec in recommendations:
        print(f"\nTitle: {rec['title']}")
        print(f"Authors: {', '.join(rec['authors']) if rec['authors'] else 'N/A'}")
        print(f"Categories: {', '.join(rec['categories']) if rec['categories'] else 'N/A'}")
        print(f"Description: {rec['description'] if rec['description'] else 'N/A'}")
        print(f"Reason: {rec['reason']}")