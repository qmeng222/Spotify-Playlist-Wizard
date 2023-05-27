import openai
from dotenv import dotenv_values
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pprint

"""
REFERENCE ONLY:
[
  {"song": "Everybody Hurts", "artist": "R.E.M."},
  {"song": "Nothing Compares 2 U", "artist": "Sinead O'Connor"},
  {"song": "Tears in Heaven", "artist": "Eric Clapton"},
  {"song": "Hurt", "artist": "Johnny Cash"},
  {"song": "Yesterday", "artist": "The Beatles"}
]
"""

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

# sp object is an instance of the spotipy.Spotify class, which represents a client for interacting with the Spotify API.:
sp = spotipy.Spotify(
    # auth_manager is set to an instance of SpotifyOAuth:
    auth_manager=SpotifyOAuth(
        client_id=config["SPOTIFY_CLIENT_ID"],
        client_secret=config["SPOTIFY_CLIENT_SECRET"],
        redirect_uri="http://localhost:9999",
        scope="playlist-modify-private",
    )
)

current_user = sp.current_user()
assert current_user is not None
# print(current_user)
search_results = sp.search(q="Uptown Funk", type="track", limit=10)
tracks = [search_results["tracks"]["items"][0]["id"]]

created_playlist = sp.user_playlist_create(
    current_user["id"], public=False, name="Testing Playlist"
)

sp.user_playlist_add_tracks(current_user["id"], created_playlist["id"], tracks)
