import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'dd2d1fa01f334bca967eb8d848fb5de3'
client_secret = '6697b93cfa1c412da35947475287c22d'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

playlist_id = '0SuY989mdonafXmhFw2WpF'

results = sp.playlist_tracks(playlist_id)
tracks = results['items']

with open('RNB_Playlist.txt', 'w', encoding='utf-8') as file:
    for item in tracks:
        track = item['track']
        track_name = track['name']
        artist_id = track['artists'][0]['id']

        artist = sp.artist(artist_id)
        genres = artist['genres']

        file.write(f'Track: {track_name}\n')
        file.write(f'Genres: {", ".join(genres)}\n')
        file.write('---\n')
