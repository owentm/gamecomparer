import requests
from bs4 import BeautifulSoup

def get_metacritic_user_score(game_title):
    base_url = "https://www.metacritic.com"
    search_url = "{base_url}/game/{game_title}/"

    # Send a GET request to the search page
    response = requests.get(search_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all("li", class_="result")
        if search_results:
            # Select the first search result (assuming it's the most relevant)
            first_result = search_results[0]
            game_url = base_url + first_result.find('a', class_='title')['href']

            # Send a GET request to the game's page
            game_response = requests.get(game_url)
            if game_response.status_code == 200:
                game_soup = BeautifulSoup(game_response.text, 'html.parser')

                # Find the user score
                user_score = game_soup.find("div", class_="user")
                if user_score:
                    user_score = user_score.find("span", class_="textscore").get_text()
                    return user_score
                else:
                    return "User score not found"
            else:
                return "Failed to retrieve game page"
        else:
            return "Game not found on Metacritic"
    else:
        return "Failed to retrieve search results"

if __name__ == "__main__":
    game1_title = input("Enter the title of the first game: ")
    game2_title = input("Enter the title of the second game: ")

    game1_score = get_metacritic_user_score(game1_title)
    game2_score = get_metacritic_user_score(game2_title)

    if game1_score != "User score not found" and game2_score != "User score not found":
        print(f"{game1_title} User Score: {game1_score}")
        print(f"{game2_title} User Score: {game2_score}")
    else:
        print("Error: One or both game scores could not be retrieved from Metacritic.")
