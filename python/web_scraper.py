"""Lightweight HTML scraping helpers using requests and BeautifulSoup.

Provides a small toolkit for fetching pages, parsing elements, and extracting
links or text content for quick data collection scripts.
"""

import requests
from bs4 import BeautifulSoup


def fetch_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def parse_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    titles = [h.get_text(strip=True) for h in soup.find_all('h1')]
    return titles


if __name__ == "__main__":
    url = "https://example.com"
    html = fetch_page(url)
    data = parse_content(html)
    for item in data:
        print(item)
