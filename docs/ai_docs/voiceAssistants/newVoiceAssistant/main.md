# Documentation for src/voiceAssistants/newVoiceAssistant/main.py

# Voice Assistant Script Documentation

## Program Overview

The provided Python script is a voice assistant designed to interact with users through voice commands. It leverages the Porcupine wake word detection engine and the PvRecorder for audio input. The assistant can respond to user queries and execute specific actions based on the parsed commands. The script integrates with an AI model to generate responses and perform various actions such as opening applications, searching the web, and managing Spotify.

## Table of Contents

- [General Setup](#general-setup)
- [Commands Dictionary](#commands-dictionary)
- [Functions](#functions)
  - [get_message_list](#get_message_list)
  - [parse_command](#parse_command)
  - [main](#main)
- [Example Usage](#example-usage)

## General Setup

The script begins by loading environment variables and setting up necessary configurations. It includes the following steps:

1. Load environment variables from a `.env` file.
2. Set up API keys and URLs for the AI model and voice detection.
3. Load a system prompt from a file.
4. Define a dictionary of commands and their corresponding functions.
5. Confirm that essential environment variables are set.

```python
load_dotenv()
AI_KEY = getenv('AI_TOKEN')
VOICE_KEY = getenv('VOICE_DETECTION_TOKEN')
AI_MODEL = getenv('AI_MODEL')
AI_URL = getenv('AI_URL')
SYS_PROMPT = load_from_file('prompt.md')
COMMANDS = {'open-app': [actions.open_app, True], 'search-the-web': [actions.search, True],
            'open-file': [actions.open_file, True], 'spotify': [spotify_runner.do_spotify, True, True], 'open-webpage': [actions.open_webpage, True],
            'open-folder': [actions.open_directory_in_finder, True], 'hide-application': [actions.hide_app, True],
            'question-mode': ['Question Mode', False], 'clipboard-contents': [paste, False], 'terminate': [actions.terminate, False],
            'quit-application': [actions.quit_app, True]}
USER_NAME = 'Jonah'

if AI_KEY is None or VOICE_KEY is None:
    raise ValueError('An environment variable (AI_KEY or VOICE_DETECTION_TOKEN) is not set')
```

## Commands Dictionary

The `COMMANDS` dictionary maps AI commands to their corresponding functions and specifies whether the command requires arguments.

```python
COMMANDS = {
    'open-app': [actions.open_app, True],
    'search-the-web': [actions.search, True],
    'open-file': [actions.open_file, True],
    'spotify': [spotify_runner.do_spotify, True, True],
    'open-webpage': [actions.open_webpage, True],
    'open-folder': [actions.open_directory_in_finder, True],
    'hide-application': [actions.hide_app, True],
    'question-mode': ['Question Mode', False],
    'clipboard-contents': [paste, False],
    'terminate': [actions.terminate, False],
    'quit-application': [actions.quit_app, True]
}
```

## Functions

### get_message_list

**Description:** Update the message list with a new user message.

**Parameters:**
- `cur_list` (list): The current list of messages.
- `message` (str): The new user message to add.
- `max_size` (int, optional): The maximum size of the message list. Defaults to 10.

**Returns:** The updated message list.

```python
def get_message_list(cur_list: list, message: str, max_size=10) -> list:
    current_datetime = datetime.now()
    cur_date = current_datetime.strftime("%B %d, %Y")
    cur_time = current_datetime.strftime("%I:%M %p")
    if not cur_list:
        return [{"role": "system", "content": SYS_PROMPT.format(cur_date, cur_time, USER_NAME, AI_MODEL)},
                {"role": "user", "content": message}]
    while len(cur_list) > max_size:
        cur_list.pop(0)
    cur_list[0] = {"role": "system", "content": SYS_PROMPT.format(cur_date, cur_time, USER_NAME, AI_MODEL)}
    cur_list.append({"role": "user", "content": message})
    return cur_list
```

### parse_command

**Description:** Parses a given message to identify and execute commands, and returns the processed message along with a flag indicating whether the message is in "Question Mode".

**Parameters:**
- `message` (str): The input message to be parsed.
- `message_list