from fuzzywuzzy import fuzz
import os
import csv
from db.mysql import get_houseuid_address
import json
import requests


os.system('clear')
n = 1
i = 0

streets = get_houseuid_address()

max_number = 30

def send_api(address, apartment, key):
    
    url = f"https://crm.dtel.ru/front/keys/create"

    payload = json.dumps({
    "values": [
        key
    ],
    "numberSystem": "16",
    "panelCode": apartment,
    "houseUid": address
    })

    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Basic QVBJX0Fya2FkeTpRYWVkNDIyISEh',
    'Cookie': 'PHPSESSID_TD_CRM=2ahncopu8d7878uv27p4bbmf99; _csrf=1a9b481a5e475988b41f5991c53739baf868885bb45cabe18e7b0f73f2d7810ca%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22gAY7alUi94lMxQxuacbWQeabjrBqpZjO%22%3B%7D; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D'
}

    requests.request("POST", url, headers=headers, data=payload)

with open("txt/street.csv", "r", newline="") as f:
    file = csv.reader(f)
    for row in file:
        for street_list in streets:

            row[0] = row[0].replace("улица","")
            row[0] = row[0].replace("д","")
            row[0] = row[0].replace(".","")
            row[0] = row[0].replace("корп","")
            row[0] = row[0].replace(",","")
            row[0] = row[0].replace("Сочи","")
            row[0] = row[0].replace("\\","")
            row[0] = row[0].replace("/","")

            ratio = fuzz.token_set_ratio(street_list,row[0])
            ratio = fuzz.ratio(street_list,row[0])
            i = i + 1


            if ratio > max_number:  # если текущее число больше предполагаемого максимального
                max_number = ratio
                origin_street = street_list[1]
                row1 = row[0]
            
            