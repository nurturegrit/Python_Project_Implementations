import requests
from datetime import datetime
MY_LAT = 31.633980
MY_LONG = 74.872261
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Kolkata"
}
response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
sunrise = response.json()["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = response.json()["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise + "\n" + sunset + "\n" + f"{datetime.now().hour}")