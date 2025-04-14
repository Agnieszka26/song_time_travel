# 🎵 Song Time Travel
Song Time Travel is a Python application that lets you travel back in time musically! Pick any date and relive the top hits from that time. This app scrapes the Billboard Hot 100 chart for the selected date and automatically creates a Spotify playlist with those songs.

## ✨ Features
⏳ Select any date (going back decades!)

📈 Scrapes Billboard Hot 100 songs for the selected date

🎧 Automatically creates and populates a Spotify playlist with the top tracks

🐍 Built entirely in Python

## 🚀 Getting Started
### Prerequisites
Make sure you have the following:

- Python 3.7+

- A Spotify Developer account

- spotipy library for Spotify API interaction

 - requests, beautifulsoup4 for web scraping

### Installation
```
  git clone https://github.com/yourusername/song-time-travel.git
  cd song-time-travel
  pip install -r requirements.txt
```

### Spotify Setup
Create an app on the Spotify Developer Dashboard.

Set the redirect URI to: http://localhost:8888/callback/

Note your Client ID and Client Secret.

Save them as environment variables or in a .env file:


SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback/

## 🛠 Tech Stack
Python 🐍

Spotify Web API (via spotipy)

Web scraping with requests and BeautifulSoup

Billboard Hot 100 source: https://www.billboard.com/charts/hot-100

## Credits
This project is based on the 100 Days of Code: [The Complete Python Pro Bootcamp](https://www.udemy.com/course/100-days-of-code) by Angela Yu on Udemy.

## 📜 License
MIT License

