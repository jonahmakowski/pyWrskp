import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import sys
from thefuzz import process, fuzz

# --- Configuration and Authentication ---

# Load environment variables from .env file
load_dotenv()

# Define the necessary scopes (no changes needed here)
SCOPE = (
    "user-read-playback-state "
    "user-modify-playback-state "
    "user-library-read "
    "user-library-modify "
    "playlist-read-private "
    "playlist-modify-private "
    "playlist-modify-public "
)

# Check if the redirect URI is set correctly
redirect_uri = os.getenv('SPOTIPY_REDIRECT_URI')
if redirect_uri != 'http://127.0.0.1:8888/callback':
    print("Warning: Make sure SPOTIPY_REDIRECT_URI in your .env file is set to 'http://127.0.0.1:8888/callback'.")

# Authenticate using SpotifyOAuth flow
try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPE))
    user_info = sp.current_user()
    print(f"--- Authenticated as {user_info['display_name']} ({user_info['id']}) ---")
    print("--- Spotify Controller Ready ---")
except Exception as e:
    print(f"Error during authentication: {e}")
    print("Please check your .env file and Spotify Developer Dashboard settings.")
    sys.exit(1)

# --- Helper Functions ---

def get_currently_playing() -> dict:
    """
    Retrieves information about the currently playing track on Spotify.

    This function uses the Spotify Web API to fetch details about the track
    currently being played on the user's active device. If no track is playing
    or an error occurs, an empty dictionary is returned.

    Returns:
        dict: A dictionary containing the following keys if a track is playing:
            - 'track_name' (str): The name of the track.
            - 'artist_name' (str): The name of the artist(s).
            - 'album_name' (str): The name of the album.
            - 'track_uri' (str): The Spotify URI of the track.
            - 'track_id' (str): The Spotify ID of the track.
            - 'is_playing' (bool): Whether the track is currently playing.
            - 'progress_ms' (int): The current playback position in milliseconds.
            - 'duration_ms' (int): The total duration of the track in milliseconds.
            Returns an empty dictionary if no track is playing or an error occurs.

    Notes:
        - Ensure that the `sp` object (Spotipy client) is properly authenticated before calling this function.
        - The user must have an active Spotify session for this function to return meaningful data.
    """
    try:
        current_playback = sp.current_playback()
        if not current_playback or not current_playback.get('item'):
            return {}

        track = current_playback['item']
        track_name = track['name']
        artist_name = ', '.join(artist['name'] for artist in track['artists'])
        album_name = track['album']['name']
        track_uri = track['uri']
        track_id = track['id']
        is_playing = current_playback['is_playing']
        progress_ms = current_playback['progress_ms']
        duration_ms = track['duration_ms']

        print(f"Currently playing: '{track_name}' by {artist_name} from the album '{album_name}'.")
        return {
            'track_name': track_name,
            'artist_name': artist_name,
            'album_name': album_name,
            'track_uri': track_uri,
            'track_id': track_id,
            'is_playing': is_playing,
            'progress_ms': progress_ms,
            'duration_ms': duration_ms
        }

    except spotipy.exceptions.SpotifyException as e:
        print(f"Error retrieving currently playing track: {e}")
        return {}


def find_track(name: str) -> tuple:
    """
    Searches for a track on Spotify by its name and returns its URI and ID.

    Args:
        name (str): The name of the track to search for.

    Returns:
        tuple: A tuple containing the track's URI and ID if found, or (None, None) if not found or an error occurs.

    Raises:
        spotipy.exceptions.SpotifyException: If an error occurs during the Spotify API request.

    Notes:
        - The function uses the global `sp` object to interact with the Spotify API.
        - If multiple tracks match the search query, only the first result is returned.
    """
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

def find_playlist_fuzzy(name:str, similarity_threshold=75) -> tuple:
    """
    Perform a fuzzy search to find a Spotify playlist matching the given name.

    This function retrieves all playlists associated with the current user, 
    separates them into user-created and other playlists, and performs a fuzzy 
    search to find the best match for the given playlist name. The search uses 
    a similarity threshold to determine acceptable matches.

    Args:
        name (str): The name of the playlist to search for.
        similarity_threshold (int, optional): The minimum similarity score (0-100) 
            required for a match. Defaults to 75.

    Returns:
        tuple: A tuple containing the URI and ID of the matched playlist. 
                Returns (None, None) if no match is found or an error occurs.

    Raises:
        spotipy.exceptions.SpotifyException: If an error occurs while interacting 
            with the Spotify API.

    Notes:
        - The function prioritizes user-created playlists over other playlists 
            when combining results.
        - The fuzzy search is case-insensitive and uses the `fuzz.WRatio` scorer 
            from the `fuzzywuzzy` library.
    """
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

        # Separate user-created playlists and other playlists
        user_playlists = [p for p in all_playlists if p['owner']['id'] == user_info['id']]
        other_playlists = [p for p in all_playlists if p['owner']['id'] != user_info['id']]

        # Create a mapping of playlist names (lowercase) to their details (uri, id)
        user_playlist_map = {p['name'].lower(): {'uri': p['uri'], 'id': p['id'], 'original_name': p['name']} for p in user_playlists}
        other_playlist_map = {p['name'].lower(): {'uri': p['uri'], 'id': p['id'], 'original_name': p['name']} for p in other_playlists}

        # Combine the maps, prioritizing user-created playlists
        combined_playlist_map = {**user_playlist_map, **other_playlist_map}
        playlist_names = list(combined_playlist_map.keys())

        # Use process.extractOne to find the best match above the threshold
        best_match = process.extractOne(
            name.lower(),
            playlist_names,
            scorer=fuzz.WRatio,
            score_cutoff=similarity_threshold
        )

        if best_match:
            matched_name_lower = best_match[0]
            score = best_match[1]
            playlist_details = combined_playlist_map[matched_name_lower]
            print(f"Best match found: '{playlist_details['original_name']}' (Score: {score}%)")
            return playlist_details['uri'], playlist_details['id']
        else:
            print(f"No playlist found matching '{name}' with similarity >= {similarity_threshold}%.")
            return None, None

    except spotipy.exceptions.SpotifyException as e:
        print(f"Error searching for playlist: {e}")
        return None, None

def list_user_playlists() -> list:
    """
    Fetches the current user's Spotify playlists.

    This function retrieves all playlists associated with the current Spotify user
    using the Spotify Web API. It handles pagination to ensure all playlists are fetched.

    Returns:
        list: A list of dictionaries, where each dictionary contains the following keys:
            - 'name' (str): The name of the playlist.
            - 'user' (str): The display name of the playlist's owner.

    Raises:
        spotipy.exceptions.SpotifyException: If an error occurs while fetching playlists.
    """
    try:
        playlists = []
        offset = 0
        limit = 50
        while True:
            results = sp.current_user_playlists(limit=limit, offset=offset)
            if not results or not results['items']:
                break
            playlists.extend(results['items'])
            if results['next']:
                offset += limit
            else:
                break

        if not playlists:
            return {}

        playlists_out = []

        for i, playlist in enumerate(playlists):
            owner = playlist['owner']['display_name']
            playlists_out.append({'name': playlist['name'], 'user': owner})
        return playlists_out

    except spotipy.exceptions.SpotifyException as e:
        print(f"Error fetching playlists: {e}")

def get_active_device():
    """
    Retrieves the active Spotify device ID or the first available device ID if no active device is found.

    This function uses the Spotify Web API to fetch the list of devices associated with the user's account.
    If an active device is found, its ID is returned. If no active device is found but devices are available,
    the ID of the first available device is returned. If no devices are found or an error occurs, `None` is returned.

    Returns:
        str or None: The ID of the active Spotify device, the first available device, or `None` if no devices are found.

    Exceptions:
        Handles `spotipy.exceptions.SpotifyException` and prints an error message if an exception occurs.

    Notes:
        - Ensure that the `sp` object (Spotipy client) is properly authenticated before calling this function.
        - The user must have at least one Spotify device connected to use this function.
    """
    try:
        devices = sp.devices()
        if not devices or not devices['devices']:
            print("No active Spotify device found. Please start Spotify on a device.")
            return None

        active_devices = [d for d in devices['devices'] if d['is_active']]
        if active_devices:
            device = active_devices[0]
            print(f"Using active device: '{device['name']}' ({device['type']})")
            return device['id']
        elif devices['devices']:
             device = devices['devices'][0]
             print(f"No active device detected, using first available: '{device['name']}' ({device['type']})")
             return device
        else:
             print("No devices found.")
             return None

    except spotipy.exceptions.SpotifyException as e:
        print(f"Error getting devices: {e}")
        return None

def play_item(uri, device_id):
    """
    Plays a Spotify track or playlist on a specified device.

    Args:
        uri (str): The Spotify URI of the item to play. This can be a track or playlist URI.
        device_id (str): The Spotify device ID where playback should occur.

    Returns:
        None

    Prints:
        - Error messages if `device_id` or `uri` is not provided.
        - Playback status messages indicating the type of item being played (track or playlist).
        - Error details if playback fails, including potential reasons such as:
            - Lack of Spotify Premium account for playback control.
            - Device unavailability.
            - Invalid URI.

    Raises:
        spotipy.exceptions.SpotifyException: If an error occurs during playback, with additional
        details about the HTTP status and error context.
    """
    if not device_id:
        print("Cannot play: No device ID provided.")
        return
    if not uri:
        print("Cannot play: No URI provided.")
        return

    try:
        item_type = uri.split(':')[1]
        if item_type == 'track':
            sp.start_playback(device_id=device_id, uris=[uri])
            print("Playing track...")
        elif item_type == 'playlist':
            sp.start_playback(device_id=device_id, context_uri=uri)
            print("Playing playlist...")
        else:
            print(f"Cannot play unknown URI type: {item_type}")
            return
        print("Playback initiated.")

    except spotipy.exceptions.SpotifyException as e:
        print(f"Could not start playback: {e}")
        if e.http_status == 403:
             print("NOTE: Playback control via API usually requires a Spotify Premium account.")
        elif e.http_status == 404 and "Device not found" in str(e):
             print("NOTE: Device might have become unavailable. Try selecting a device again.")
        elif e.http_status == 400:
             print(f"NOTE: Bad request. URI might be invalid: {uri}")

def stop_playback(device_id):
    """
    Stops playback on the specified Spotify device.

    Args:
        device_id (str): The unique identifier of the Spotify device where playback should be stopped.

    Returns:
        None

    Prints:
        - A success message if playback is stopped successfully.
        - An error message if no device ID is provided or if an exception occurs.

    Notes:
        - If the Spotify API returns a 403 error, it may indicate that playback control requires a Spotify Premium account.
        - If the Spotify API returns a 404 error with "Device not found," it may indicate that the device is unavailable or needs to be reselected.
    """
    if not device_id:
        print("Cannot stop: No device ID provided.")
        return

    try:
        sp.pause_playback(device_id=device_id)
        print("Playback stopped.")

    except spotipy.exceptions.SpotifyException as e:
        print(f"Could not stop playback: {e}")
        if e.http_status == 403:
             print("NOTE: Playback control via API usually requires a Spotify Premium account.")
        elif e.http_status == 404 and "Device not found" in str(e):
             print("NOTE: Device might have become unavailable. Try selecting a device again.")

def like_song(track_id):
    """
    Adds a song to the user's Liked Songs on Spotify.

    Parameters:
        track_id (str): The Spotify track ID of the song to be liked. 
                        Must be a valid non-empty string.

    Behavior:
        - If the track ID is invalid or empty, a message is printed, and the function returns.
        - If the song is already in the user's Liked Songs, a message is printed, and no action is taken.
        - If the song is not already liked, it is added to the user's Liked Songs, and a confirmation message is printed.

    Exceptions:
        - Handles `spotipy.exceptions.SpotifyException` and prints an error message if an issue occurs while interacting with the Spotify API.
    """
    if not track_id:
        print("Cannot like song: Invalid track ID provided.")
        return
    try:
        is_liked_list = sp.current_user_saved_tracks_contains(tracks=[track_id])
        if is_liked_list and is_liked_list[0]:
            print("Song is already in your Liked Songs.")
            return

        sp.current_user_saved_tracks_add(tracks=[track_id])
        print("Song added to your Liked Songs.")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Could not like song: {e}")

def add_track_to_playlist(track_uri, playlist_name):
    """
    Adds a track to a Spotify playlist by its URI.

    This function checks if the provided track URI is valid and whether the track
    is already present in the specified playlist. If the track is not already in
    the playlist, it adds the track to the playlist.

    Args:
        track_uri (str): The Spotify URI of the track to be added.
        playlist_name (str): The name of the playlist to which the track should be added.

    Returns:
        None

    Raises:
        spotipy.exceptions.SpotifyException: If there is an issue with the Spotify API.
        Exception: For any other unexpected errors.

    Notes:
        - The function uses a fuzzy search to find the playlist by name.
        - If the playlist is not found, the function exits without making changes.
        - If the track is already in the playlist, it does not add it again.
    """
    if not track_uri:
         print("Cannot add track: Invalid track URI provided.")
         return

    # Find the playlist ID using the fuzzy search function
    playlist_uri, playlist_id = find_playlist_fuzzy(playlist_name)

    if not playlist_id:
        return

    try:
        # Check if the track is already in the playlist
        results = sp.playlist_items(playlist_id, fields="items.track.uri")
        tracks = results['items']
        track_uris = [item['track']['uri'] for item in tracks]

        if track_uri in track_uris:
            print(f"Track is already in the playlist '{playlist_name}'.")
            return

        sp.playlist_add_items(playlist_id=playlist_id, items=[track_uri])
        playlist_info = sp.playlist(playlist_id, fields='name')
        print(f"Track added to playlist '{playlist_info['name']}'.")
    except spotipy.exceptions.SpotifyException as e:
        print(f"Could not add track to playlist: {e}")
    except Exception as e:
        print(f"Track added, but couldn't confirm playlist name. Error: {e}")
