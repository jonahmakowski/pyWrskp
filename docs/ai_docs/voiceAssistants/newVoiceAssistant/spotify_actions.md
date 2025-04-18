# Documentation for src/voiceAssistants/newVoiceAssistant/spotify_actions.py

# Spotify Controller Script Documentation

This Python script is designed to interact with the Spotify Web API using the Spotipy library. It provides various functionalities such as retrieving the currently playing track, searching for tracks and playlists, listing user playlists, controlling playback, and more.

## Table of Contents

* [Configuration and Authentication](#configuration-and-authentication)
* [Helper Functions](#helper-functions)
    * [get_currently_playing](#get_currently_playing)
    * [find_track](#find_track)
    * [find_playlist_fuzzy](#find_playlist_fuzzy)
    * [list_user_playlists](#list_user_playlists)
    * [get_active_device](#get_active_device)
    * [play_item](#play_item)
    * [stop_playback](#stop_playback)
    * [like_song](#like_song)
    * [add_track_to_playlist](#add_track_to_playlist)

## Configuration and Authentication

The script starts by loading environment variables from a `.env` file using the `dotenv` library. It then sets up the necessary scopes for the Spotify API and checks if the redirect URI is set correctly. The script uses the `SpotifyOAuth` flow to authenticate the user and create a Spotipy client object.

## Helper Functions

### get_currently_playing

**Description:** Retrieves information about the currently playing track on Spotify.

**Parameters:** None

**Returns:** A dictionary containing details about the currently playing track, or an empty dictionary if no track is playing or an error occurs.

**Example Usage:**

```python
current_track = get_currently_playing()
if current_track:
    print(f"Currently playing: {current_track['track_name']} by {current_track['artist_name']}")
else:
    print("No track is currently playing.")
```

### find_track

**Description:** Searches for a track on Spotify by its name and returns its URI and ID.

**Parameters:**
* `name` (str): The name of the track to search for.

**Returns:** A tuple containing the track's URI and ID if found, or `(None, None)` if not found or an error occurs.

**Example Usage:**

```python
track_uri, track_id = find_track("Shape of You")
if track_uri:
    print(f"Found track: {track_uri}")
else:
    print("Track not found.")
```

### find_playlist_fuzzy

**Description:** Performs a fuzzy search to find a Spotify playlist matching the given name.

**Parameters:**
* `name` (str): The name of the playlist to search for.
* `similarity_threshold` (int, optional): The minimum similarity score (0-100) required for a match. Defaults to 75.

**Returns:** A tuple containing the URI and ID of the matched playlist, or `(None, None)` if no match is found or an error occurs.

**Example Usage:**

```python
playlist_uri, playlist_id = find_playlist_fuzzy("My Favorite Songs")
if playlist_uri:
    print(f"Found playlist: {playlist_uri}")
else:
    print("Playlist not found.")
```

### list_user_playlists

**Description:** Fetches the current user's Spotify playlists.

**Parameters:** None

**Returns:** A list of dictionaries, where each dictionary contains the name and owner of a playlist.

**Example Usage:**

```python
playlists = list_user_playlists()
for playlist in playlists:
    print(f"Playlist: {playlist['name']} by {playlist['user']}")
```

### get_active_device

**Description:** Retrieves the active Spotify device ID or the first available device ID if no active device is found.

**Parameters:** None

**Returns:** The ID of the active Spotify device, the first available device, or `None` if no devices are found.

**Example Usage:**

```python
device_id = get_active_device()
if device_id:
    print(f"Active device ID: {device_id}")
else:
    print("No active device found.")
```

### play_item

**Description:** Plays a Spotify track or playlist on a specified device.

**Parameters:**
* `uri` (str): The Spotify URI of the item to play. This can be a track or playlist URI.
* `device_id` (str): The Spotify device ID where playback should occur.

**Returns:** None

**Example Usage:**

```python
play_item("spotify:track:4uLU6hMCjMI75M1A2tKUQC", "device_id")
```

### stop_playback

**Description:** Stops playback on the specified Spotify device.

**Parameters:**
* `device_id` (str): The unique identifier of the Spotify device where playback should be stopped.

**Returns:** None

**Example Usage:**

```python
stop_playback("device_id")
```

### like