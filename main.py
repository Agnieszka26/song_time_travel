import SongScraper
import SpotifyLogin

song_scraper = SongScraper.SongScraper()

song_scraper.get_songs()
songs = song_scraper.songs

spotify_login = SpotifyLogin.SpotifyLogin()
sp = spotify_login.sp
user_id = spotify_login.user_id
items = []
for song in songs:
    query = f"track:{song['track']} artist:{song['artist']} year:{song['year']}"
    results = sp.search(q=query, type="track", limit=1)
    if results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        spotify_url = track['external_urls']['spotify']
        items.append(spotify_url)
        print(f"{track['name']} by {track['artists'][0]['name']}")
        print(f"URL: {spotify_url}\n")
    else:
        print("Song not found.")


playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{song_scraper.date} Billboard 100",
    public=True,
    collaborative=False,
    description="Time traveller for python")
playlist_id = playlist["id"]
print(playlist)
sp.playlist_add_items(playlist_id, items, position=None)
