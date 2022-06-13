import credentials
import requests
import pprint
import shutil

temp = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={credentials.latitude}&lon={credentials.longitude}&appid={credentials.api_key}&units=metric").json()
pprint.pprint(temp)

# mapp = requests.get(f"https://tile.openweathermap.org/map/clouds_new/1/1/1.png?appid={credentials.api_key}")
r = requests.get(settings.STATICMAP_URL.format(**data), stream=True)
if r.status_code == 200:
    with open(path, 'wb') as f:
        r.raw.decode_content = True
        shutil.copyfileobj(r.raw, f)   