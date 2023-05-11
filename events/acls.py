import requests

def get_photo(city, state):
    headers = {
        "Authorization": "Bearer {PEXELS_API_KEY}" 
    }
    url = f"https://api.pexels.com/v1/search?query={city} {state} skyline&per_page=1"
    
    response = requests.get(url, headers=headers)
    data = response.json()
    
    if "photos" in data:
        photos = data["photos"]
        if len(photos) > 0:
            photo_url = photos[0]["src"]["medium"]
            return {"picture_url": photo_url}
    
    return {"picture_url": None}


def get_weather_data(city, state):
    geocoding_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid={OPEN_WEATHER_API_KEY}"  # Replace YOUR_API_KEY with your OpenWeatherMap API key
    
    geocoding_response = requests.get(geocoding_url)
    geocoding_data = geocoding_response.json()
    
    if geocoding_response.status_code == 200 and "coord" in geocoding_data:
        lat = geocoding_data["coord"]["lat"]
        lon = geocoding_data["coord"]["lon"]
        
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}"  # Replace YOUR_API_KEY with your OpenWeatherMap API key
        
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()
        
        if weather_response.status_code == 200 and "main" in weather_data and "weather" in weather_data:
            main_weather = weather_data["main"]
            weather_description = weather_data["weather"][0]["description"]
            
            return {"temperature": main_weather["temp"], "description": weather_description}
    
    return {"temperature": None, "description": None}
