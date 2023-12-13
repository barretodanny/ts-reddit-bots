import requests

ENDPOINT = "https://ts-reddit-rest-api.onrender.com/api"
LOGIN_ENDPOINT = f"{ENDPOINT}/sessions"
SUBREDDITS_ENDPOINT = f"{ENDPOINT}/subreddits"

def create_session(payload):
    return requests.post(LOGIN_ENDPOINT, json=payload)

def get_subreddit_by_name(subreddit_name):
    return requests.get(f"{SUBREDDITS_ENDPOINT}/{subreddit_name}?string=true")
