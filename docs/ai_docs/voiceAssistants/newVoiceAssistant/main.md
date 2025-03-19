# Documentation for src/voiceAssistants/newVoiceAssistant/main.py

# Voice Assistant Script Documentation

## Program Overview

This Python script implements a voice assistant that listens for a wake word, captures voice commands, processes them using an AI model, and performs corresponding actions. The script leverages various libraries for audio processing, text-to-speech, and AI interaction.

## Table of Contents

- [Function 1](#play_sound)
    - Description: Play a sound file using the mixer module.
    - Parameters: `hold` (bool), `sound` (str, optional)
    - Returns: None

- [Function 2](#take_command)
    - Description: Listens for a voice command and returns the recognized text.
    - Parameters: None
    - Returns: str

- [Function 3](#get_message_list)
    - Description: Update the message list with a new user message.
    - Parameters: `cur_list` (list), `message` (str), `max_size` (int, optional)
    - Returns: list

- [Function 4](#speak)
    - Description: Convert text to speech and play it through the speakers.
    - Parameters: `message` (str), `voice` (int, optional)
    - Returns: None

- [Function 5](#parse_command)
    - Description: Parse the command from the message and execute the corresponding action.
    - Parameters: `message` (str), `message_list` (list)
    - Returns: tuple[str, bool]

- [Function 6](#main)
    - Description: The main function to run the voice assistant.
    - Parameters: None
    - Returns: None

## Detailed Function Descriptions

### play_sound

**Description:** Play a sound file using the mixer module.

**Parameters:**
- `hold` (bool): If True, the function will block until the sound finishes playing.
- `sound` (str, optional): The path to the sound file to play. Defaults to 'audio.mp3'.

**Returns:** None

### take_command

**Description:** Listens for a voice command and returns the recognized text.

This function uses the `speech_recognition` library to capture audio from the microphone, then processes the audio to recognize and return the spoken text.

**Parameters:** None

**Returns:** str: The recognized text from the audio input.

### get_message_list

**Description:** Update the message list with a new user message.

**Parameters:**
- `cur_list` (list): The current list of messages.
- `message` (str): The new user message to add.
- `max_size` (int, optional): The maximum size of the message list. Defaults to 10.

**Returns:** list: The updated message list.

### speak

**Description:** Convert text to speech and play it through the speakers.

**Parameters:**
- `message` (str): The text message to be spoken.
- `voice` (int, optional): The index of the voice to use. Defaults to 132.

**Returns:** None

### parse_command

**Description:** Parse the command from the message and execute the corresponding action.

**Parameters:**
- `message` (str): The message containing the command.
- `message_list` (list): The current list of messages.

**Returns:** tuple[str, bool]: The remaining message and a boolean indicating if the assistant is in question mode.

### main

**Description:** The main function to run the voice assistant.

**Parameters:** None

**Returns:** None

## Example Usage

### Example Usage for `play_sound`

```python
# Play a sound file and block until it finishes
play_sound(True, 'bootup.mp3')
```

### Example Usage for `take_command`

```python
# Capture a voice command and print the recognized text
command = take_command()
print(command)
```

### Example Usage for `get_message_list`

```python
# Update the message list with a new user message
message_list = get_message_list([], "Hello, how are you?")
print(message_list)
```

### Example Usage for `speak`

```python
# Convert text to speech and play it through the speakers
speak("Hello, this is a test message.")
```

### Example Usage for `parse_command`

```python
# Parse a command from the message and execute the corresponding action
message = "open-app$notepad"
message_list = []
result, question_mode = parse_command(message, message_list)
print(result, question_mode)
```

### Example Usage for `main`

```python
# Run the voice assistant
if __name__ == '__main__':
    main()
```

This documentation provides a comprehensive overview of the functions and classes in the script, along with examples of how to use them.