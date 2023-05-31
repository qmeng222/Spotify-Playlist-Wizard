# Spotify Playlist Wizard

## Overview:

- **_Intro_**: The Spotify Playlist Wizard is an innovative application that leverages the power of the GPT (Generative Pre-trained Transformer) model to generate music playlists on Spotify based on user prompts. This project aims to enhance the music discovery experience for Spotify users by providing personalized and relevant playlists tailored to their specific interests and preferences.
- **_Tech stack_**: GPT, Python

![Project Overview](/Spotify-Playlist-Wizard.gif)

## Setup:

1. create a virtual environment: `python -m venv env`
2. activate the virtual environment: `source env/bin/activate` (all subsequent steps should be performed within the virtual environment)
3. update pip: `python -m pip install --upgrade pip`
4. install the OpenAI package, the python-dotenv package, and the Spotipy library (a lightweight Python library that provides a simple and convenient way to interact with the Spotify Web API):
   ```
   pip install openai
   pip install python_dotenv
   pip install spotipy
   ```
   or simply `pip install openai python_dotenv spotipy` altogether!
5. accept command line arguments by running `python app.py -p "Independence Day songs" -n 12`, for example

## Resources

1. Spotify for Developers: https://developer.spotify.com/
2. Spotify web player: https://open.spotify.com/
