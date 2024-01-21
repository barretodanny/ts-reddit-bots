from bot import login, send_post
from api import get_useless_fact
from config import read_config
from utils import parse_useless_fact_data
from datetime import datetime

print(0)
# credentials for this bot
login_profile = read_config("config.ini", "useless_fact_bot_login")
email = login_profile["email"]
password = login_profile["password"]

print(1)
# attempt to login bot
login_result = login(email, password)

print(2)
# bot logged in, grab tokens
access_token = login_result["accessToken"]

print(3)
# create post
today_date = datetime.now()
formatted_date = today_date.strftime("%A %B %d, %Y")
title = f"Useless Fact for {formatted_date}"
useless_fact_req = get_useless_fact()

if useless_fact_req.status_code != 200:
    print("Error fetching useless fact, exiting.")
    exit()

print(4)
fact = parse_useless_fact_data(useless_fact_req.text)
subreddit_names = ["Facts"]

print(5)
for subreddit_name in subreddit_names:
    post_result = send_post(title, fact, subreddit_name, access_token)
