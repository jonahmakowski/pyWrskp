# Documentation for src/helpfulPackage/app/pyWrkspPackage/audio.py

# Python Script Documentation

## Program Overview

The provided Python script is designed to perform voice recognition and text-to-speech functionalities. It uses the `speech_recognition` library to capture and recognize voice commands, the `whisper` library to transcribe audio, and the `pyttsx3` library to convert text to speech. The `pygame` mixer module is used to play sound files.

## Table of Contents

- [take_command](#take_command)
  - Description: Listens for a voice command and returns the recognized text.
  - Parameters: None
  - Returns: The recognized text from the audio input.

- [play_sound](#play_sound)
  - Description: Play a sound file using the mixer module.
  - Parameters:
    - `hold` (bool): If True, the function will block until the sound finishes playing.
    - `sound` (str, optional): The path to the sound file to play. Defaults to 'audio/audio.mp3'.
  - Returns: None

- [speak](#speak)
  - Description: Convert text to speech and play it through the speakers.
  - Parameters:
    - `message` (str): The text message to be spoken.
    - `voice` (int, optional): The index of the voice to use. Defaults to 132.
  - Returns: None

## Detailed Function Descriptions

### take_command

**Description**: Listens for a voice command and returns the recognized text.

**Parameters**: None

**Returns**: The recognized text from the audio input.

```python
def take_command() -> str:
    """
    Listens for a voice command and returns the recognized text.

    This function uses the `speech_recognition` library to capture audio from the microphone,
    then processes the audio to recognize and return the spoken text.

    Returns:
        str: The recognized text from the audio input.
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 2
        audio = r.listen(source)

    print("Recognizing...")
    with open("temp_audio.wav", "wb") as f:
        f.write(audio.get_wav_data())
    transcription = model.transcribe("temp_audio.wav")['text']
    remove("temp_audio.wav")

    return transcription
```

### play_sound

**Description**: Play a sound file using the mixer module.

**Parameters**:
- `hold` (bool): If True, the function will block until the sound finishes playing.
- `sound` (str, optional): The path to the sound file to play. Defaults to 'audio/audio.mp3'.

**Returns**: None

```python
def play_sound(hold: bool, sound='audio/audio.mp3') -> None:
    """
    Play a sound file using the mixer module.

    Args:
        hold (bool): If True, the function will block until the sound finishes playing.
        sound (str, optional): The path to the sound file to play. Defaults to 'audio/audio.mp3'.
    """
    mixer.music.load(sound)
    mixer.music.play()
    if hold:
        while mixer.music.get_busy():
            sleep(0.001)
```

### speak

**Description**: Convert text to speech and play it through the speakers.

**Parameters**:
- `message` (str): The text message to be spoken.
- `voice` (int, optional): The index of the voice to use. Defaults to 132.

**Returns**: None

```python
def speak(message: str, voice=132, hold=True) -> None:
    """
    Convert text to speech and play it through the speakers.

    Args:
        message (str): The text message to be spoken.
        voice (int, optional): The index of the voice to use. Defaults to 132.
    """
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[voice].id)  # Changing index changes voices
    engine.say(message)
    engine.runAndWait()
```

## Example Usage

### Usage of `take_command`

```python
command = take_command()
print(f"Recognized command: {command}")
```

### Usage of `play_sound`

```python
play_sound(hold=True, sound='path/to/your/sound.mp3')
```

### Usage of `speak`

```python
speak("Hello, how can I assist you today?", voice=132)
```