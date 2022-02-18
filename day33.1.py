
from ast import Num
import json
import requests

from unittest import result
import requests
import json
from datetime import datetime, time  
import time



my_lat = 40.712776
my_lng = -74.005974

def is_is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()



    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    print("Current ISS Longitude is " , iss_longitude)
    print("Current ISS Latitude is " , iss_longitude)
    

    # our Position is with in +/- 5 a

    if my_lat -5 <= iss_latitude <= my_lat +5 and my_lng -5 <= iss_longitude <= my_lng +5:

        return True


def is_night():

    parameter = {
        "lat": my_lat,
        "lng": my_lng,
        "formatted":0, 
    }




    response = requests.get ("https://api.sunrise-sunset.org/json", params= parameter)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split("T")[1].split(":")[:2]
    sunset =  data["results"]["sunset"].split("T")[1].split(":")[:2]

    timen_now = datetime.now().hour

    if timen_now >= sunset or timen_now <= sunrise:
        return True


while True:
    time.sleep(1024)
    if is_is_overhead() and is_night():
        print("ISS is Overhead")







