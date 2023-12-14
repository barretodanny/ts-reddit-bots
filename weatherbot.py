from bot import *
from config import read_config
from datetime import datetime
from utils import parse_weather_data

# credentials for this bot
login_profile = read_config("config.ini", "weather_bot_login")
email = login_profile["email"]
password = login_profile["password"]

# attempt to log in bot
login_result = login(email, password)

# bot logged in, grab tokens
access_token = login_result["accessToken"]

# create post
# cities: Barrie, Toronto, Ottawa, NewYork, London, Paris, Sydney, Tokyo
# Seoul, Beijing, MexicoCity, SaoPaulo
today_date = datetime.now()
formatted_date = today_date.strftime("%A %B %d, %Y")
cities = [
    "Barrie",
    "Toronto",
    "Ottawa",
    "New York",
    "London",
    "Paris",
    "Sydney",
    "Tokyo",
    "Seoul",
    "Beijing",
    "Mexico City",
]

for city in cities:
    # fetch weather
    weather_req = get_city_weather(city)

    if weather_req.status_code != 200:
        print(f"Error fetching weather data for {city}.")
        continue

    # parse weather data
    weather_data = weather_req.text
    parsed_weather_data = parse_weather_data(weather_data)
    sky_condition = parsed_weather_data["sky_condition"]
    temp = parsed_weather_data["temp"]
    humidity = parsed_weather_data["humidity"]

    title = f"{city} Weather Forecast for {formatted_date}"
    content = (
        f"Sky conditions: {sky_condition}, temperature: {temp} °C, humidity: {humidity}"
    )
    subreddit_name = city.replace(" ", "")
    post_result = send_post(title, content, subreddit_name, access_token)
