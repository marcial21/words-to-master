import requests
from bs4 import BeautifulSoup

class GoogleSearchService:
    def __init__(self) -> None:
        pass

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



m = GoogleSearchService()

word = "ferocious"
definition = m.getDefinition(word)
if definition:
    print(f"The definition of '{word}' is '{definition}'")
else:
    print(f"No definition found for '{word}'")

