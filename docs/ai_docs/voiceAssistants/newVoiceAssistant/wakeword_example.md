# Documentation for src/voiceAssistants/newVoiceAssistant/wakeword_example.py

# Porcupine Keyword Detection Script

## Program Overview

This Python script utilizes the Porcupine library to detect specific keywords in real-time audio input. The script is designed to listen for predefined keywords and print a message when a keyword is detected. This can be useful for various applications such as voice-activated commands or wake-word detection.

## Table of Contents

- [Porcupine Initialization](#porcupine-initialization)
- [Recorder Initialization](#recorder-initialization)
- [Main Loop](#main-loop)
- [Exception Handling](#exception-handling)
- [Resource Cleanup](#resource-cleanup)

## Detailed Function Descriptions

### Porcupine Initialization

The Porcupine library is initialized with an access key and a list of keywords. This setup allows the script to detect the specified keywords in the audio input.

```python
porcupine = pvporcupine.create(access_key=access_key, keywords=keywords)
```

**Parameters:**
- `access_key` (str): The API key required to access the Porcupine service.
- `keywords` (list): A list of keywords that the script will detect.

**Returns:**
- `porcupine`: An instance of the Porcupine keyword detection engine.

### Recorder Initialization

The `PvRecorder` class is used to capture audio input from the microphone. The recorder is configured to match the frame length required by the Porcupine engine.

```python
recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)
```

**Parameters:**
- `device_index` (int): The index of the audio input device. `-1` indicates the default device.
- `frame_length` (int): The frame length required by the Porcupine engine.

**Returns:**
- `recoder`: An instance of the `PvRecorder` class.

### Main Loop

The main loop continuously reads audio input and processes it using the Porcupine engine. If a keyword is detected, a message is printed.

```python
try:
    recoder.start()

    while True:
        keyword_index = porcupine.process(recoder.read())
        if keyword_index >= 0:
            print(f"Detected {keywords[keyword_index]}")
```

**Parameters:**
- None

**Returns:**
- None

### Exception Handling

The script includes exception handling to ensure that the recorder stops gracefully if a `KeyboardInterrupt` is detected.

```python
except KeyboardInterrupt:
    recoder.stop()
```

**Parameters:**
- None

**Returns:**
- None

### Resource Cleanup

The script ensures that the Porcupine engine and recorder are properly deleted to free up resources.

```python
finally:
    porcupine.delete()
    recoder.delete()
```

**Parameters:**
- None

**Returns:**
- None

## Example Usage

Here is an example of how to use the script to detect the keyword "computer":

```python
import pvporcupine
from pvrecorder import PvRecorder

keywords = ['computer']
access_key = 'YOUR_API_KEY_HERE'

porcupine = pvporcupine.create(access_key=access_key, keywords=keywords)
recoder = PvRecorder(device_index=-1, frame_length=porcupine.frame_length)

try:
    recoder.start()

    while True:
        keyword_index = porcupine.process(recoder.read())
        if keyword_index >= 0:
            print(f"Detected {keywords[keyword_index]}")

except KeyboardInterrupt:
    recoder.stop()
finally:
    porcupine.delete()
    recoder.delete()
```

Replace `'YOUR_API_KEY_HERE'` with your actual Porcupine API key. The script will continuously listen for the keyword "computer" and print a message when it is detected.