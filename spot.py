import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'xxx'
client_secret = 'yyy'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

playlist_id = 'zzz'

results = sp.playlist_tracks(playlist_id)
tracks = results['items']

#Extracting tracks'info 
with open('Name.docx', 'a', encoding='utf-8') as file:
    for item in tracks:
        track = item['track']
        track_name = track['name']
        track_id = track['id']
        track_url = track['external_urls']['spotify']
        album_name = track['album']['name']
        album_url = track['album']['external_urls']['spotify']
        artist_ids = [artist['id'] for artist in track['artists']]
        artist_names = [artist['name'] for artist in track['artists']]

        artist_details = []
        for artist_id in artist_ids:
            artist = sp.artist(artist_id)
            genres = artist['genres']
            artist_info = {
                'id': artist_id,
                'name': artist['name'],
                'genres': genres
            }
            artist_details.append(artist_info)

        file.write(f'Track: {track_name}\n')
        file.write(f'Track URL: {track_url}\n')
        file.write(f'Album: {album_name}\n')
        file.write('Artists:\n')
        for artist in artist_details:
            file.write(f'  - Artist Name: {artist["name"]}\n')
            file.write(f'    Genres: {", ".join(artist["genres"])}\n')
        file.write('---\n')

print("Complete!")
