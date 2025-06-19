# Documentation for src/obsidianDataSQL/obisidian_to_SQL.py

# Script Documentation

This script is designed to extract properties from Obsidian notes, which are assumed to be in YAML front matter format, and push these properties to a MySQL database. The script consists of three main functions and an entry point for execution.

## Table of Contents

- [Function 1: `extract_properties_from_note`](#function-1-extract_properties_from_note)
    - Description: Extracts properties from an Obsidian note.
    - Parameters: `note_path` (str, path to the note file)
    - Returns: Dictionary of properties extracted from the note.

- [Function 2: `get_all_properties_from_folders`](#function-2-get_all_properties_from_folders)
    - Description: Iterates through specified folders and extracts properties from all Obsidian notes.
    - Parameters: `folder` (str, path to the folder containing notes)
    - Returns: List of dictionaries, each containing properties from a note and the note's path.

- [Function 3: `push_properties_to_mysql`](#function-3-push_properties_to_mysql)
    - Description: Pushes extracted properties to a MySQL database using pandas and sqlalchemy.
    - Parameters:
        - `properties` (list, list of dictionaries containing properties)
        - `db_url` (str, MySQL database connection URL)
        - `table_name` (str, name of the table in the database)
    - Returns: None

- [Example Usage](#example-usage)

## Detailed Function Descriptions

### Function 1: `extract_properties_from_note`

**Description:** This function extracts properties from an Obsidian note. Properties are assumed to be in YAML front matter format (key: value or key: [list]).

**Parameters:**
- `note_path` (str): Path to the note file.

**Returns:** Dictionary of properties extracted from the note.

```python
def extract_properties_from_note(note_path):
    """
    Extracts properties from an Obsidian note.
    Properties are assumed to be in YAML front matter format (key: value or key: [list]).
    """
    properties = {}
    with open(note_path, "r", encoding="utf-8") as file:
        lines = file.readlines()
        if lines[0].strip() == "---":  # Check for YAML front matter
            yaml_lines = []
            for line in lines[1:]:
                if line.strip() == "---":  # End of YAML front matter
                    break
                yaml_lines.append(line)

            # Parse YAML content
            yaml_content = "\n".join(yaml_lines)
            try:
                properties = yaml.safe_load(yaml_content)
            except Exception as e:
                print(f"Error parsing YAML: {e}")

    for prop in properties:
        if isinstance(properties[prop], list):
            properties[prop] = [
                (float(item) if item.replace(".", "").isdigit() else str(item))
                for item in properties[prop]
            ]
        elif isinstance(properties[prop], str):
            if properties[prop].replace(".", "", 1).isdigit():
                properties[prop] = float(properties[prop])

    return properties
```

### Function 2: `get_all_properties_from_folders`

**Description:** This function iterates through specified folders and extracts properties from all Obsidian notes.

**Parameters:**
- `folder` (str): Path to the folder containing notes.

**Returns:** List of dictionaries, each containing properties from a note and the note's path.

```python
def get_all_properties_from_folders(folder):
    """
    Iterates through specified folders and extracts properties from all Obsidian notes.
    """
    all_properties = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".md"):  # Only process Markdown files
                note_path = os.path.join(root, file)
                properties = extract_properties_from_note(note_path)
                properties["note_path"] = note_path  # Add note path for reference
                all_properties.append(properties)
    return all_properties
```

### Function 3: `push_properties_to_mysql`

**Description:** This function pushes extracted properties to a MySQL database using pandas and sqlalchemy.

**Parameters:**
- `properties` (list): List of dictionaries containing properties.
- `db_url` (str): MySQL database connection URL.
- `table_name` (str): Name of the table in the database.

**Returns:** None

```python
def push_properties_to_mysql(properties, db_url, table_name):
    """
    Pushes extracted properties to a MySQL database using pandas and sqlalchemy.
    """
    # Normalize properties to ensure consistent structure
    normalized_properties =