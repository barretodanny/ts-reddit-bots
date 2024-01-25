from bot import login, send_post
from api import get_random_stoic_quote
from config import read_config
from utils import parse_stoic_quote_data
from datetime import datetime

# credentials for this bot
login_profile = read_config("config.ini", "stoic_quote_bot_login")
email = login_profile["email"]
password = login_profile["password"]

# attempt to log in bot
login_result = login(email, password)

# bot logged in, grab tokens
access_token = login_result["accessToken"]

# create post
today_date = datetime.now()
formatted_date = today_date.strftime("%A %B %d, %Y")
title = f"Stoic Quote for {formatted_date}"
quote_req = get_random_stoic_quote()


if quote_req.status_code != 200:
    print("Error fetching random stoic quote, exiting.")
    exit()

res = parse_stoic_quote_data(quote_req.text)
quote = res[0]
author = res[1]
content = f"{quote} - {author}"
subreddit_names = ["Quotes"]

for subreddit_name in subreddit_names:
    post_result = send_post(title, content, subreddit_name, access_token)
