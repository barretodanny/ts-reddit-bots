import requests
from config import read_config

##### TS-REDDIT API #####
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


##### WEATHER API #####
weather_api_profile = read_config("config.ini", "weather_api")
WEATHER_ENDPOINT = weather_api_profile["url"]
WEATHER_API_KEY = weather_api_profile["key"]


def get_city_weather(city):
    return requests.get(f"{WEATHER_ENDPOINT}{city}&APPID={WEATHER_API_KEY}")


##### CAT FACT API #####
cat_fact_api_profile = read_config("config.ini", "cat_fact_api")
CAT_FACT_ENDPOINT = cat_fact_api_profile["url"]


def get_cat_fact():
    return requests.get(CAT_FACT_ENDPOINT)


##### DOG FACT API #####
dog_fact_api_profile = read_config("config.ini", "dog_fact_api")
DOG_FACT_ENDPOINT = dog_fact_api_profile["url"]


def get_dog_fact():
    return requests.get(DOG_FACT_ENDPOINT)
