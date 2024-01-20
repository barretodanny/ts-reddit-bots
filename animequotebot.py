from bot import login, send_post
from api import get_anime_quote
from config import read_config
from utils import parse_anime_quote_data

# credentials for this bot
login_profile = read_config("config.ini", "anime_quote_bot_login")
email = login_profile["email"]
password = login_profile["password"]

# attempt to log in bot
login_result = login(email, password)

# bot logged in, grab tokens
access_token = login_result["accessToken"]

# create post
anime_quote_req = get_anime_quote()

if anime_quote_req.status_code != 200:
    print("Error fetching anime quote, exiting.")
    exit()

anime_title, character, quote = parse_anime_quote_data(anime_quote_req.text)
subreddit_names = ["Anime", "Quotes"]

for subreddit_name in subreddit_names:
    title = f"{anime_title} - {character}"
    post_result = send_post(title, quote, subreddit_name, access_token)
