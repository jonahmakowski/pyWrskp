# Documentation for src/bookSuggester/main.py

# Book Recommendation Script Documentation

## Program Overview
-------------------

This script is designed to fetch book data from various APIs, analyze the data to find similar books, and generate recommendations based on user preferences. The script utilizes the Google Books API and Open Library API to gather book information and the AI API to analyze book sentiments and generate ratings.

## Table of Contents
-----------------------------

- [get_google_books_data](#get_google_books_data)
- [find_similar_books](#find_similar_books)
- [get_open_library_data](#get_open_library_data)
- [load_book_data](#load_book_data)
- [get_book_sentiment](#get_book_sentiment)
- [get_overall_book_sentiment](#get_overall_book_sentiment)
- [get_rating](#get_rating)
- [find_best](#find_best)

## Detailed Function Descriptions
--------------------------------

### get_google_books_data

**Description**: Fetches book data from the Google Books API based on the book title.

**Parameters**:
- `book_title` (str): The title of the book to search for.

**Returns**: A dictionary containing book information (title, authors, categories, description, publisher, published_date) or `None` if no data is found.

```python
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
```

### find_similar_books

**Description**: Finds similar books based on authors and categories. It takes a DataFrame of book data as input and returns a list of recommended books.

**Parameters**:
- `df` (pd.DataFrame): DataFrame containing book data with columns 'title' and 'rating'.
- `rating_threshold` (int, optional): Minimum rating threshold for books to be considered. Default is 7.

**Returns**: A list of dictionaries containing recommended book information (title, authors, categories, description, reason).

```python
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
                            "authors