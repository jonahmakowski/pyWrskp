# Documentation for src/voiceAssistants/newVoiceAssistant/main.py

# Python Script Documentation

## Program Overview

The provided Python script is designed to create a voice-activated assistant that can perform various tasks based on voice commands. The assistant uses speech recognition to listen for commands, processes these commands using an AI model, and executes corresponding actions. The script integrates several libraries and modules to handle audio playback, speech recognition, and AI responses.

## Table of Contents

- [Function 1](#play_sound)
    - Description: Play a sound file using the mixer module.
    - Parameters: `hold (bool)`, `sound (str, optional)`
    - Returns: None
- [Function 2](#take_command)
    - Description: Listens for a voice command and returns the recognized text.
    - Parameters: None
    - Returns: `str`
- [Function 3](#get_message_list)
    - Description: Update the message list with a new user message.
    - Parameters: `cur_list (list)`, `message (str)`, `max_size (int, optional)`
    - Returns: `list`
- [Function 4](#speak)
    - Description: Convert text to speech and play it through the speakers.
    - Parameters: `message (str)`, `voice (int, optional)`, `hold (bool, optional)`
    - Returns: None
- [Function 5](#parse_command)
    - Description: Parse the command and execute the corresponding action.
    - Parameters: `message (str)`, `message_list (list)`
    - Returns: `tuple[str, bool]`
- [Function 6](#main)
    - Description: Main function to run the voice-activated assistant.
    - Parameters: None
    - Returns: None

## Detailed Function Descriptions

### play_sound

Description: Play a sound file using the mixer module.

Parameters:
    - `hold (bool)`: If True, the function will block until the sound finishes playing.
    - `sound (str, optional)`: The path to the sound file to play. Defaults to 'audio.mp3'.

Returns: None

### take_command

Description: Listens for a voice command and returns the recognized text. This function uses the `speech_recognition` library to capture audio from the microphone, then processes the audio to recognize and return the spoken text.

Parameters: None

Returns: `str`: The recognized text from the audio input.

### get_message_list

Description: Update the message list with a new user message.

Parameters:
    - `cur_list (list)`: The current list of messages.
    - `message (str)`: The new user message to add.
    - `max_size (int, optional)`: The maximum size of the message list. Defaults to 10.

Returns: `list`: The updated message list.

### speak

Description: Convert text to speech and play it through the speakers.

Parameters:
    - `message (str)`: The text message to be spoken.
    - `voice (int, optional)`: The index of the voice to use. Defaults to 132.
    - `hold (bool, optional)`: If True, the function will block until the speech finishes. Defaults to True.

Returns: None

### parse_command

Description: Parse the command and execute the corresponding action.

Parameters:
    - `message (str)`: The command message to parse.
    - `message_list (list)`: The current list of messages.

Returns: `tuple[str, bool]`: A tuple containing the processed message and a boolean indicating if the assistant is in question mode.

### main

Description: Main function to run the voice-activated assistant.

Parameters: None

Returns: None

## Example Usage

### Example Usage for `play_sound`

```python
# Play a sound file and wait until it finishes
play_sound(hold=True, sound='bootup.mp3')
```

### Example Usage for `take_command`

```python
# Listen for a voice command and print the recognized text
command = take_command()
print(command)
```

### Example Usage for `get_message_list`

```python
# Update the message list with a new user message
message_list = get_message_list([], "Hello, how can I help you?")
print(message_list)
```

### Example Usage for `speak`

```python
# Convert text to speech and play it through the speakers
speak("Hello, Jonah. How can I assist you today?")
```

### Example Usage for `parse_command`

```python
# Parse a command and execute the corresponding action
message_list = []
response, question_mode = parse_command("open-app$Google Chrome", message_list)
print(response)
print(question_mode)
```

### Example Usage for `main`

```python
# Run the voice-activated assistant
if __name__ == '__main__':
    main()
```

