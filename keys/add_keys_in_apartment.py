"""
Скрипт добавляет ключи в нужную квартиру с учетом особеностей дома и подъезда
"""

import requests
import json
from config import *

#----ввод-данных-----------------------------------------------

print(list_home) # выводи сообщение без новой строки 
num_home = int(input())

print("Введите номер квартиры: ", end = "") # выводи сообщение без новой строки 
apartment = int(input())

def api_add_keys(mac,key,apartment,name):
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

    if "true" in response.text: print(f"OK - ключ добавлен - {name} - {key}")
    else: print(response.status_code);print(response.text, f" - {name}")

def set_tep75_gates():
    api_add_keys(MAC_ADRESS["mac_tep75_gates_1"],key,0,"калитка 1")
    api_add_keys(MAC_ADRESS["mac_tep75_gates_2"],key,0,"калитка 2")
    api_add_keys(MAC_ADRESS["mac_tep75_gates_3"],key,0,"калитка 3")

for key in keys:

    # cycle_keys(key,num_home,apartment)
    
    if num_home == 1 and 1 <= apartment <= 96:
        api_add_keys(MAC_ADRESS["mac_tep75_entrance_1"],key,apartment,"Дом 75 - подъезд 1");set_tep75_gates()

    if num_home == 1 and 97 <= apartment <= 272:
        api_add_keys(MAC_ADRESS["mac_tep75_entrance_2"],key,apartment,"Дом 75 - подъезд 2");set_tep75_gates()

    if num_home == 2 and 1 <= apartment <= 96:
        api_add_keys(MAC_ADRESS["mac_tep75_1_entrance_1"],key,apartment,"Дом 75/1 - подъезд 1");set_tep75_gates()

    if num_home == 2 and 97 <= apartment <= 272:
        api_add_keys(MAC_ADRESS["mac_tep75_1_entrance_2"],key,apartment,"Дом 75/1 - подъезд 2");set_tep75_gates()

    if num_home == 3:
        api_add_keys(MAC_ADRESS["mac_vin22_entrance_1"],key,apartment,"Виноградная 22/1В подъезд 1")
        api_add_keys(MAC_ADRESS["mac_vin22_entrance_2"],key,apartment,"Виноградная 22/1В подъезд 2")

    if num_home == 4:
        api_add_keys(MAC_ADRESS["mac_abr21_entrance_1"],key,apartment,"Абрикосовая 21 подъезд 1")
        api_add_keys(MAC_ADRESS["mac_abr21_entrance_2"],key,apartment,"Абрикосовая 21 подъезд 2")
    
    if num_home == 5 and 1 <= apartment <= 123:
        api_add_keys(MAC_ADRESS["mac_esa4_6_entranse_1"],key,apartment,"Есауленко 4/6 подъезд 1")
        api_add_keys(MAC_ADRESS["mac_esa4_6_gates"],key,apartment,"Есауленко 4/6 калитка")
    
    if num_home == 5 and 124 <= apartment <= 270:
        api_add_keys(MAC_ADRESS["mac_esa4_6_entranse_2"],key,apartment,"Есауленко 4/6 подъезд 2")
        api_add_keys(MAC_ADRESS["mac_esa4_6_gates"],key,apartment,"Есауленко 4/6 калитка")
    
    if num_home == 6 and 1 <= apartment <= 96:
        api_add_keys(MAC_ADRESS["mac_tep79_entranse_1"],key,apartment,"Тепличная 79 - подъезд 1")

    if num_home == 6 and 97 <= apartment <= 272:
        api_add_keys(MAC_ADRESS["mac_tep79_entranse_2"],key,apartment,"Тепличная 79 - подъезд 2")

    if num_home == 7 and 1 <= apartment <= 96:
        api_add_keys(MAC_ADRESS["mac_tep79_1_entranse_1"],key,apartment,"Тепличная 79/1 - подъезд 1")

    if num_home == 7 and 97 <= apartment <= 272:
        api_add_keys(MAC_ADRESS["mac_tep79_1_entranse_2"],key,apartment,"Тепличная 79/1 - подъезд 2")
    
    if num_home == 8 and 1 <= apartment <= 44:
        api_add_keys(MAC_ADRESS["mac_ovs67_entranse_1"],key,apartment,"Островского 67 подъезд 1")
    
    if num_home == 8 and 66 <= apartment <= 109:
        api_add_keys(MAC_ADRESS["mac_ovs67_entranse_2"],key,apartment,"Островского 67 подъезд 2")

    if num_home == 8 and (45 <= apartment <= 65 or 110 <= apartment <=130):
        api_add_keys(MAC_ADRESS["mac_ovs67_entranse_1"],key,apartment,"Островского 67 подъезд 1")
        api_add_keys(MAC_ADRESS["mac_ovs67_entranse_1"],key,apartment,"Островского 67 подъезд 2")
    
    if num_home == 9:
        api_add_keys(MAC_ADRESS["mac_dja4b_entranse_1"],key,apartment,"Джапаридзе 4В подъезд 1")

    if num_home == 10 and 1 <= apartment <= 44:
        api_add_keys(MAC_ADRESS["mac_hudak5_1_entranse_1"],key,apartment,"Худякова 5/1 подъезд 1")
    
    if num_home == 10 and 45 <= apartment <= 88:
        api_add_keys(MAC_ADRESS["mac_hudak5_1_entranse_2"],key,apartment,"Худякова 5/1 подъезд 2")



with keys as f:
    f =  f.write(f"")
print("Готово")