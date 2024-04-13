import requests
from bs4 import BeautifulSoup
import json
HOST = "https://open.spotify.com"
URL = "https://open.spotify.com/artist/67ex1KyNuK3IvMiwejjz2X"
HEADERS = {
    "accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent" : "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36"
}

def get_html(url, params = ""):
    request = requests.get(url, headers=HEADERS, params=params)
    return request

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all("div", class_="GtWz6DBoskS84f0Pggus")
    articles = []
    for item in items:
        try:
            articles.append(
                {
                    "name" : item.find("a").find("span", class_="Type__TypeElement-sc-goli3j-0 ivZzFX bAoMcNJrNmKnmCl3rsYX").get_text(strip=True),
                    "img" : item.find("a").find("div", class_="oBCZQFuv15YE1qV0Fpph").find("img").get("src"),
                    "when" : item.find("a").find("div", class_="Type__TypeElement-sc-goli3j-0 hPtQNW NUIYLDG1fxo4fduLNM4C").get_text(strip=True),
                    "link" : HOST + item.find("a").get("href")
                }
            )
        except Exception as e:
            pass
        
    return articles


def parser():
    html = get_html(url=URL)
    articles = get_content(html.text)
    with open("./music.json", "w") as file:
        json.dump(articles, file, indent=4, ensure_ascii=False)

if __name__ == "__main__":
    parser() 