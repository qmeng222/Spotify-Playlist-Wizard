import openai
from dotenv import dotenv_values
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import argparse

# import pprint

config = dotenv_values(".env")
openai.api_key = config["OPENAI_API_KEY"]

parser = argparse.ArgumentParser(description="Simple command line utility")
parser.add_argument(
    "-p",
    type=str,
    default="Popular songs",
    help="The prompt to describe the playlist.",
)
parser.add_argument(
    "-n", type=int, default=9, help="The number of songs to be added to the playlist."
)

args = parser.parse_args()


def get_playlist(prompt, count=9):
    example_json = """
  [
    {"song": "The Dance", "artist": "Garth Brooks"},
    {"song": "Friends In Low Places", "artist": "Garth Brooks"},
    {"song": "Humble And Kind", "artist": "Tim McGraw"},
    {"song": "Take Your Time", "artist": "Sam Hunt"},
    {"song": "Tennessee Whiskey", "artist": "Chris Stapleton"}
  ]
  """

    messages = [
        {
            "role": "system",
            "content": """
        You are a helpful playlist generating assistant.
        You should generate a list of songs and their artists according to a text prompt.
        You should return a JSON array with each element follows this format: {"song": <song_title>, "artist": <artist_name>}
        """,
        },
        {
            "role": "user",
            "content": "Generate a playlist of 5 songs based on this prompt: country music",
        },
        {"role": "assistant", "content": example_json},
        {
            "role": "user",
            "content": f"Generate a playlist of {count} songs based on this prompt: {prompt}",
        },
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages, max_tokens=200
    )

    playlist = json.loads(response.choices[0].message.content)
    return playlist


# songs = get_playlist("epic songs", 3)
songs = get_playlist(args.p, args.n)
print(songs)

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

track_ids = []
for item in songs:
    song, artist = item["song"], item["artist"]
    query = f"{song} {artist}"
    search_results = sp.search(q=query, type="track", limit=10)
    track_ids.append(search_results["tracks"]["items"][0]["id"])

created_playlist = sp.user_playlist_create(
    current_user["id"], public=False, name=args.p
)

# append searched track to the playlist:
sp.user_playlist_add_tracks(current_user["id"], created_playlist["id"], track_ids)
