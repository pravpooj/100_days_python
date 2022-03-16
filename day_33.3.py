
from unittest import result
import requests
import json
from datetime import datetime, time  


my_lat = 40.712776
my_lng = -74.005974


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

print(sunrise[0],":",sunrise[1])
print(sunset[0],":", sunset[1])

timen_now = datetime.now()

print(timen_now)

