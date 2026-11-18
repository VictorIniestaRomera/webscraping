from scraper import Scraper;
from uigenerator import UIGenerator;

def main():
    scr = Scraper();
    scr.connect();
    scr.scrap(quoteFilter=["The"], tagsFilter=["change"]);

    uig = UIGenerator();
    uig.drawTable(scr.getQuotes());

if __name__ == "__main__":
    main();