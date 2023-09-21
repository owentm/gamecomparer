#TODO
# add more websites to search, add keywords, add GUI elements

import requests
import re

import spans
from bs4 import BeautifulSoup
#take in user input, and turn it into a searchable function for pcgamer.com
def gameSearch(game):

    newGame = "https://www.pcgamer.com/" + game.lower().replace(' ', '-') + "-review"
    return newGame




url1 = input('Input name of first game: ')
url2 = input('Input name of second game: ')
#allow user to search for two games




game1 = gameSearch(url1)
game2 = gameSearch(url2)
#change the strings to the correct urls




gamepage1 = requests.get(game1)
gamepage2 = requests.get(game2)
#access internet pages

soup = BeautifulSoup(gamepage1.text, features='html.parser')
soup2 = BeautifulSoup(gamepage2.text, features='html.parser')
#read pages


spans = soup.find(name='span', attrs={'class' : 'score score-long'})
spans2 = soup2.find(name='span', attrs={'class' : 'score score-long'})
#find the scores




print(url1 + ": " + spans.get_text(strip=True))
print(url2 + ": " + spans2.get_text(strip=True))
#print out the respective scores

