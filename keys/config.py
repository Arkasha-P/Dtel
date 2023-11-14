#---Библиотеки-------------------------------------------------
import requests
import json
import csv


#---Переменные-------------------------------------------------

MAC_ADRESS= {
"mac_tep75_gates_1" :       "08:13:CD:00:07:D0",
"mac_tep75_gates_2" :       "08:13:CD:00:07:7F",
"mac_tep75_gates_3" :       "08:13:CD:00:02:30",

"mac_tep75_entrance_1" :    "08:13:CD:00:07:96",
"mac_tep75_entrance_2" :    "08:13:CD:00:07:85",

"mac_tep75_1_entrance_1" :  "08:13:CD:00:04:12",
"mac_tep75_1_entrance_2" :  "08:13:CD:00:07:77",

"mac_vin22_entrance_1" :    "08:13:CD:00:01:3D",
"mac_vin22_entrance_2" :    "08:13:CD:00:03:1C",

"mac_abr21_entrance_1" :    "08:13:CD:00:0F:B3",
"mac_abr21_entrance_2" :    "08:13:CD:00:0F:F3",

"mac_esa4_6_entranse_1" :   "08:13:CD:00:01:CD",
"mac_esa4_6_entranse_2" :   "08:13:CD:00:01:F9",
"mac_esa4_6_gates" :        "08:13:CD:00:0F:F5",

"mac_tep79_entranse_1" :    "08:13:CD:00:0F:B4",
"mac_tep79_entranse_2" :    "08:13:CD:00:0F:E9",
"mac_tep79_1_entranse_1" :  "08:13:CD:00:0F:BB",
"mac_tep79_1_entranse_2" :  "08:13:CD:00:0F:BF",

"mac_ovs67_entranse_1" :    "08:13:CD:00:0E:A2",
"mac_ovs67_entranse_2" :    "08:13:CD:00:0F:FC",

"mac_dja4b_entranse_1" :    "08:13:CD:00:0E:90",
"mac_hudak5_1_entranse_1":  "08:13:CD:00:0E:97",
"mac_hudak5_1_entranse_2":  "08:13:CD:00:11:43"
}

list_home = """Выберете дом (введите номер строки):
1) Тепличная 75
2) Тепличная 75/1
3) Виноградная 22/1В
4) Абрикосовая 21
5) Есауленко 4/6
6) Тепличная 79
7) Тепличная 79/1
8) Островского 67
9) Джапаридзе 4В
10) Худякова 5/1
"""

mac = str()
key = str()
keys = open(r"keys/keys.txt", 'r+')
apartment = str()
num_entrance = str() # Номер подезда
num_home = int()

Cookie = "PHPSESSID_TD_CRM=65r54f5l3r6ne8hpvsmfh27js3; _csrf=11319b03dd44ab191f63862cf53eb348ea36d7e773bb47d99df5f539ce7169e8a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22pN_pI8mSdIOpNKkEcMUyRxD2VbNMfWPH%22%3B%7D; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D"


#---Функции-------------------------------------------------

def set_tep75_gates():
    api_add_keys(MAC_ADRESS["mac_tep75_gates_1"],key,0,f" {key} калитка 1")
    api_add_keys(MAC_ADRESS["mac_tep75_gates_2"],key,0,f" {key} калитка 2")
    api_add_keys(MAC_ADRESS["mac_tep75_gates_3"],key,0,f" {key} калитка 3")

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
    
def cycle_keys(key,num_home,apartment):

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
