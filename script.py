import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

scope = "playlist-read-private user-library-read user-library-modify"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

while True:
    playlist_link = input("Paste the playlist link: ").strip()

    # Extract playlist ID from the link
    if "playlist/" in playlist_link:
        playlist_id = playlist_link.split("playlist/")[1].split("?")[0]
    else:
        print("Invalid playlist link.")
        exit()

    # Get all tracks from playlist
    tracks = []
    results = sp.playlist_items(playlist_id)
    tracks.extend(results['items'])
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])

    # Prepare track IDs and names, skipping invalid tracks
    track_ids = [item['track']['id'] for item in tracks if item['track'] and item['track']['id']]
    track_names = [item['track']['name'] + " - " + item['track']['artists'][0]['name'] 
    for item in tracks if item['track'] and item['track']['id']]

    def chunks(lst, n):
        """Yield successive n-sized chunks from lst."""
        for i in range(0, len(lst), n):
            yield lst[i:i + n]

    already_liked = []
    for chunk in chunks(track_ids, 50):
        already_liked.extend(sp.current_user_saved_tracks_contains(chunk))

    # Identify missing tracks
    missing_tracks = [track_names[i] for i, liked in enumerate(already_liked) if not liked]
    missing_ids = [track_ids[i] for i, liked in enumerate(already_liked) if not liked]

    if not missing_tracks:
        print("All songs in the playlist are already in your Liked Songs!")
    else:
        print("Songs missing from your Liked Songs:")
        for song in missing_tracks:
            print("❌", song)

        # Optional: Add missing songs to Liked Songs
        add = input("\nDo you want to add the missing songs to your Liked Songs? (y/n): ").lower()
        if add == "y":
            sp.current_user_saved_tracks_add(missing_ids)
            print("✅ Missing songs added to your Liked Songs!")