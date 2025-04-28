# Documentation for src/voiceAssistants/newVoiceAssistant/helper.py

# Python Script Documentation

## Program Overview

The provided Python script is designed to capture voice commands, play sound files, and convert text to speech. This script utilizes several libraries to achieve these functionalities, including `whisper`, `pyttsx3`, `pygame`, and `speech_recognition`. The script also includes a function to format and display weather data.

## Table of Contents

- [take_command](#take_command)
  - Description: Listens for a voice command and returns the recognized text.
  - Parameters: None
  - Returns: The recognized text from the audio input.
- [play_sound](#play_sound)
  - Description: Play a sound file using the mixer module.
  - Parameters:
    - `hold` (bool): If True, the function will block until the sound finishes playing.
    - `sound` (str, optional): The path to the sound file to play. Defaults to 'audio.mp3'.
  - Returns: None
- [speak](#speak)
  - Description: Convert text to speech and play it through the speakers.
  - Parameters:
    - `message` (str): The text message to be spoken.
    - `voice` (int, optional): The index of the voice to use. Defaults to 132.
  - Returns: None
- [ai_weather_display](#ai_weather_display)
  - Description: Formats and displays weather data in a readable string format.
  - Parameters:
    - `data` (dict): A dictionary containing weather information.
  - Returns: A formatted string displaying the current weather and forecast details for each date.

## Detailed Function Descriptions

### take_command

**Description:** Listens for a voice command and returns the recognized text.

**Parameters:** None

**Returns:** The recognized text from the audio input.

**Example Usage:**

```python
command = take_command()
print(f"Recognized Command: {command}")
```

### play_sound

**Description:** Play a sound file using the mixer module.

**Parameters:**
- `hold` (bool): If True, the function will block until the sound finishes playing.
- `sound` (str, optional): The path to the sound file to play. Defaults to 'audio.mp3'.

**Returns:** None

**Example Usage:**

```python
play_sound(hold=True, sound='audio.mp3')
```

### speak

**Description:** Convert text to speech and play it through the speakers.

**Parameters:**
- `message` (str): The text message to be spoken.
- `voice` (int, optional): The index of the voice to use. Defaults to 132.

**Returns:** None

**Example Usage:**

```python
speak("Hello, how can I assist you today?", voice=132)
```

### ai_weather_display

**Description:** Formats and displays weather data in a readable string format.

**Parameters:**
- `data` (dict): A dictionary containing weather information. Expected keys:
  - `current_temp` (str): The current temperature.
  - `current_weather` (str): The current weather condition.
  - Other keys representing dates (str), where each date maps to a dictionary with:
    - `max_temp` (float): The maximum temperature for the date in °C.
    - `min_temp` (float): The minimum temperature for the date in °C.
    - `precipitation` (float): The precipitation percentage for the date.
    - `avg_temp` (float): The average temperature for the date in °C.

**Returns:** A formatted string displaying the current weather and forecast details for each date.

**Example Usage:**

```python
weather_data = {
    'current_temp': '20°C',
    'current_weather': 'Sunny',
    '2023-10-01': {
        'daily_temps': 25.0,
        'daily_low_temps': 15.0,
        'daily_precipitation': 10.0,
        'daily_avg_temp': 20.0
    },
    '2023-10-02': {
        'daily_temps': 22.0,
        'daily_low_temps': 14.0,
        'daily_precipitation': 20.0,
        'daily_avg_temp': 18.0
    }
}

formatted_weather = ai_weather_display(weather_data)
print(formatted_weather)
```

This documentation provides a comprehensive overview of the script's functionalities, including detailed descriptions of each function and examples of how to use them.