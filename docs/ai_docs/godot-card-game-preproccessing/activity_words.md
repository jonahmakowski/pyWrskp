# Documentation for src/godot-card-game-preproccessing/activity_words.py

# AI Summary
The `activity_words.py` script is designed to process a list of English words. It first fetches definitions for these words using the dictionaryapi.dev, handling various API and network errors. Subsequently, it uses an AI model (via the `pyWrkspPackage`) to rate each word based on its suitability for "speaking", "pantomiming", and "drawing" activities. Finally, it compiles these definitions and ratings and saves them into a JSON file named `activity_words.json`.

The AI gave it a general rating of 9/10

The AI gave it a conventions rating of 9/10

The reason for the AI's rating is:

The code demonstrates high quality with robust error handling for API calls, including specific HTTP errors and retry mechanisms for rate limiting. The `get_word_definition` function is well-structured, concise, and clearly documented with type hints. Adherence to Python conventions is strong, with clear variable names and a logical flow of execution. The overall script effectively achieves its goal of processing words and their attributes.
# Functions

## get_word_definition
### Explanation
This function retrieves definitions for a given word using the dictionaryapi.dev API. It constructs the API URL, makes a GET request, and parses the JSON response to extract definitions. The function handles various potential errors, including HTTP errors (e.g., 404 for word not found, 429 for rate limit with a retry mechanism), network errors, timeout errors, and JSON decoding issues. It returns a list of formatted definition strings (including part of speech) if successful, or a descriptive error message string otherwise.
### Code
```python
def get_word_definition(word: str) -> list[str] | str:
    """
    Gets the definition(s) of a word using the dictionaryapi.dev API.

    Args:
        word (str): The word for which to retrieve definitions.

    Returns:
        list[str] | str: A list of formatted definition strings if successful,
                         where each string includes the part of speech and the definition.
                         Returns an error message string if the word is not found
                         or an API error occurs.
    """
    base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    api_url = (
        f"{base_url}{word.lower()}"  # Convert to lowercase for consistent API calls
    )

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

        data = response.json()

        if not data:
            return f"No data found for '{word}'. The API returned an empty response."

        # The API returns a list, even for a single word query.
        # Typically, the first element contains the primary information.
        word_info = data[0]

        definitions = []
        if "meanings" in word_info:
            for meaning in word_info["meanings"]:
                part_of_speech = meaning.get("partOfSpeech", "N/A")
                if "definitions" in meaning:
                    for definition_obj in meaning["definitions"]:
                        definition_text = definition_obj.get("definition")
                        if definition_text:
                            definitions.append(f"({part_of_speech}) {definition_text}")

        if definitions:
            return definitions
        else:
            return f"No definitions found for '{word}' in the API response despite successful query."

    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return f"'{word}' not found in the dictionary. Please check the spelling."
        elif response.status_code == 429:
            print("Rate limit exceeded. Waiting for 5 seconds before retrying...")
            sleep(5)
            return get_word_definition(word)
        else:
            return f"HTTP error occurred: {e} (Status Code: {response.status_code})"
    except requests.exceptions.ConnectionError:
        return "Network error: Could not connect to the dictionary API. Please check your internet connection."
    except requests.exceptions.Timeout:
        return "Timeout error: The request to the dictionary API took too long."
    except requests.exceptions.RequestException as e:
        return f"An unexpected request error occurred: {e}"
    except ValueError:  # JSON decoding error
        return f"Error: Could not decode JSON response from the API for '{word}'."
    except IndexError:  # If data is empty or not in expected list format
        return f"Error: Unexpected response format from API for '{word}'."
```
# Overall File Contents
```python
import pyWrkspPackage
import requests
import os
from dotenv import load_dotenv
from time import sleep


def get_word_definition(word: str) -> list[str] | str:
    """
    Gets the definition(s) of a word using the dictionaryapi.dev API.

    Args:
        word (str): The word for which to retrieve definitions.

    Returns:
        list[str] | str: A list of formatted definition strings if successful,
                         where each string includes the part of speech and the definition.
                         Returns an error message string if the word is not found
                         or an API error occurs.
    """
    base_url = "https://api.dictionaryapi.dev/api/v2/entries/en/"
    api_url = (
        f"{base_url}{word.lower()}"  # Convert to lowercase for consistent API calls
    )

    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)

        data = response.json()

        if not data:
            return f"No data found for '{word}'. The API returned an empty response."

        # The API returns a list, even for a single word query.
        # Typically, the first element contains the primary information.
        word_info = data[0]

        definitions = []
        if "meanings" in word_info:
            for meaning in word_info["meanings"]:
                part_of_speech = meaning.get("partOfSpeech", "N/A")
                if "definitions" in meaning:
                    for definition_obj in meaning["definitions"]:
                        definition_text = definition_obj.get("definition")
                        if definition_text:
                            definitions.append(f"({part_of_speech}) {definition_text}")

        if definitions:
            return definitions
        else:
            return f"No definitions found for '{word}' in the API response despite successful query."

    except requests.exceptions.HTTPError as e:
        if response.status_code == 404:
            return f"'{word}' not found in the dictionary. Please check the spelling."
        elif response.status_code == 429:
            print("Rate limit exceeded. Waiting for 5 seconds before retrying...")
            sleep(5)
            return get_word_definition(word)
        else:
            return f"HTTP error occurred: {e} (Status Code: {response.status_code})"
    except requests.exceptions.ConnectionError:
        return "Network error: Could not connect to the dictionary API. Please check your internet connection."
    except requests.exceptions.Timeout:
        return "Timeout error: The request to the dictionary API took too long."
    except requests.exceptions.RequestException as e:
        return f"An unexpected request error occurred: {e}"
    except ValueError:  # JSON decoding error
        return f"Error: Could not decode JSON response from the API for '{word}'."
    except IndexError:  # If data is empty or not in expected list format
        return f"Error: Unexpected response format from API for '{word}'."


file = pyWrkspPackage.load_from_file("google-10000-english-no-swears.txt")
words = file.split("\n")

words_with_definitions = {}

for index, word in enumerate(words):
    if len(word) > 3:
        print(f"Getting definition for: {word} ({index + 1}/{len(words)})")
        definitions = get_word_definition(word)
        if isinstance(definitions, list):
            words_with_definitions[word] = definitions
        else:
            print(definitions)

pyWrkspPackage.json_write_file("words_with_definitions.json", words_with_definitions)


# words_with_definitions = pyWrkspPackage.json_load_file("words_with_definitions.json")

load_dotenv()
ai_key = os.getenv("LITELLM_KEY")

system_prompt = pyWrkspPackage.load_from_file("activity_words_system_prompt.md")

ratings_and_definitions = {}

for index, word in enumerate(words_with_definitions.keys()):
    result, _ = pyWrkspPackage.ai_response(
        [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": "Word: {}".format(word)},
        ],
        "litellm/general_model",
        url="http://192.168.86.11:4001",
        key=ai_key,
    )
    print("\n\nWord: {}. ({}/{})".format(word, index + 1, len(words_with_definitions)))
    print(result)

    speaking = int(result.split("\n")[0].split(": ")[1])
    pantomiming = int(result.split("\n")[1].split(": ")[1])
    drawing = int(result.split("\n")[2].split(": ")[1])

    ratings_and_definitions[word] = {
        "definitions": words_with_definitions[word],
        "speaking": speaking,
        "pantomiming": pantomiming,
        "drawing": drawing,
    }

pyWrkspPackage.json_write_file("activity_words.json", ratings_and_definitions)

```
