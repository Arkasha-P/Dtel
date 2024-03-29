"""
Скрипт по дабовлению ключей во все панели по адресу Абрикосовая 21 из файла  "txt/keys.txt"
"""

import requests
import json
from cfg.cfg import headers_crm, print_output


#---Переменные-------------------------------------------------

print("Введите номер квартиры: ", end = "") # выводи сообщение без новой строки 
apartment = int(input())

mac = ["08:13:CD:00:0F:B3","08:13:CD:00:0F:F3"]

with open("txt/keys.txt", "r") as f:
    file = f.readlines()

    for list_mac in mac:
        for list_key in file:

            url = f"https://crm.dtel.ru/front/device-keys/{list_mac}/create-key"

            payload = json.dumps({
            "value": list_key,
            "numberSystem": "16",
            "flatNum": apartment,
            "inner": "1"
            })

            response = requests.request("POST", url, headers=headers_crm, data=payload)


            print(list_mac)
            print_output(response, list_key)
        