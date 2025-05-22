import os
import pandas as pd
from sqlalchemy import create_engine
import yaml


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


def push_properties_to_mysql(properties, db_url, table_name):
    """
    Pushes extracted properties to a MySQL database using pandas and sqlalchemy.
    """
    # Normalize properties to ensure consistent structure
    normalized_properties = []
    for prop in properties:
        if isinstance(prop, dict):
            normalized_properties.append(
                {
                    k: (v if not isinstance(v, list) else ", ".join(map(str, v)))
                    for k, v in prop.items()
                }
            )

    # Convert normalized properties to a DataFrame
    df = pd.DataFrame(normalized_properties)
    print(f"DataFrame created with {len(df)} records.")
    df = df[df['rating'].notna()]  # Remove rows where 'ratings' column is None
    print(f"DataFrame created with {len(df)} records after filtering.")

    # Create SQLAlchemy engine
    engine = create_engine(db_url)
    print(f"Connected to database at {db_url}")

    # Push DataFrame to MySQL
    df.to_sql(table_name, con=engine, if_exists="replace", index=False)
    print(f"Data successfully pushed to table '{table_name}' in the database.")


if __name__ == "__main__":
    # Specify the folders containing Obsidian notes
    folder_books = "./Media Ratings/Reading/Books"
    folder_movies = "./Media Ratings/Movies&Shows"

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
