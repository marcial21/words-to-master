"""
Gabriel Marcial
https://github.com/marcial21
mgabrielofficial@outlook.com

GoogleSearchService.py
"""

import requests
from bs4 import BeautifulSoup

"""
Service class used to handle queries to google search.
"""
class GoogleSearchService:
    # Constructor
    def __init__(self) -> None:
        pass

    """
    Queries google api for words and scrapes the html returned and filters it so that
    we can extract the definition. 

    Parameters:
        word (string): The word that we will lookup definition for.

    Returns
        string: The definition scraped from the html.
    """
    def getDefinition(self, word):
        url = f"https://www.google.com/search?q=define+{word}"
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        #print(soup.prettify())
        definition = None
        for tag in soup.find_all("div"):
            if "data-dobid" in tag.attrs and tag.attrs["data-dobid"] == "dfn":
                definition = tag.get_text()
                break
        return definition
    
    """
    Queries google api for words and scrapes the html returned and filters it so that
    we can extract all the definitions. 

    Parameters:
        word (string): The word that we will lookup definition for.

    Returns
        list: The definitions scraped from the html.
    """
    def getMultipleDefinitions(self, word):
        url = f"https://www.google.com/search?q=define+{word}"
        headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36"}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        definitions = []
        for tag in soup.find_all("div"):
            if "data-dobid" in tag.attrs and tag.attrs["data-dobid"] == "dfn":
                definitions.append(tag.get_text())
        return definitions
    
    # Todo: get 'Part of Speech' from words
    def getPartsOfSpeech(self):
        pass
