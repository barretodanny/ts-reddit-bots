import random
from bot import login, send_post
from api import get_random_pokemon
from config import read_config
from utils import parse_pokemon_data
from datetime import datetime

TOTAL_NUMBER_OF_POKEMON = 1025

# credentials for this bot
login_profile = read_config("config.ini", "random_pokemon_bot_login")
email = login_profile["email"]
password = login_profile["password"]

# attempt to log in bot
login_result = login(email, password)

# bot logged in, grab tokens
access_token = login_result["accessToken"]

# create post
today_date = datetime.now()
formatted_date = today_date.strftime("%A %B %d, %Y")
title = f"Random Pokemon for {formatted_date}"

# fetch pokemon based on a random number from 1 to n
# where n is the total number of pokemon
n = random.randint(1, TOTAL_NUMBER_OF_POKEMON)
random_pokemon_req = get_random_pokemon(n)

if random_pokemon_req.status_code != 200:
    print("Error fetching random pokemon, exiting.")
    exit()

pokemon = parse_pokemon_data(random_pokemon_req.text).capitalize()
subreddit_names = ["Pokemon"]

for subreddit_name in subreddit_names:
    post_result = send_post(title, pokemon, subreddit_name, access_token)
