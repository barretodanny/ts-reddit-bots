import requests
from config import read_config

##### TS-REDDIT API #####
ENDPOINT = "http://localhost:1337/api"
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


##### ANIME QUOTE API #####
anime_quote_api_profile = read_config("config.ini", "anime_quote_api")
ANIME_QUOTE_ENDPOINT = anime_quote_api_profile["url"]


def get_anime_quote():
    return requests.get(ANIME_QUOTE_ENDPOINT)


##### JOKE API #####
joke_api_profile = read_config("config.ini", "joke_api")
JOKE_API_ENDPOINT = joke_api_profile["url"]


def get_joke():
    return requests.get(JOKE_API_ENDPOINT)


##### CHUCK NORRIS JOKE API #####
chucknorris_joke_api_profile = read_config("config.ini", "chucknorris_joke_api")
CHUCKNORRIS_JOKE_ENDPOINT = chucknorris_joke_api_profile["url"]


def get_chucknorris_joke():
    return requests.get(CHUCKNORRIS_JOKE_ENDPOINT)


##### USELESS FACT API #####
useless_fact_api_profile = read_config("config.ini", "useless_fact_api")
USELESS_FACT_ENDPOINT = useless_fact_api_profile["url"]


def get_useless_fact():
    return requests.get(USELESS_FACT_ENDPOINT)


##### DAD JOKE API #####
dad_joke_api_profile = read_config("config.ini", "dad_joke_api")
DAD_JOKE_ENDPOINT = dad_joke_api_profile["url"]


def get_dad_joke():
    return requests.get(DAD_JOKE_ENDPOINT, headers={"Accept": "application/json"})


##### YO MAMA JOKE API #####
yomama_joke_api_profile = read_config("config.ini", "yomama_joke_api")
YOMAMA_JOKE_ENDPOINT = yomama_joke_api_profile["url"]


def get_yomama_joke():
    return requests.get(YOMAMA_JOKE_ENDPOINT)


##### POKEMON API #####
pokemon_api_profile = read_config("config.ini", "random_pokemon_api")
POKEMON_ENDPOINT = pokemon_api_profile["url"]


def get_random_pokemon(n):
    return requests.get(f"{POKEMON_ENDPOINT}{n}")
