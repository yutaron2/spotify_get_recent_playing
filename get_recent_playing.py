import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

client_id = os.environ['SPOTIPY_CLIENT_ID']
client_secret = os.environ['SPOTIPY_CLIENT_SECRET']

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

recently_played = sp.current_user_recently_played(limit=50)


for idx, item in enumerate(recently_played['items']):
    track = item['track']
    print(f"{idx+1}: {track['name']} by {track['artists'][0]['name']}") 
