# Documentation for src/voiceAssistants/newVoiceAssistant/helper.py

# Python Script Documentation

This document provides a comprehensive overview of the provided Python script, which includes functionalities for voice command recognition, sound playback, and text-to-speech conversion. The script utilizes several libraries such as `whisper`, `pyttsx3`, `pygame`, `speech_recognition`, and `os`.

## Table of Contents

- [Function 1: `take_command`](#function-1-take_command)
  - Description: Listens for a voice command and returns the recognized text.
  - Parameters: None.
  - Returns: Recognized text from the audio input.

- [Function 2: `play_sound`](#function-2-play_sound)
  - Description: Plays a sound file using the mixer module.
  - Parameters: `hold` (bool), `sound` (str, optional).
  - Returns: None.

- [Function 3: `speak`](#function-3-speak)
  - Description: Converts text to speech and plays it through the speakers.
  - Parameters: `message` (str), `voice` (int, optional).
  - Returns: None.

## Detailed Function Descriptions

### Function 1: `take_command`

**Description:** This function listens for a voice command and returns the recognized text. It uses the `speech_recognition` library to capture audio from the microphone and then processes the audio to recognize and return the spoken text.

**Parameters:** None.

**Returns:** The recognized text from the audio input.

### Example Usage

```python
command = take_command()
print(f"Recognized command: {command}")
```

### Function 2: `play_sound`

**Description:** This function plays a sound file using the mixer module. It can either play the sound in the background or block until the sound finishes playing.

**Parameters:**
- `hold` (bool): If True, the function will block until the sound finishes playing.
- `sound` (str, optional): The path to the sound file to play. Defaults to 'audio.mp3'.

**Returns:** None.

### Example Usage

```python
play_sound(hold=True, sound='notification.mp3')
```

### Function 3: `speak`

**Description:** This function converts text to speech and plays it through the speakers. It allows for selecting different voices.

**Parameters:**
- `message` (str): The text message to be spoken.
- `voice` (int, optional): The index of the voice to use. Defaults to 132.

**Returns:** None.

### Example Usage

```python
speak("Hello, how can I assist you today?", voice=132)
```

## Additional Setup

Before using the functions, ensure the following setup is done:

```python
from os import remove
import whisper
import pyttsx3
from pygame import mixer
from time import sleep
import speech_recognition as sr

# Setting up Audio Systems
mixer.init()  # mp3 player init
engine = pyttsx3.init()  # text to speech init
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
model = whisper.load_model('base.en')  # Whisper model init
```

This setup initializes the necessary audio systems and loads the Whisper model for voice recognition.

---

This documentation should help users understand how to use the provided script effectively. If you have any further questions or need additional assistance, please feel free to ask!