import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 31.633980
MY_LONG = 74.872261


def check_overhead():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    lat = float(iss_response.json()["iss_position"]["latitude"])
    long = float(iss_response.json()["iss_position"]["longitude"])
    if MY_LAT - 5 < lat < MY_LAT + 5 and MY_LONG - 5 < long < MY_LONG + 5:
        return True


def is_night():
    parameters_sun = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
        "tzid": "Asia/Kolkata"
    }
    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters_sun)
    sun_response.raise_for_status()
    sunrise = int(sun_response.json()["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(sun_response.json()["results"]["sunset"].split("T")[1].split(":")[0])
    now = datetime.now().hour
    if now > sunset or now < sunrise:
        return True


while True:
    if check_overhead() and is_night():
        email = "sumitjaidka786@gmail.com"
        password = "gsai chlq kmav iali"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(email, password=password)
            connection.sendmail(from_addr=email, to_addrs="sumitatcultivatewill@yahoo.com",
                                msg="Subject:ISS is Overhead\n\n"
                                    "International Space Station is Overhead!!")
        time.sleep(60)
