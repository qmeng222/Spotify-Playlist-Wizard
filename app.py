import openai
from dotenv import dotenv_values
import spotipy
from spotipy.oauth2 import SpotifyOAuth

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=config["SPOTIFY_CLIENT_ID"],
        client_secret=config["SPOTIFY_CLIENT_SECRET"],
        redirect_uri="http://localhost:9999",
    )
)

current_user = sp.current_user()
print(current_user)
