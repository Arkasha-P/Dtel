"""
Добавление ключей в crm из файла keys.csv (пока Тепличный 79)
"""
import csv
import requests
import json

file = r"txt/keys.csv"

with open(file, newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[1])


def send_api(apartment, key):
    mac = mac_tep79_entrance_1
    url = f"https://crm.dtel.ru/front/device-keys/{mac}/create-key"

    payload = json.dumps({
    "value": key,
    "numberSystem": "16",
    "flatNum": apartment,
    "inner": "1"
    })
    headers = {
    'Cookie': Cookie,
    'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    if "true" in response.text: print(f"OK - ключ добавлен - Дом 79 - подезд 1 - {key}")
    else: print(response.status_code);print(response.text, " - 79 под. 1")