from db.mysql import *
import csv
import requests
import json
import os
import datetime
import time 

ip_panels = "192.168.10.228"

def get_mac(ip):
    url = f"http://{ip}/system/info"

    payload = {}
    headers = {
    'Authorization': 'Basic cm9vdDoxMjM0NTY='
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    response = response.json()
    print(response["mac"])





get_mac(ip_panels)