# Documentation for src/voiceAssistants/improvedAssistant/v1.0/main.py

# Python Script Documentation

## Program Overview
-------------------

The provided Python script is designed to create an interactive assistant GUI that allows users to execute various commands such as opening applications, files, websites, running Python scripts, playing music, creating files, and interacting with an AI chatbot. The script utilizes the `subprocess` module to execute bash scripts for different actions and `PySimpleGUI` for the graphical user interface.

## Table of Contents
-----------------------------

Here is a table of contents listing all the functions and classes in the script:

* [run_app](#run_app)
    * Description: Executes a bash script with the provided application name as an argument.
    * Parameters: `app (str)` - The name of the application to be passed to the bash script.
    * Returns: `None`

* [open_file](#open_file)
    * Description: Opens a file using a bash script.
    * Parameters:
        * `file (str)` - The name or path of the file to open.
        * `loc (str, optional)` - An optional location parameter to be passed to the bash script. Defaults to `None`.
    * Returns: `None`

* [open_web](#open_web)
    * Description: Opens a web page using a bash script.
    * Parameters: `url (str)` - The URL of the web page to open.
    * Returns: `None`

* [python_run](#python_run)
    * Description: Executes a Python script using a bash script.
    * Parameters:
        * `file (str)` - The path to the Python file to be executed.
        * `loc (str, optional)` - An optional location argument to be passed to the bash script.
    * Returns: `None`

* [start_music](#start_music)
    * Description: Starts playing music by running a bash script.
    * Returns: `None`

* [create_file](#create_file)
    * Description: Creates a file by running a bash script.
    * Parameters: `file (str)` - The name of the file to be created.
    * Returns: `None`

* [stop_music](#stop_music)
    * Description: Stops the music by running a shell script.
    * Returns: `None`

* [ai_backend](#ai_backend)
    * Description: Processes a chat conversation using the Ollama AI model and returns the latest response.
    * Parameters: `chat (list)` - A list of dictionaries representing the chat history. Each dictionary should have a 'message' key.
    * Returns: `tuple` - A tuple containing the latest response content (str) and the updated chat history (list).

* [ask_ai](#ask_ai)
    * Description: Launches a simple AI chat interface using PySimpleGUI.
    * Returns: `None`

* [remove_keyword](#remove_keyword)
    * Description: Removes the first occurrence of a specified keyword from a given text.
    * Parameters:
        * `text (str)` - The input text from which the keyword will be removed.
        * `keyword (str)` - The keyword to be removed from the text.
    * Returns: `str` - The text with the first occurrence of the keyword removed.

* [place_in_top_right](#place_in_top_right)
    * Description: Places the given window in the top right corner of the screen.
    * Parameters: `window` - An object representing the window to be positioned.
    * Returns: The window object with its position updated to the top right corner of the screen.

* [parse_command](#parse_command)
    * Description: Parses and executes a given command.
    * Parameters: `command (str)` - The command to be parsed and executed.
    * Returns: `None`

* [run_assistant](#run_assistant)
    * Description: Launches the assistant GUI and handles user interactions.
    * Returns: `None`

## Detailed Function Descriptions
--------------------------------

### run_app

**Description**: Executes a bash script with the provided application name as an argument.

**Parameters**:
* `app (str)` - The name of the application to be passed to the bash script.

**Returns**: `None`

**Example Usage**:
```python
run_app("firefox")
```

### open_file

**Description**: Opens a file using a bash script.

**Parameters**:
* `file (str)` - The name or path of the file to open.
* `loc (str, optional)` - An optional location parameter to be passed to the bash script. Defaults to `None`.

**Returns**: `None`

**Example Usage**:
```python
open_file("document.txt")
open_file("document.txt", "/home/user/documents")
```

### open_web

**Description**: Opens a web