# Documentation for src/voiceAssistants/newVoiceAssistant/spotify_actions.py

# Spotify Controller Script Documentation

## Overview

This Python script provides a command-line interface (CLI) to control Spotify playback, manage playlists, and interact with user's Spotify library. It leverages the `spotipy` library for Spotify API interactions and `thefuzz` for fuzzy matching of track and playlist names.

## Table of Contents

- [Configuration and Authentication](#configuration-and-authentication)
- [Helper Functions](#helper-functions)
  - [find_track](#find_track)
  - [find_playlist_fuzzy](#find_playlist_fuzzy)
  - [list_user_playlists](#list_user_playlists)
  - [get_active_device](#get_active_device)
  - [play_item](#play_item)
  - [stop_playback](#stop_playback)
  - [like_song](#like_song)
  - [add_track_to_playlist](#add_track_to_playlist)
- [Main Command Loop](#main-command-loop)
  - [run_cli](#run_cli)
- [Example Usage](#example-usage)

## Configuration and Authentication

### Environment Variables

The script uses environment variables for configuration. Ensure you have a `.env` file with the following variables:

- `SPOTIPY_CLIENT_ID`: Your Spotify API client ID.
- `SPOTIPY_CLIENT_SECRET`: Your Spotify API client secret.
- `SPOTIPY_REDIRECT_URI`: The redirect URI for Spotify authentication (should be `http://localhost:8888/callback`).

### Authentication

The script authenticates using Spotify's OAuth flow. It checks if the redirect URI is set correctly and prints a warning if not.

```python
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
if redirect_uri != 'http://localhost:8888/callback':
    print("Warning: Make sure SPOTIPY_REDIRECT_URI in your .env file is set to 'http://localhost:8888/callback'.")

try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))
    user_info = sp.current_user()
    print(f"--- Authenticated as {user_info['display_name']} ({user_info['id']}) ---")
    print("--- Spotify Controller Ready ---")
except Exception as e:
    print(f"Error during authentication: {e}")
    print("Please check your .env file and Spotify Developer Dashboard settings.")
    sys.exit(1)
```

## Helper Functions

### find_track

Searches for a track and returns its URI and ID.

**Parameters:**
- `name` (str): The name of the track to search for.

**Returns:**
- `tuple`: A tuple containing the track URI and ID, or `(None, None)` if not found.

```python
def find_track(name):
    try:
        results = sp.search(q=name, type='track', limit=1)
        items = results['tracks']['items']
        if items:
            track = items[0]
            track_name = track['name']
            artist_names = ', '.join(artist['name'] for artist in track['artists'])
            print(f"Found track: '{track_name}' by {artist_names}")
            return track['uri'], track['id']
        else:
            print(f"Track '{name}' not found.")
            return None, None
    except spotipy.exceptions.SpotifyException as e:
        print(f"Error searching for track: {e}")
        return None, None
```

### find_playlist_fuzzy

Searches within the user's playlists using fuzzy matching and returns the best match's URI and ID.

**Parameters:**
- `name` (str): The name of the playlist to search for.
- `similarity_threshold` (int, optional): The minimum similarity score for a match. Defaults to 75.

**Returns:**
- `tuple`: A tuple containing the playlist URI and ID, or `(None, None)` if not found.

```python
def find_playlist_fuzzy(name, similarity_threshold=75):
    print(f"Fuzzy searching for playlist matching '{name}'...")
    try:
        all_playlists = []
        offset = 0
        limit = 50
        while True:
            results = sp.current_user_playlists(limit=limit, offset=offset)
            if not results or not results['items']:
                break
            all_playlists.extend(results['items'])
            if results['next']:
                offset += limit
            else:
                break

        if not all_playlists:
             print("You don't seem to have any playlists.")
             return None, None

        user_playlists = [p for p in all_playlists if p['owner']['id'] == user_info['id']]
        other_playlists = [p for