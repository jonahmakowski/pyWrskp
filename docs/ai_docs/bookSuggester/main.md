# Documentation for src/bookSuggester/main.py

# Book Recommendation Script Documentation

This script is designed to fetch book data from Google Books and Open Library APIs, analyze book sentiments using an AI model, and recommend books based on user preferences. The script leverages various Python libraries, including `requests`, `pandas`, and `sqlalchemy`.

## Table of Contents

- [Setup](#setup)
- [Functions](#functions)
  - [get_google_books_data](#get_google_books_data)
  - [find_similar_books](#find_similar_books)
  - [get_open_library_data](#get_open_library_data)
  - [load_book_data](#load_book_data)
  - [get_book_sentiment](#get_book_sentiment)
  - [get_overall_book_sentiment](#get_overall_book_sentiment)
  - [get_rating](#get_rating)
  - [find_best](#find_best)
- [Example Usage](#example-usage)

## Setup

Before running the script, ensure you have the following environment variables set:

- `GOOGLE_BOOKS_API_KEY`: Your Google Books API key.
- `AI_API_KEY`: Your AI API key.

You can set these environment variables in a `.env` file in the same directory as the script.

## Functions

### get_google_books_data

**Description**: Fetches book data from the Google Books API based on the book title.

**Parameters**:
- `book_title` (str): The title of the book to search for.

**Returns**: A dictionary containing book information, or `None` if no book is found.

**Example Usage**:
```python
book_info = get_google_books_data("To Kill a Mockingbird")
print(book_info)
```

### find_similar_books

**Description**: Finds similar books based on authors and categories, given a DataFrame of book data.

**Parameters**:
- `df` (DataFrame): A DataFrame containing book data with columns `title` and `rating`.
- `rating_threshold` (int, optional): The minimum rating for a book to be considered. Default is 7.

**Returns**: A list of dictionaries containing recommended book information.

**Example Usage**:
```python
df = pd.DataFrame({
    "title": ["To Kill a Mockingbird", "1984"],
    "rating": [8, 9]
})
recommendations = find_similar_books(df)
print(recommendations)
```

### get_open_library_data

**Description**: Fetches book data from the Open Library API based on the book title.

**Parameters**:
- `book_title` (str): The title of the book to search for.

**Returns**: A dictionary containing book information, or `None` if no book is found.

**Example Usage**:
```python
book_info = get_open_library_data("To Kill a Mockingbird")
print(book_info)
```

### load_book_data

**Description**: Loads book data from a MySQL database.

**Parameters**: None

**Returns**: A DataFrame containing book data.

**Example Usage**:
```python
df = load_book_data()
print(df)
```

### get_book_sentiment

**Description**: Fetches the sentiment of a book using an AI model.

**Parameters**:
- `book_title` (str): The title of the book.

**Returns**: A string containing the book sentiment.

**Example Usage**:
```python
sentiment = get_book_sentiment("To Kill a Mockingbird")
print(sentiment)
```

### get_overall_book_sentiment

**Description**: Fetches the overall sentiment of a list of books using an AI model.

**Parameters**:
- `books` (list): A list of dictionaries containing book information.

**Returns**: A string containing the overall book sentiment.

**Example Usage**:
```python
books = [
    {"title": "To Kill a Mockingbird", "rating": 8},
    {"title": "1984", "rating": 9}
]
overall_sentiment = get_overall_book_sentiment(books)
print(overall_sentiment)
```

### get_rating

**Description**: Fetches a rating for a book based on the overall sentiment using an AI model.

**Parameters**:
- `book_title` (str): The title of the book.
- `book_description` (str): The description of the book.
- `overall_sentiment` (str): The overall sentiment of the books.

**Returns**: An integer rating for the book.

**Example Usage**:
```python
rating = get_rating("To Kill a Mockingbird", "A novel about the American South during the 1930s.", "The books are about the American South during the 1930s.")
print(rating)
```

### find_best

**Description**: Finds the best