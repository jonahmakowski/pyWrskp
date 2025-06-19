# Documentation for src/voiceAssistants/newVoiceAssistant/main.py

# Python Script Documentation

## Overview

This Python script is designed to create a voice-activated assistant that can perform various actions based on user commands. The assistant uses the Porcupine wake word detection engine to listen for a specific wake word ("computer") and processes voice commands to interact with an AI model. The assistant can respond to user queries and execute specific actions based on the parsed commands.

## Table of Contents

1. [General Setup](#general-setup)
2. [Functions](#functions)
    - [get_sys_prompt](#get_sys_prompt)
    - [get_message_list](#get_message_list)
    - [parse_command](#parse_command)
3. [Main Function](#main)
4. [Example Usage](#example-usage)

## General Setup

The script begins with importing necessary modules and setting up environment variables.

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
from weather_get import get_weather
from google_calendar_api import get_events, get_credentials

# General Setup
load_dotenv()
AI_KEY = getenv('AI_TOKEN')
VOICE_KEY = getenv('VOICE_DETECTION_TOKEN')
AI_MODEL = getenv('AI_MODEL')
AI_URL = getenv('AI_URL')
SYS_PROMPT = load_from_file('prompt.md')
# Commands dictionary format: {ai_command: [function, requires_arguments]}
COMMANDS = {'open-app': [actions.open_app, True], 'search-the-web': [actions.search, True],
            'open-file': [actions.open_file, True], 'spotify': [spotify_runner.do_spotify, True, True], 'open-webpage': [actions.open_webpage, True],
            'open-folder': [actions.open_directory_in_finder, True], 'hide-application': [actions.hide_app, True],
            'question-mode': ['Question Mode', False], 'clipboard-contents': [paste, False], 'terminate': [actions.terminate, False],
            'quit-application': [actions.quit_app, True]}
USER_NAME = 'Jonah'

# Verify google calendar credentials
get_credentials()

# Confirming env variables are set
if AI_KEY is None or VOICE_KEY is None:
    raise ValueError('An environment variable (AI_KEY or VOICE_DETECTION_TOKEN) is not set')
```

## Functions

### get_sys_prompt

Generates a system prompt string containing the current date, time, user name, AI model, and formatted weather information.

```python
def get_sys_prompt() -> str:
    """
    Generates a system prompt string containing the current date, time, user name, AI model,
    and formatted weather information.

    Returns:
        str: A formatted system prompt string.

    Dependencies:
        - datetime.now(): Retrieves the current date and time.
        - get_weather(): Fetches weather data.
        - ai_weather_display(weather_data): Formats the weather data for display.
        - SYS_PROMPT: A predefined string template requiring placeholders for date, time,
          user name, AI model, and weather information.
        - USER_NAME: The name of the user.
        - AI_MODEL: The name or identifier of the AI model.
    """
    current_datetime = datetime.now()
    cur_date = current_datetime.strftime("%B %d, %Y")
    cur_time = current_datetime.strftime("%I:%M %p")
    weather_data = get_weather()
    weather_display = ai_weather_display(weather_data)
    _, events = get_events(5)
    return SYS_PROMPT.format(cur_date, cur_time, USER_NAME, AI_MODEL, weather_display, events)
```

### get_message_list

Updates the message list with a new user message.

```python
def get_message_list(cur_list: list, message: str, max_size=10) -> list:
    """
    Update the message list with a new user message.

    Args:
        cur_list (list): The current list of messages.
        message (str): The new user message to add.
        max_size (int, optional): The maximum size of the message list. Defaults to 10.

    Returns:
        list: The updated message list.
    """
    if not cur_list:
        return [{"role": "system", "content": get_sys_prompt()},
                {"role": "user", "content": message}]
    while len(cur_list) > max