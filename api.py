import requests

ENDPOINT = "https://ts-reddit-rest-api.onrender.com/api"
LOGIN_ENDPOINT = f"{ENDPOINT}/sessions"

def create_session(payload):
    return requests.post(LOGIN_ENDPOINT, json=payload)