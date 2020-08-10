from bs4 import BeautifulSoup
import requests

link = "https://www.wsj.com/"

request = requests.get(link)
contents = request.content
soup = BeautifulSoup(contents, "html.parser")

print(soup.prettify())
