"""
Simple web scraper to get fact from http://unkno.com/

E.g., fact is embedded within a <div> with id "content"
<div id="content">An octupus has 3 hearts.</div>

"""
import requests
from bs4 import BeautifulSoup

URL = "http://unkno.com"


def main():
    """ Main application """
    page = requests.get(URL)
    soup = BeautifulSoup(page.text, "html.parser")
    fact = soup.find("div", {"id": "content"})
    return fact.text.strip()


if __name__ == "__main__":
    FACTOID = main()
    print(FACTOID)
