import credentials
import requests
# from datetime import datetime
# import pprint


def fetch():
    temp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={credentials.latitude}&lon={credentials.longitude}&appid={credentials.api_key}&units=metric").json()
    # pprint.pprint(temp)
    return temp

