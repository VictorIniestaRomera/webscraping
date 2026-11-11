from bs4 import BeautifulSoup;

import requests

#Select all
url = "https://quotes.toscrape.com/"

response = requests.get(url, timeout=10)
response.raise_for_status()

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser");

print(soup.prettify()[:2000])

#Select specific
getDivs = soup.select("div.quote");

for div in getDivs:
    quote = div.select_one("span.text");
    author = div.select_one("small.author");

    if quote and author:
        print(quote.get_text(strip=True));
        print(author.get_text(strip=True))