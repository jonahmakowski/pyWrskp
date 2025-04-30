# Documentation for src/voiceAssistants/newVoiceAssistant/helper.py

# Python Script Documentation

## Program Overview

This Python script is designed to facilitate voice command recognition, text-to-speech conversion, and audio playback. It leverages the `whisper` library for speech recognition, `pyttsx3` for text-to-speech conversion, and `pygame` for playing sound files. The script includes functions to capture voice commands, play sound files, and convert text to speech.

## Table of Contents

- [take_command](#take_command)
  - Description: Listens for a voice command and returns the recognized text.
  - Returns: The recognized text from the audio input.

- [play_sound](#play_sound)
  - Description: Plays a sound file using the mixer module.
  - Parameters: `hold` (bool), `sound` (str, optional)
  - Returns: None

- [speak](#speak)
  - Description: Converts text to speech and plays it through the speakers.
  - Parameters: `message` (str), `voice` (int, optional)
  - Returns: None

- [ai_weather_display](#ai_weather_display)
  - Description: Formats and displays weather data in a readable string format.
  - Parameters: `data` (dict)
  - Returns: A formatted string displaying the current weather and forecast details for each date.

## Detailed Function Descriptions

### take_command

**Description**: Listens for a voice command and returns the recognized text. This function uses the `speech_recognition` library to capture audio from the microphone, then processes the audio to recognize and return the spoken text.

**Parameters**: None

**Returns**: The recognized text from the audio input.

**Example Usage**:
```python
command = take_command()
print(f"Recognized command: {command}")
```

### play_sound

**Description**: Plays a sound file using the mixer module.

**Parameters**:
- `hold` (bool): If True, the function will block until the sound finishes playing.
- `sound` (str, optional): The path to the sound file to play. Defaults to 'audio/audio.mp3'.

**Returns**: None

**Example Usage**:
```python
play_sound(hold=True, sound='audio/notification.mp3')
```

### speak

**Description**: Converts text to speech and plays it through the speakers.

**Parameters**:
- `message` (str): The text message to be spoken.
- `voice` (int, optional): The index of the voice to use. Defaults to 132.

**Returns**: None

**Example Usage**:
```python
speak("Hello, how can I assist you today?", voice=132)
```

### ai_weather_display

**Description**: Formats and displays weather data in a readable string format.

**Parameters**:
- `data` (dict): A dictionary containing weather information. Expected keys:
  - `current_temp` (str): The current temperature.
  - `current_weather` (str): The current weather condition.
  - Other keys representing dates (str), where each date maps to a dictionary with:
    - `daily_temps` (float): The maximum temperature for the date in °C.
    - `daily_low_temps` (float): The minimum temperature for the date in °C.
    - `daily_precipitation` (float): The precipitation percentage for the date.
    - `daily_avg_temp` (float): The average temperature for the date in °C.

**Returns**: A formatted string displaying the current weather and forecast details for each date.

**Example Usage**:
```python
weather_data = {
    'current_temp': '20°C',
    'current_weather': 'Sunny',
    '2023-10-01': {
        'daily_temps': 25.0,
        'daily_low_temps': 15.0,
        'daily_precipitation': 10.0,
        'daily_avg_temp': 20.0
    }
}
formatted_weather = ai_weather_display(weather_data)
print(formatted_weather)
```

## Example Usage

Here is an example of how to use the functions in the script:

```python
# Capture a voice command
command = take_command()
print(f"Recognized command: {command}")

# Play a sound file
play_sound(hold=True, sound='audio/notification.mp3')

# Convert text to speech
speak("Hello, how can I assist you today?", voice=132)

# Display weather data
weather_data = {
    'current_temp': '20°C',
    'current_weather': 'Sunny',
    '2023-10-01': {
        'daily_t