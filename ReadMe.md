# Spotify Playlist Wizard

## Overview:

- Introduction: The Spotify Playlist Wizard is an innovative application that leverages the power of the GPT (Generative Pre-trained Transformer) model to generate music playlists on Spotify based on user prompts. This project aims to enhance the music discovery experience for Spotify users by providing personalized and relevant playlists tailored to their specific interests and preferences.
- Tech stack: GPT, Python
  ![Project Overview](/playlist_generator.gif)

---

## Setup:

1. create a virtual environment: `python -m venv env`
2. activate the virtual environment: `source env/bin/activate`
3. (within virtual environment) install OpenAI, the python-dotenv package, and the Spotipy library (a lightweight Python library that provides a simple and convenient way to interact with the Spotify Web API):
   ```
   pip install openai
   pip install python_dotenv
   pip install spotipy
   ```
   or simply `pip install openai python_dotenv spotipy` altogether!
4. (within virtual environment) run the file: `python app.py`
