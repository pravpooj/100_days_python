
import json
import requests
import sys 
import pandas
import re





url="https://sandboxapicdc.cisco.com/api/aaaLogin.json"


def login():
    
    payload = {
      "aaaUser": {
         "attributes": {
            "name":"admin",
            "pwd":"!v3G@!4@Y"
         }
      }
   }


    response = requests.post(url,data=json.dumps(payload),verify=False).json()

    token = response['imdata'][0]['aaaLogin']['attributes']['token']
    return token



def main():
    token = login()
    print("The token is: " + token)

main()
