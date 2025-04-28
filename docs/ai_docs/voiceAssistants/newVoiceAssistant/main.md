# Documentation for src/voiceAssistants/newVoiceAssistant/main.py

# Voice Assistant Script Documentation

## Overview

This Python script implements a voice-activated assistant that uses wake-word detection, speech recognition, and AI-based responses to perform various tasks. The assistant can execute commands, search the web, manage applications, and interact with Spotify and Google Calendar. The script leverages several external libraries and APIs to achieve its functionality.

## Table of Contents

- [Environment Setup](#environment-setup)
- [Function Descriptions](#function-descriptions)
  - [get_sys_prompt](#get_sys_prompt)
  - [get_message_list](#get_message_list)
  - [parse_command](#parse_command)
  - [main](#main)
- [Example Usage](#example-usage)

## Environment Setup

The script requires several environment variables and dependencies to function correctly. Ensure you have the following:

- `AI_TOKEN`: API token for the AI model.
- `VOICE_DETECTION_TOKEN`: API token for voice detection.
- `AI_MODEL`: Identifier for the AI model.
- `AI_URL`: URL for the AI model endpoint.

These variables should be set in a `.env` file in the same directory as the script.

## Function Descriptions

### get_sys_prompt

Generates a system prompt string containing the current date, time, user name, AI model, and formatted weather information.

**Returns:**
- `str`: A formatted system prompt string.

**Dependencies:**
- `datetime.now()`: Retrieves the current date and time.
- `get_weather()`: Fetches weather data.
- `ai_weather_display(weather_data)`: Formats the weather data for display.
- `SYS_PROMPT`: A predefined string template requiring placeholders for date, time, user name, AI model, and weather information.
- `USER_NAME`: The name of the user.
- `AI_MODEL`: The name or identifier of the AI model.

```python
def get_sys_prompt() -> str:
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

**Parameters:**
- `cur_list` (list): The current list of messages.
- `message` (str): The new user message to add.
- `max_size` (int, optional): The maximum size of the message list. Defaults to 10.

**Returns:**
- `list`: The updated message list.

```python
def get_message_list(cur_list: list, message: str, max_size=10) -> list:
    if not cur_list:
        return [{"role": "system", "content": get_sys_prompt()},
                {"role": "user", "content": message}]
    while len(cur_list) > max_size:
        cur_list.pop(0)
    cur_list[0] = {"role": "system", "content": get_sys_prompt()}
    cur_list.append({"role": "user", "content": message})
    return cur_list
```

### parse_command

Parses a given message to identify and execute commands, and returns the processed message along with a flag indicating whether the message is in "Question Mode".

**Parameters:**
- `message` (str): The input message to be parsed.
- `message_list` (list): A list of previous messages for context or processing.

**Returns:**
- `tuple[str, bool]`: A tuple containing:
  - The processed message as a string.
  - A boolean indicating whether the message is in "Question Mode".

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
        return list_to_str(split_message), True
    elif len(command[0]) == 3:
        func(list_to_str(split_message))
    elif func == paste:
        print('Ran command {} without arguments'.format(key))
        speak(command[1].split()[0])
        clipboard = str(paste())
        print(clipboard)
        message_list = get_message_list(message_list, 'AUTOMATED RESP