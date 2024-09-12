import requests
import os
from dotenv import load_dotenv 
import json
load_dotenv()
city = 'Ho chi minh'
rsp = requests.get(f'http://api.weatherapi.com/v1/history.json?key={os.getenv("API_KEY")}&q={city}&dt=2024-09-11').json()

with open("weather.json", "w") as f:
    json.dump(rsp, f, indent=4)
name = rsp['location']['name']
country = rsp['location']['country']
localtime = rsp['location']['localtime']
print(f'City: {name}, Country: {country}, Local Time: {localtime}')