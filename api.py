import requests

ENDPOINT = "https://ts-reddit-rest-api.onrender.com/api"
LOGIN_ENDPOINT = f"{ENDPOINT}/sessions"
SUBREDDITS_ENDPOINT = f"{ENDPOINT}/subreddits"
POSTS_ENDPOINT = f"{ENDPOINT}/posts"

def create_session(payload):
    return requests.post(LOGIN_ENDPOINT, json=payload)

def get_subreddit_by_name(subreddit_name):
    return requests.get(f"{SUBREDDITS_ENDPOINT}/{subreddit_name}?string=true")

def create_post(payload, token):
    header = {"Authorization": f"Bearer {token}"}
    return requests.post(f"{POSTS_ENDPOINT}", json=payload, headers=header)