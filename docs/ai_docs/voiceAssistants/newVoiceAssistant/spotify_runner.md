# Documentation for src/voiceAssistants/newVoiceAssistant/spotify_runner.py

# Python Script Documentation

## Program Overview

The provided Python script is designed to interact with Spotify based on user prompts. It utilizes an AI model to interpret the user's request and perform corresponding Spotify actions such as playing, pausing, liking a song, adding a song to a playlist, and more.

## Table of Contents

- [do_spotify](#do_spotify)
  - Description: Perform Spotify actions based on the given prompt.
  - Parameters:
    - `prompt` (str): The prompt containing the action to perform.
  - Returns:
    - `bool`: True if the action was performed successfully, False otherwise.

## Detailed Function Descriptions

### do_spotify

**Description**: This function takes a user prompt, sends it to an AI model to interpret, and performs the corresponding Spotify action based on the AI's response.

**Parameters**:
- `prompt` (str): The prompt containing the action to perform.

**Returns**:
- `bool`: True if the action was performed successfully, False otherwise.

**Example Usage**:

```python
# Example usage of do_spotify function
prompt = "Play the song 'Shape of You' by Ed Sheeran."
do_spotify(prompt)
```

## Environment Variables

The script uses environment variables to configure the AI model settings. Ensure you have a `.env` file with the following variables:

- `AI_TOKEN`: The API token for the AI model.
- `AI_MODEL`: The model name to be used.
- `AI_URL`: The URL of the AI service.

## Dependencies

The script relies on several external libraries and modules. Ensure you have the following dependencies installed:

- `helper`
- `pyWrkspPackage`
- `spotify_actions`
- `actions`
- `time`
- `dotenv`
- `os`

## Example Usage

Here is an example of how to use the script:

```python
from helper import *
from pyWrkspPackage import ai_response, load_from_file
from spotify_actions import *
from actions import play, pause
from time import sleep
from dotenv import load_dotenv
from os import getenv

load_dotenv()
AI_KEY = getenv('AI_TOKEN')
AI_MODEL = getenv('AI_MODEL')
AI_URL = getenv('AI_URL')

def do_spotify(prompt: str) -> bool:
    """
    Perform Spotify actions based on the given prompt.

    Args:
        prompt (str): The prompt containing the action to perform.

    Returns:
        bool: True if the action was performed successfully, False otherwise.
    """
    messages = [{"role": "system", "content": load_from_file('spotify_prompt.md').format(list_user_playlists(), get_currently_playing()['track_name'] if get_currently_playing() else 'Nothing is playing right now')},
                {"role": "user", "content": prompt}]

    response, _ = ai_response(messages, AI_MODEL, AI_URL, AI_KEY)
    if response is None:
        return False

    device = get_active_device()
    if device is None:
        play()
        while device is None:
            device = get_active_device()
            sleep(0.5)
        pause()

    print(response)

    if "stop-playback" in response:
        stop_playback(device)
    elif "like-song" in response:
        like_song(get_currently_playing()['track_id'])
    elif "play-song" in response:
        uri, _ = find_track(response.split('play-song')[1].strip())
        play_item(uri, device)
    elif "playlistadd" in response:
        playlist_name = response.split('playlistadd')[1].strip()
        song_uri = get_currently_playing()['track_uri']
        add_track_to_playlist(song_uri, playlist_name)
    elif "playlist" in response:
        uri, _ = find_playlist_fuzzy(response.split('playlist')[1].strip())
        play_item(uri, device)

if __name__ == "__main__":
    # Example usage
    print('Ready')
    prompt = input()
    do_spotify(prompt)
```

This documentation provides a comprehensive overview of the script, including function descriptions, parameters, return values, and example usage. Make sure to set up the required environment variables and dependencies before running the script.