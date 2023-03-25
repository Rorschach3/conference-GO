from .keys import PEXELS_API_KEY, OPEN_WEATHER_API_KEY
import json
import requests


def get_photo(city, state):
    url = "http://api.pexels.com/v1/search"
    headers = {"Authorization": PEXELS_API_KEY}
    params = {"per_page": 1, "query": city + " " + state}
    resp = requests.get(url, headers=headers, params=params)
    clue = json.loads(resp.content)
    try:
        return {"picture_url": clue["photos"][0]["src"]["original"]}
    except:
        return {"picture_url": None}


def get_weather(city, state):
    url = "http://api.openweathermap.org/geo/1.0/direct"
    params = {
        "q": city + "," + state + ",1",
        "limit": 1,
        "appid": OPEN_WEATHER_API_KEY,
    }
    resp = requests.get(url, params=params)
    clue = json.loads(resp.content)
    lat, lon = clue[0]["lat"], clue[0]["lon"]

    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": OPEN_WEATHER_API_KEY,
        "units": "imperial",
    }
    resp = requests.get(url, params=params)
    clue = json.loads(resp.content)
    try:
        return {
            "temp": clue["main"]["temp"],
            "description": clue["weather"][0]["description"],
        }
    except:
        return None
