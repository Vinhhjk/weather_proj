import requests
import os
from dotenv import load_dotenv 
import json
from datetime import datetime, timedelta

load_dotenv()
city = 'Ho chi minh'
start_date = datetime(2024, 9,7)
end_date = datetime(2024,9,14)
current_date = start_date
while current_date <= end_date:
    date_str = current_date.strftime("%Y-%m-%d")

    rsp = requests.get(f'http://api.weatherapi.com/v1/history.json?key={os.getenv("API_KEY")}&q={city}&dt={date_str}').json()

    # Save each day's data to a separate JSON file
    with open(f"weather_{date_str}.json", "w") as f:
        json.dump(rsp, f, indent=4)
    name = rsp['location']['name']
    country = rsp['location']['country']
    localtime = rsp['location']['localtime']
    print(f'Date: {date_str}, City: {name}, Country: {country}, Local Time: {localtime}')

    # Move to the next day
    
    current_date += timedelta(days=1)