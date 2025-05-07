import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Load .env variables
load_dotenv()

# Get credentials
client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI")

# Set scope – this determines what data you can access
scope = "user-top-read"

# Create Spotipy client with OAuth
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
))

# Get user's top tracks
top_tracks = sp.current_user_top_tracks(limit=10, time_range='short_term')

# Print the top track names
print("Your Top Tracks:")
for idx, track in enumerate(top_tracks['items']):
    print(f"{idx + 1}. {track['name']} by {track['artists'][0]['name']}")

