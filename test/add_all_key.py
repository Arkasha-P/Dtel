import requests
import json
import time
import asyncio

#---Переменные-------------------------------------------------

mac_tep75_gates_1 = "08:13:CD:00:07:D0" 
mac_tep75_gates_2 = "08:13:CD:00:07:7F"
mac_tep75_gates_3 = "08:13:CD:00:02:30"

mac_tep75_entrance_1 = "08:13:CD:00:07:96"
mac_tep75_entrance_2 = "08:13:CD:00:07:85"

mac_tep75_1_entrance_1 = "08:13:CD:00:04:12"
mac_tep75_1_entrance_2 = "08:13:CD:00:07:77"

mac_gai5_5_entrance_1 = "08:13:CD:00:00:0C"

mac_vin22_1_entrance_1 = "08:13:CD:00:01:3D"
mac_vin22_1_entrance_2 = "08:13:CD:00:03:1C"

mac_panel_office = "08:13:CD:00:06:C4"

mac = str()
key = str()
file = open('keys.txt', 'r')
apartment = str()
num_entrance = str() # Номер подезда

num_home = int()

url = f"https://crm.dtel.ru/front/device-keys/{mac}/create-key"
Cookie = "PHPSESSID_TD_CRM=65r54f5l3r6ne8hpvsmfh27js3; _csrf=11319b03dd44ab191f63862cf53eb348ea36d7e773bb47d99df5f539ce7169e8a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22pN_pI8mSdIOpNKkEcMUyRxD2VbNMfWPH%22%3B%7D; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D"

#----ввод-данных-----------------------------------------------

print("Введите номер квартиры: ", end = "") # выводи сообщение без новой строки 
apartment = "1"

#----функции---------------------------------------------------
async def gates_1():

    apartment = "0"
    mac = mac_tep75_gates_1
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

    if "true" in response.text: print(f"OK - ключ добавлен - калитка 1 - {key}")
    else: print(response.text, end = "/"); print("калитка 1 - Тепличная 75", end = "\n")

async def gates_2():

    apartment = "0"
    mac = mac_tep75_gates_2
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

    if "true" in response.text: print(f"OK - ключ добавлен - калитка 2 - {key}")
    else: print(response.text, end = "/"); print("калитка 2 - Тепличная 75", end = "\n")

async def gates_3():

    apartment = "0"
    mac = mac_tep75_gates_3
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

    if "true" in response.text: print(f"OK - ключ добавлен - калитка 3 - {key}")
    else: print(response.text, end = "/"); print("калитка 3 - Тепличная 75", end = "\n")

async def entrance_1_75():
    
    mac = mac_tep75_entrance_1
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

    if "true" in response.text: print(f"OK - ключ добавлен - Дом 75 - подезд 1 - {key}")
    else: print(response.text, end = "/"); print("подезд 1 - Тепличная 75", end = "\n")

async def entrance_2_75():
    
    mac = mac_tep75_entrance_2
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

    if "true" in response.text: print(f"OK - ключ добавлен - Дом 75 - подезд - 2 - {key}")
    else: print(response.text, end = "/"); print("подезд 2 - Тепличная 75", end = "\n")

async def entrance_1_75_1():
    
    mac = mac_tep75_1_entrance_1
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

    if "true" in response.text: print(f"OK - ключ добавлен - Дом 75/1 - подезд 1 - {key}")
    else: print(response.text, end = "/"); print("подезд 1 - Тепличная 75/1", end = "\n")

async def entrance_2_75_2():
    
    mac = mac_tep75_1_entrance_2
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

    if "true" in response.text: print(f"OK - ключ добавлен - Дом 75/1 - подезд 2 - {key}")
    else: print(response.text, end = "/"); print("подезд 2 - Тепличная 75/1", end = "\n")

async def entrance_1_gaidara_5_5():
    
    mac = mac_gai5_5_entrance_1
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

    if "true" in response.text: print(f"OK - ключ добавлен - Гайдара 5/5 - подезд 1 - {key}")
    else: print(response.text, end = "/"); print("подезд 1 - Гайдара 5/5", end = "\n")

async def office_panel():
    
    mac = mac_panel_office
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

    if "true" in response.text: print(f"OK - ключ добавлен - Панель Оффис - {key}")
    else: print(response.text, end = "/"); print("Панель Оффис", end = "\n")

    time.sleep(1)

async def entrance_1_vinogradnai_22():
    
    mac = mac_vin22_1_entrance_1
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

    if "true" in response.text: print(f"OK - ключ добавлен - Виноградная 22 - подезд 1 - {key}")
    else: print(response.text, end = "/"); print("Виноградная 22 - подезд 1", end = "\n")

async def entrance_2_vinogradnai_22():
    
    mac = mac_vin22_1_entrance_2
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

    if "true" in response.text: print(f"OK - ключ добавлен - Виноградная 22 - подезд 2 - {key}")
    else: print(response.text, end = "/"); print("Виноградная 22 - подезд 2", end = "\n")

async def main():
    await asyncio.gather(
                        office_panel(),
                        gates_1(),
                        gates_2(),
                        # gates_3(),
                        entrance_1_75(),
                        entrance_2_75(),
                        entrance_1_75_1(),
                        entrance_2_75_2(),
                        entrance_1_gaidara_5_5(),
                        entrance_1_vinogradnai_22(),
                        entrance_2_vinogradnai_22()
                        )

for key in file:

    asyncio.run(main())

print("Готово - скрипт отработал")
