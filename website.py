import requests
from bs4 import BeautifulSoup

url = 'https://www.pcgamer.com/baldurs-gate-3-review/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
print(soup.title)
print(soup.find('span class = "score score-long"'))