# Documentation for src/obsidianDataSQL/obisidian_to_SQL.py

# Obsidian Note Properties Extractor and MySQL Uploader

This script extracts properties from Obsidian notes stored in specified folders and uploads them to a MySQL database. The properties are assumed to be in YAML front matter format within the notes.

## Table of Contents

* [Function 1: `extract_properties_from_note`](#function-1-extract_properties_from_note)
    * Description: Extracts properties from an Obsidian note.
    * Parameters: `note_path` (str, path to the Obsidian note).
    * Returns: A dictionary containing the properties extracted from the note.

* [Function 2: `get_all_properties_from_folders`](#function-2-get_all_properties_from_folders)
    * Description: Iterates through specified folders and extracts properties from all Obsidian notes.
    * Parameters: `folder` (str, path to the folder containing Obsidian notes).
    * Returns: A list of dictionaries, each containing the properties extracted from a note.

* [Function 3: `push_properties_to_mysql`](#function-3-push_properties_to_mysql)
    * Description: Pushes extracted properties to a MySQL database using pandas and sqlalchemy.
    * Parameters:
        * `properties` (list, list of dictionaries containing properties).
        * `db_url` (str, MySQL database connection URL).
        * `table_name` (str, name of the table in the database).
    * Returns: None.

## Detailed Function Descriptions

### Function 1: `extract_properties_from_note`

**Description**: Extracts properties from an Obsidian note. Properties are assumed to be in YAML front matter format (key: value or key: [list]).

**Parameters**:
* `note_path` (str): Path to the Obsidian note.

**Returns**: A dictionary containing the properties extracted from the note.

**Example Usage**:
```python
note_path = './Media Ratings/Reading/Books/note1.md'
properties = extract_properties_from_note(note_path)
print(properties)
```

### Function 2: `get_all_properties_from_folders`

**Description**: Iterates through specified folders and extracts properties from all Obsidian notes.

**Parameters**:
* `folder` (str): Path to the folder containing Obsidian notes.

**Returns**: A list of dictionaries, each containing the properties extracted from a note.

**Example Usage**:
```python
folder = './Media Ratings/Reading/Books'
all_properties = get_all_properties_from_folders(folder)
print(all_properties)
```

### Function 3: `push_properties_to_mysql`

**Description**: Pushes extracted properties to a MySQL database using pandas and sqlalchemy.

**Parameters**:
* `properties` (list): List of dictionaries containing properties.
* `db_url` (str): MySQL database connection URL.
* `table_name` (str): Name of the table in the database.

**Returns**: None.

**Example Usage**:
```python
db_url = "mysql://root:password@192.168.86.2/obsidian"
table_name = "books"
properties = get_all_properties_from_folders('./Media Ratings/Reading/Books')
push_properties_to_mysql(properties, db_url, table_name)
```

## Example Usage

Here is an example of how to use the script to extract properties from Obsidian notes and upload them to a MySQL database:

```python
if __name__ == "__main__":
    # Specify the folders containing Obsidian notes
    folder_books = './Media Ratings/Reading/Books'
    folder_movies = './Media Ratings/Movies&Shows'

    # MySQL database connection URL (update with your credentials)
    db_url = "mysql://root:password@192.168.86.2/obsidian"

    # Table name in the database
    table_name_books = "books"
    table_name_movies = "movies"

    # Extract properties from notes
    properties_books = get_all_properties_from_folders(folder_books)
    properties_movies = get_all_properties_from_folders(folder_movies)

    # Push properties to MySQL
    push_properties_to_mysql(properties_books, db_url, table_name_books)
    push_properties_to_mysql(properties_movies, db_url, table_name_movies)
```

This script will iterate through the specified folders, extract properties from all Obsidian notes, and upload them to the specified MySQL database tables.