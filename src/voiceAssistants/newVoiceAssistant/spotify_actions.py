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
if redirect_uri != 'http://localhost:8888/callback':
    print("Warning: Make sure SPOTIPY_REDIRECT_URI in your .env file is set to 'http://localhost:8888/callback'.")

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

def find_track(name):
    """Searches for a track and returns its URI and ID. Spotify's search has some inherent fuzziness."""
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

def find_playlist_fuzzy(name, similarity_threshold=75):
    """
    Searches within the user's playlists using fuzzy matching and returns the best match's URI and ID.
    Prioritizes playlists created by the user.
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

def list_user_playlists():
    """Lists the current user's playlists."""
    print("\n--- Your Playlists ---")
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
            print("No playlists found.")
            return

        for i, playlist in enumerate(playlists):
            owner = playlist['owner']['display_name']
            print(f"{i+1}. {playlist['name']} (by {owner})")
        print(f"--- Found {len(playlists)} playlists ---")

    except spotipy.exceptions.SpotifyException as e:
        print(f"Error fetching playlists: {e}")

def get_active_device():
    """Gets the ID of the first available active device."""
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
             return device['id']
        else:
             print("No devices found.")
             return None

    except spotipy.exceptions.SpotifyException as e:
        print(f"Error getting devices: {e}")
        return None

def play_item(uri, device_id):
    """Plays a track or playlist URI on the specified device."""
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
    """Stops playback on the specified device."""
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
    """Adds a track to the user's 'Liked Songs'."""
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
    """Adds a track URI to a specified playlist by name (using fuzzy search)."""
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

# --- Main Command Loop ---

def run_cli():
    """Runs the command-line interface loop."""
    print("\nAvailable commands:")
    print("  playsong <song name>          - Play a track")
    print("  playplaylist <playlist name>  - Play a playlist")
    print("  stop                          - Stop playback")
    print("  like <song name>              - Add a song to your Liked Songs")
    print("  add <song name> to <playlist name> - Add song to fuzzy matched playlist")
    print("  playlists                     - List all your playlists")
    print("  device                        - Show and select active device")
    print("  quit                          - Exit the application")
    print("-" * 20)

    active_device_id = get_active_device()

    while True:
        command_line = input("> ").strip()
        if not command_line:
            continue

        parts = command_line.lower().split()
        action = parts[0]

        if action == "quit":
            print("Exiting Spotify Controller.")
            break

        elif action == "device":
            active_device_id = get_active_device()

        elif action == "playlists":
            list_user_playlists()

        elif action == "playsong":
            if len(parts) < 2:
                print("Usage: playsong <song name>")
                continue
            song_query = " ".join(parts[1:])
            track_uri, _ = find_track(song_query)
            if track_uri:
                 if not active_device_id:
                      print("No active device selected. Trying to find one...")
                      active_device_id = get_active_device()
                 if active_device_id:
                      play_item(track_uri, active_device_id)
                 else:
                      print("Playback failed: Could not find an active device.")

        elif action == "playplaylist":
            if len(parts) < 2:
                print("Usage: playplaylist <playlist name>")
                continue
            playlist_query = " ".join(parts[1:])
            playlist_uri, _ = find_playlist_fuzzy(playlist_query)
            if playlist_uri:
                 if not active_device_id:
                      print("No active device selected. Trying to find one...")
                      active_device_id = get_active_device()
                 if active_device_id:
                      play_item(playlist_uri, active_device_id)
                 else:
                      print("Playback failed: Could not find an active device.")

        elif action == "stop":
            if not active_device_id:
                print("No active device selected. Trying to find one...")
                active_device_id = get_active_device()
            if active_device_id:
                stop_playback(active_device_id)
            else:
                print("Could not stop playback: No active device found.")

        elif action == "like":
            if len(parts) < 2:
                print("Usage: like <song name>")
                continue
            song_query = " ".join(parts[1:])
            _, track_id = find_track(song_query)
            if track_id:
                like_song(track_id)

        elif action == "add":
            try:
                to_index = parts.index("to")
                if to_index == 1 or to_index == len(parts) - 1:
                    raise ValueError
                song_query = " ".join(parts[1:to_index])
                playlist_query = " ".join(parts[to_index+1:])

                track_uri, _ = find_track(song_query)
                if track_uri:
                   add_track_to_playlist(track_uri, playlist_query)

            except ValueError:
                print("Invalid 'add' format. Use: add <song name> to <playlist name>")

        else:
            print(f"Unknown command: '{action}'. Type 'quit' to exit.")

# --- Run the Application ---
if __name__ == "__main__":
    run_cli()