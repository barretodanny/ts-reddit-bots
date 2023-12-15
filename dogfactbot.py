from bot import *
from config import read_config
from datetime import datetime
from utils import parse_dog_fact_data

# credentials for this bot
login_profile = read_config("config.ini", "dog_fact_bot_login")
email = login_profile["email"]
password = login_profile["password"]

# attempt to log in bot
login_result = login(email, password)

# bot logged in, grab tokens
access_token = login_result["accessToken"]

# create post
today_date = datetime.now()
formatted_date = today_date.strftime("%A %B %d, %Y")
title = f"Dog fact for {formatted_date}"
dog_fact_req = get_dog_fact()

if dog_fact_req.status_code != 200:
    print("Error fetching dog fact, exiting.")
    exit()

content = parse_dog_fact_data(dog_fact_req.text)
subreddit_names = ["Dogs", "Facts"]

for subreddit_name in subreddit_names:
    post_result = send_post(title, content, subreddit_name, access_token)
