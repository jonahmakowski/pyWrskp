# Documentation for src/voiceAssistants/improvedAssistant/v1.1/main.py

# Python Script Documentation

## Overview

This Python script is designed to create an interactive assistant that can perform various tasks based on voice commands. The assistant uses speech recognition to interpret user commands, executes corresponding actions, and provides feedback through text-to-speech. The script leverages several libraries, including `PySimpleGUI` for the graphical user interface, `speech_recognition` for voice input, `gTTS` for text-to-speech, and `subprocess` for running external scripts.

## Table of Contents

* [Function 1: `find_closest_command`](#find_closest_command)
* [Function 2: `listen`](#listen)
* [Function 3: `speak_text`](#speak_text)
* [Function 4: `run_app`](#run_app)
* [Function 5: `open_file`](#open_file)
* [Function 6: `open_web`](#open_web)
* [Function 7: `python_run`](#python_run)
* [Function 8: `start_music`](#start_music)
* [Function 9: `create_file`](#create_file)
* [Function 10: `stop_music`](#stop_music)
* [Function 11: `ai_backend`](#ai_backend)
* [Function 12: `ask_ai`](#ask_ai)
* [Function 13: `remove_keyword`](#remove_keyword)
* [Function 14: `place_in_top_right`](#place_in_top_right)
* [Function 15: `parse_command`](#parse_command)
* [Function 16: `run_assistant`](#run_assistant)

## Detailed Function Descriptions

### find_closest_command

**Description:** Finds the closest matching command from a list of commands based on the user's input.

**Parameters:**
* `user_input` (str): The input string provided by the user.
* `command_list` (list of str): A list of possible command strings to match against.

**Returns:** A tuple containing the closest matching command (str) and the similarity score (float).

### listen

**Description:** Listens to the user's speech through the microphone, converts it to text using Google's speech recognition, and plays a sound before and after listening.

**Parameters:** None

**Returns:** The recognized text from the user's speech, or `None` if the speech could not be recognized.

**Raises:** Exception: If there is an error during the speech recognition process.

### speak_text

**Description:** Converts the given text to speech and plays it.

**Parameters:**
* `text` (str): The text to be converted to speech.
* `wait` (bool, optional): If `True`, the function will wait until the speech is finished playing before returning. Defaults to `True`.

**Returns:** None

### run_app

**Description:** Executes a bash script with the provided application name as an argument.

**Parameters:**
* `app` (str): The name of the application to be passed to the bash script.

**Returns:** None

### open_file

**Description:** Opens a file using a bash script.

**Parameters:**
* `file` (str): The name or path of the file to open.
* `loc` (str, optional): An optional location parameter to be passed to the bash script. Defaults to `None`.

**Returns:** None

### open_web

**Description:** Opens a web page using a bash script.

**Parameters:**
* `url` (str): The URL of the web page to open.

**Returns:** None

### python_run

**Description:** Executes a Python script using a bash script.

**Parameters:**
* `file` (str): The path to the Python script to be executed.
* `loc` (str, optional): An optional location argument to be passed to the bash script.

**Returns:** None

### start_music

**Description:** Starts playing music by running a bash script.

**Parameters:** None

**Returns:** None

### create_file

**Description:** Creates a file by running a bash script.

**Parameters:**
* `file` (str): The name of the file to be created.

**Returns:** None

### stop_music

**Description:** Stops the music by running a bash script with the 'pause' argument.

**Parameters:** None

**Returns:** None

### ai_backend

**Description:** Processes a chat conversation using the Ollama AI model and returns the latest response.

**Parameters:**
* `chat` (list): A list of dictionaries representing the chat messages. Each dictionary should contain at least a 'message' key with the message content.

**Returns:** A tuple containing:
* `str`: The content of