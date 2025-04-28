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
    model = 'mistral-large-latest'
    url = 'http://192.168.86.4:4001'
    do_spotify(prompt, model, url)
