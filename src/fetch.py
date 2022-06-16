import credentials
import requests

def fetch():
    temp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={credentials.latitude}&lon={credentials.longitude}&appid={credentials.api_key}&units=metric").json()
    return temp
