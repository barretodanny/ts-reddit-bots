import json


def parse_weather_data(weather_data):
    weather_data = json.loads(weather_data)
    sky_condition = weather_data["weather"][0]["description"]
    temp = round(weather_data["main"]["temp"] - 273.15, 2)
    humidity = weather_data["main"]["humidity"]

    return {"sky_condition": sky_condition, "temp": temp, "humidity": humidity}


def kelvin_to_celcius(kelvin):
    return kelvin - 273.15
