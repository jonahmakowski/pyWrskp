# Documentation for src/voiceAssistants/newVoiceAssistant/main.py

# Voice Assistant Script Documentation

This Python script implements a voice-activated assistant that listens for specific keywords, processes voice commands, and performs corresponding actions. The script utilizes various libraries for audio processing, speech recognition, and text-to-speech conversion.

## Table of Contents

- [Function 1](#play_sound)
    - Description: Plays a sound from 'audio.mp3'.
    - Parameters: `hold (bool)` - If True, the function will block until the sound finishes playing.
    - Returns: None.

- [Function 2](#take_command)
    - Description: Listens for a voice command and returns the recognized text.
    - Parameters: None.
    - Returns: `str` - The recognized text from the audio input.

- [Function 3](#get_message_list)
    - Description: Updates the message list with a new user message.
    - Parameters: `cur_list (list)`, `message (str)`, `max_size (int, optional)`.
    - Returns: `list` - The updated message list.

- [Function 4](#speak)
    - Description: Converts text to speech and plays it through the speakers.
    - Parameters: `message (str)`, `voice (int, optional)`.
    - Returns: None.

- [Function 5](#parse_command)
    - Description: Parses a command message and executes the corresponding action.
    - Parameters: `message (str)`.
    - Returns: `tuple[str, bool]` - The remaining message and a boolean indicating if it's in question mode.

- [Function 6](#main)
    - Description: The main function that runs the assistant.
    - Parameters: None.
    - Returns: None.

## Detailed Function Descriptions

### play_sound

**Description**: Plays a sound from 'audio.mp3'.

**Parameters**:
    *   `hold (bool)`: If True, the function will block until the sound finishes playing.

**Returns**: None.

### take_command

**Description**: Listens for a voice command and returns the recognized text.

This function uses the `speech_recognition` library to capture audio from the microphone, then processes the audio to recognize and return the spoken text.

**Parameters**: None.

**Returns**: `str` - The recognized text from the audio input.

### get_message_list

**Description**: Updates the message list with a new user message.

**Parameters**:
    *   `cur_list (list)`: The current list of messages.
    *   `message (str)`: The new user message to add.
    *   `max_size (int, optional)`: The maximum size of the message list. Defaults to 10.

**Returns**: `list` - The updated message list.

### speak

**Description**: Converts text to speech and plays it through the speakers.

**Parameters**:
    *   `message (str)`: The text message to be spoken.
    *   `voice (int, optional)`: The index of the voice to use. Defaults to 132.

**Returns**: None.

### parse_command

**Description**: Parses a command message and executes the corresponding action.

**Parameters**:
    *   `message (str)`: The command message to parse.

**Returns**: `tuple[str, bool]` - The remaining message and a boolean indicating if it's in question mode.

### main

**Description**: The main function that runs the assistant.

**Parameters**: None.

**Returns**: None.

## Example Usage

### play_sound

Usage example for `play_sound`:

```python
play_sound(hold=True)
```

### take_command

Usage example for `take_command`:

```python
command = take_command()
print(f"Recognized command: {command}")
```

### get_message_list

Usage example for `get_message_list`:

```python
message_list = get_message_list([], "Hello, how can I help you?", max_size=10)
print(message_list)
```

### speak

Usage example for `speak`:

```python
speak("Hello, this is a test message.", voice=132)
```

### parse_command

Usage example for `parse_command`:

```python
remaining_message, question_mode = parse_command("open-app$Google Chrome")
print(f"Remaining message: {remaining_message}, Question mode: {question_mode}")
```

### main

Usage example for `main`:

```python
if __name__ == '__main__':
    main()
```

This documentation provides a comprehensive overview of the functions and their usage within the voice assistant script.