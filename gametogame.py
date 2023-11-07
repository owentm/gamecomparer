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

# def keyWordPositive(key, game):
#     keySearch = "https://www.ign.com/wikis/" + game.lower().replace(' ', '-')
#
#     keyPage = requests.get(keySearch)
#     if keyPage.status_code == 200:
#         keyAccess = BeautifulSoup(keyPage.text, 'html.parser')
#         keywordSearch = keyAccess.find(text = lambda text: text and key in text.lower())
#         return 5 if keywordSearch else 0
#     else:
#         print("Unable to process page.")
#         return 0
#










url1 = input('Input name of first game: ')
url2 = input('Input name of second game: ')
#allow user to search for two games

checkFlag = 0

sum1 = 0
sum2 = 0




game1 = gameSearch(url1)
game2 = gameSearch(url2)
#change the strings to the correct urls

# while checkFlag == 0:
#
#     keywordPlus = input('Input feature that you are wanting: ')
#     print(keywordPlus)
#     sum1 += keyWordPositive(keywordPlus, url1)
#     sum2 += keyWordPositive(keywordPlus, url2)
#     check = input('More features? If no, input N: ')
#     if check == 'N':
#         checkFlag = 1
#     else:
#         checkFlag = 0




gamepage1 = requests.get(game1)
gamepage2 = requests.get(game2)
#access internet pages

# if gamepage1.status_code == 200 and gamepage2.status_code == 200:
soup = BeautifulSoup(gamepage1.text, features='html.parser')
soup2 = BeautifulSoup(gamepage2.text, features='html.parser')
    #read pages


spans = soup.find(name='span', attrs={'class' : 'score score-long'})
spans2 = soup2.find(name='span', attrs={'class' : 'score score-long'})
    #find the scores

# sum1 += type(int(spans.get_text(strip=True)))
# sum2 += type(int(spans2.get_text(strip=True)))


print(url1 + ": " + sum1)
print(url2 + ": " + sum2)
    #print out the respective scores
# else:
#     print("Could not find the gamepage for one or both of the attempted pages.")

