from bs4 import BeautifulSoup
import requests

URL = "https://www.billboard.com/charts/hot-100/"
class SongScraper:
    def __init__(self):
        self.songs = []
        self.date = input(f"Which year would you want to go? Type date in this format YYYY-MM-DD:")
    def get_songs(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
        url = f"{URL}{self.date}"
        songs_website = requests.get(url=url, headers=headers)
        songs_website.raise_for_status()

        soup = BeautifulSoup(songs_website.text, "html.parser")

        all_song_band_elements = soup.select(selector="li.o-chart-results-list__item > h3#title-of-a-story")
        for song in all_song_band_elements:
            song_title = song.getText().strip()

            parent = song.find_parent("li")
            artist_span = parent.select_one("span.c-label")

            artist = artist_span.getText().strip() if artist_span else "Unknown Artist"
            self.songs.append(f"{song_title} - {artist}")

        return self.songs

