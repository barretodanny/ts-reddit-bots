from bot import *
from config import read_config
from datetime import datetime
from utils import parse_cat_fact_data

# credentials for this bot
login_profile = read_config("config.ini", "cat_fact_bot_login")
email = login_profile["email"]
password = login_profile["password"]

# attempt to log in bot
login_result = login(email, password)

# bot logged in, grab tokens
access_token = login_result["accessToken"]

# create post
today_date = datetime.now()
formatted_date = today_date.strftime("%A %B %d, %Y")
title = f"Cat fact for {formatted_date}"
cat_fact_req = get_cat_fact()

if cat_fact_req.status_code != 200:
    print("Error fetching cat fact, exiting.")
    exit()

content = parse_cat_fact_data(cat_fact_req.text)
subreddit_names = ["Cats", "Facts"]

for subreddit_name in subreddit_names:
    post_result = send_post(title, content, subreddit_name, access_token)
