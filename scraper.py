from bs4 import BeautifulSoup;

import requests;
import csv;

class Scraper:
    URL = "https://quotes.toscrape.com/";

    response: requests.Request;
    soup: BeautifulSoup;

    quotes = [];

    def __init__(self):
        pass;

    def connect(self) -> None:
        self.response = requests.get(self.URL, timeout=10);
        self.response.raise_for_status();

        self.soup = BeautifulSoup(self.response.text, "html.parser");
        
        print(self.response.status_code);

    def printSoup(self) -> None:
        print(self.soup.prettify()[:2000]);

    def scrap(self, authorFilter: list = None, tagsFilter: list = None, textFilter: list = None) -> None:
        for phrase in self.soup.select("div.quote"):
            quote = phrase.select_one("span.text");
            author = phrase.select_one("small.author");
            
            if quote is None or author is None:
                continue;

            text = quote.get_text(strip=True);
            authorText = author.get_text(strip=True);
            tags = [tag.get_text(strip=True) for tag in phrase.select_one("a.tag")];

            if authorFilter is not None:
                cont = False;

                for flag in authorFilter:
                    if flag == authorText:
                        cont = True;

                        break;

                if not cont:
                    continue;

            if tagsFilter is not None:
                cont = False;

                for tag in tags:
                    if tag in tagsFilter:
                        cont = True;

                        break;

                if not cont:
                    continue;

            if textFilter is not None:
                cont = False;

                for flag in textFilter:
                    if flag in text:
                        cont = True;

                        break;

                if not cont:
                    continue;

            self.quotes.append({
                "quote": text.replace('"', "'"), 
                "author": authorText,
                "tags": ", ".join(tags)
            });

            for item in self.quotes[:3]:
                print(item);

            fieldnames = ["quote", "author", "tags"];

            with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=fieldnames);

                writer.writeheader();
                writer.writerows(self.quotes);

            print(f"Saved {len(self.quotes)} quotes to 'quotes.csv'");

    def getQuotes(self) -> list:
        return self.quotes;