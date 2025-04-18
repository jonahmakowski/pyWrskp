# Documentation for src/voiceAssistants/newVoiceAssistant/main.py

# Python Script Documentation

## Program Overview

This Python script is designed to create a voice-activated assistant that can perform various commands based on user input. The assistant uses speech recognition to listen for commands, processes these commands using an AI model, and executes corresponding actions. The script leverages several libraries and modules, including `pyWrkspPackage`, `helper`, `actions`, `pvporcupine`, `pvrecorder`, `speech_recognition`, and `spotify_runner`.

## Table of Contents

- [General Setup](#general-setup)
- [Functions](#functions)
  - [get_message_list](#get_message_list)
  - [parse_command](#parse_command)
- [Main Function](#main-function)

## General Setup

The script begins by importing necessary modules and setting up environment variables. It loads environment variables from a `.env` file and checks if the required tokens are set. The script also defines a dictionary of commands that map AI commands to corresponding functions.

```python
from pyWrkspPackage import list_to_str, ai_response, load_from_file
from helper import *
import actions
from os import getenv
from dotenv import load_dotenv
import pvporcupine
from pvrecorder import PvRecorder
import speech_recognition as sr
from datetime import datetime
from pandas.io.clipboard import paste
import spotify_runner

# General Setup
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

# Confirming env variables are set
if AI_KEY is None or VOICE_KEY is None:
    raise ValueError('An environment variable (AI_KEY or VOICE_DETECTION_TOKEN) is not set')
```

## Functions

### get_message_list

**Description**: Updates the message list with a new user message.

**Parameters**:
- `cur_list` (list): The current list of messages.
- `message` (str): The new user message to add.
- `max_size` (int, optional): The maximum size of the message list. Defaults to 10.

**Returns**: The updated message list.

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

**Description**: Parses the command from the message and executes the corresponding function.

**Parameters**:
- `message` (str): The message containing the command.
- `message_list` (list): The current list of messages.

**Returns**: A tuple containing the updated message and a boolean indicating if the command is in question mode.

```python
def parse_command(message: str, message_list: list) -> tuple[str, bool]:
    split_message = message.split('$')
    command = None
    for chunk in split_message:
        for key in COMMANDS.keys():
            if key in chunk:
                del split_message[split_message.index(chunk)]
                command = (COMMANDS[key], chunk)
                break

    if command is None:
        return message, '?' in message

    func = command[0][0]
    if func == 'Question Mode':
        return list