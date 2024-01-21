import json


def parse_weather_data(weather_data):
    weather_data = json.loads(weather_data)
    sky_condition = weather_data["weather"][0]["description"]
    temp = round(weather_data["main"]["temp"] - 273.15, 2)
    humidity = weather_data["main"]["humidity"]

    return {"sky_condition": sky_condition, "temp": temp, "humidity": humidity}


def kelvin_to_celcius(kelvin):
    return kelvin - 273.15


def parse_cat_fact_data(cat_fact_data):
    cat_fact_data = json.loads(cat_fact_data)
    return cat_fact_data["fact"]


def parse_dog_fact_data(dog_fact_data):
    dog_fact_data = json.loads(dog_fact_data)
    return dog_fact_data["facts"][0]


def parse_anime_quote_data(anime_quote_data):
    anime_quote_data = json.loads(anime_quote_data)
    title = anime_quote_data["anime"]
    character = anime_quote_data["character"]
    quote = anime_quote_data["quote"]

    return (title, character, quote)


def parse_joke_data(joke_data):
    joke_data = json.loads(joke_data)
    return joke_data["joke"]


def parse_chucknorris_joke_data(chucknorris_joke_data):
    chucknorris_joke_data = json.loads(chucknorris_joke_data)
    return chucknorris_joke_data["value"]


def parse_useless_fact_data(useless_fact_data):
    useless_fact_data = json.loads(useless_fact_data)
    return useless_fact_data["text"]


def parse_dad_joke_data(dad_joke_data):
    dad_joke_data = json.loads(dad_joke_data)
    return dad_joke_data["joke"]


def parse_yomama_joke_data(yomama_joke_data):
    yomama_joke_data = json.loads(yomama_joke_data)
    return yomama_joke_data["joke"]


def parse_pokemon_data(pokemon_data):
    pokemon_data = json.loads(pokemon_data)
    return pokemon_data["species"]["name"]
