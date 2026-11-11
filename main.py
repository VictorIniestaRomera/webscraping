from bs4 import BeautifulSoup;

import requests;
import csv;

#Select all
url = "https://quotes.toscrape.com/"

response = requests.get(url, timeout=10)
response.raise_for_status()

print(response.status_code)

soup = BeautifulSoup(response.text, "html.parser");

print(soup.prettify()[:2000])

#Select specific
quotes = [];

for phrase in soup.select("div.quote"):
    quote = phrase.select_one("span.text");
    author = phrase.select_one("small.author");

    if quote is None or author is None:
        continue;

    tags = [tag.get_text(strip=True) for tag in phrase.select_one("a.tag")];

    quotes.append({
            "quote": quote.get_text(strip=True).replace('"', "'"), 
            "author": author.get_text(strip=True),
            "tags": ", ".join(tags)
        });

    for item in quotes[:3]:
        print(item);

    fieldnames = ["quote", "author", "tags"];

    with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames);

        writer.writeheader();
        writer.writerows(quotes);

    print(f"Saved {len(quotes)} quotes to 'quotes.csv'");