# Spotify Playlist Liker

A Python script to check all tracks in a Spotify playlist and add missing songs to your Liked Songs.

## Features
- Reads a playlist from Spotify using its URL.
- Compares each track against your Liked Songs.
- Lists tracks that are not yet liked.
- Optionally adds missing tracks to your Liked Songs automatically.
- Handles large playlists (chunks requests to comply with Spotify API limits).
- Skips unavailable or local tracks.

## Requirements
- Python 3.8+
- [Spotipy](https://spotipy.readthedocs.io/en/2.22.0/)
- python-dotenv

Install dependencies:
```
pip install -r requirements.txt
```

## Spotify API Setup
1. Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and create a new app.
2. Set a Redirect URI (e.g., `http://127.0.0.1:8888/callback`).
3. Enable the WebAPI SDK.
4. Copy the **Client ID** and **Client Secret**.
5. Create a `.env` file in the project root (use `.env.example` as a template).

## Usage
1. Run the script:
```
python script.py
```
2. Paste your Spotify playlist URL when prompted.
3. The script will display which songs are missing from your Liked Songs.
4. Optionally, add missing songs automatically.

## Notes
- Spotify API only allows 50 track IDs per request, so the script splits large playlists into chunks automatically.
- Tracks without valid Spotify IDs (e.g., local or unavailable tracks) are skipped.
- Your Liked Songs will sync across all devices automatically.

## License
This script is free to use and modify.
