from bot import login, send_post
from api import get_chucknorris_joke
from config import read_config
from utils import parse_chucknorris_joke_data
from datetime import datetime

# credentials for this bot
login_profile = read_config("config.ini", "chucknorris_joke_bot_login")
email = login_profile["email"]
password = login_profile["password"]

# attempt to log in bot
login_result = login(email, password)

# bot logged in, grab tokens
access_token = login_result["accessToken"]

# create post
today_date = datetime.now()
formatted_date = today_date.strftime("%A %B %d, %Y")
title = f"Chuck Norris Joke for {formatted_date}"
joke_req = get_chucknorris_joke()

if joke_req.status_code != 200:
    print("Error fetching chuck norris joke, exiting.")
    exit()

joke = parse_chucknorris_joke_data(joke_req.text)
subreddit_names = ["Jokes"]

for subreddit_name in subreddit_names:
    post_result = send_post(title, joke, subreddit_name, access_token)
