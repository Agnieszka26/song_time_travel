import SongScraper
import SpotifyLogin

song_scraper = SongScraper.SongScraper()

song_scraper.get_songs()
songs = song_scraper.songs[:10]

spotify_login = SpotifyLogin.SpotifyLogin
sp = spotify_login().sp

for song in songs:
    query = f"track:{song['track']} artist:{song['artist']} year:{song['year']}"
    results = sp.search(q=query, type="track", limit=1)
    if results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        print(f"Found: {track['name']} by {track['artists'][0]['name']}")
    else:
        print("Song not found.")