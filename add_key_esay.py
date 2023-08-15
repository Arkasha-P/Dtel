import requests
import json
from cfg.cfg import headers_crm, print_output

#---Переменные-------------------------------------------------

key = open(r'C:\Users\sever\Documents\api_sokol\txt\keys.txt', 'r')

print("Введите номер квартиры: ", end = "") # выводи сообщение без новой строки 
apartment = int(input())

mac = ["08:13:CD:00:01:CD", "08:13:CD:00:01:F9"] # cd - 1 entrance 1-123 267-274; f9 - 2 entrance 124-266 275-285

if 1 <= apartment <= 123 or 267 <= apartment <= 274: # 1 - 96 квартир
    mac = mac[0]

elif 124 <= apartment <= 266 or 275 <= apartment <= 285: # 97 - 272 квартиры
    mac = mac[1]

else: print("Введите корректные данные")

for list_key in key:

    url = f"https://crm.dtel.ru/front/device-keys/{mac}/create-key"

    payload = json.dumps({
    "value": list_key,
    "numberSystem": "16",
    "flatNum": apartment,
    "inner": "1"
    })

    response = requests.request("POST", url, headers=headers_crm, data=payload)

    print_output(response, list_key)