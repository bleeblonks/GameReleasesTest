import requests
from bs4 import BeautifulSoup

def fetch_pc_releases():
    url = "https://www.releases.com/new/pc"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    games = []

    for game in soup.select(".card-release"):
        title = game.select_one(".card-title").get_text(strip=True)
        platform = "PC"
        date_tag = game.select_one(".card-release-date")

        if not title or not date_tag:
            continue

        release_date = date_tag.get_text(strip=True)

        games.append({
            "title": title,
            "platform": platform,
            "release_date": release_date
        })

    return games
