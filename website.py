import requests
import re

import spans
from bs4 import BeautifulSoup
def gameOneSearch(search1):
    return "search"
def gameTwoSearch(search2):
    return "search"

url1 = 'https://www.pcgamer.com/baldurs-gate-3-review/'
url2 = 'https://www.pcgamer.com/starfield-review/'

gamepage1 = requests.get(url1)
gamepage2 = requests.get(url2)
soup = BeautifulSoup(gamepage1.text, 'html.parser')
soup2 = BeautifulSoup(gamepage2.text, features='html.parser')


spans = soup.find('span', {'class' : 'score score-long'})
spans2 = soup2.find(name='span', attrs={'class' : 'score score-long'})


print(soup.title)
print(spans)
print(spans2)