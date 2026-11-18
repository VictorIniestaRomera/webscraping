from scraper import Scraper;
from uigenerator import UIGenerator;

def main():
    scr = Scraper();
    scr.connect();
    scr.scrap(textFilter=["The"]);
    #scr.scrap();

    uig = UIGenerator();
    uig.drawTable(scr.getQuotes());
    uig.drawBarChart(scr.getQuotes());

if __name__ == "__main__":
    main();