from bot import *
from config import read_login_config
from datetime import datetime

# credentials for this bot
login_profile = read_login_config("config.ini", "date_bot_login")
email = login_profile["email"]
password = login_profile["password"]

# attempt to log in bot
login_result = login(email, password)

# bot logged in, grab tokens
access_token = login_result["accessToken"]
refresh_token = login_result["refreshToken"]

# create post
today_date = datetime.now()
formatted_date = today_date.strftime("%A %B %d, %Y")
title = f"Today is {formatted_date}"
content = "Have a wonderful day!"
subreddit_name = "Today"
post_result = send_post(title, content, subreddit_name, access_token)
