import json
import spotipy
from dotenv import load_dotenv
from os import getenv

load_dotenv()
username = getenv("SPOTIFY_USERNAME")
clientID = getenv("SPOTIFY_CLIENT_ID")
clientSecret = getenv("SPOTIFY_CLIENT_SECRET")
redirect_uri = "https://google.com/callback/"
oauth_object = spotipy.SpotifyOAuth(
    clientID,
    clientSecret,
    redirect_uri,
    scope="user-modify-playback-state,user-read-playback-state",
)
token_dict = oauth_object.get_access_token()
token = token_dict["access_token"]
spotifyObject = spotipy.Spotify(auth=token)
user_name = spotifyObject.current_user()


def play_song(search_song: str) -> None:
    results = spotifyObject.search(search_song, 1, 0, "track")
    songs_dict = results["tracks"]
    song_items = songs_dict["items"]
    song_uri = song_items[0]["uri"]

    # Get available devices and set the first one as active
    try:
        devices = spotifyObject.devices()
        if devices["devices"]:
            active_device_id = devices["devices"][0]["id"]
            spotifyObject.transfer_playback(device_id=active_device_id, force_play=True)
            spotifyObject.start_playback(uris=[song_uri])
            print("Song is now playing on your computer.")
        else:
            print("No active devices found. Please open Spotify on a device.")
    except spotipy.exceptions.SpotifyException:
        print("Error, but I think it worked")
