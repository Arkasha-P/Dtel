import requests
import json

#---Переменные-------------------------------------------------

mac_tep75_gates_1 = "08:13:CD:00:07:D0" 
mac_tep75_gates_2 = "08:13:CD:00:07:7F"
mac_tep75_gates_3 = "08:13:CD:00:02:30"

mac_tep75_entrance_1 = "08:13:CD:00:07:96"
mac_tep75_entrance_2 = "08:13:CD:00:07:85"

mac = str()
key = str()
file = open('keys.txt', 'r')
apartment = str()
num_entrance = str() # Номер подезда

url = f"https://crm.dtel.ru/front/device-keys/{mac}/create-key"
Cookie = "PHPSESSID_TD_CRM=65r54f5l3r6ne8hpvsmfh27js3; _csrf=11319b03dd44ab191f63862cf53eb348ea36d7e773bb47d99df5f539ce7169e8a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22pN_pI8mSdIOpNKkEcMUyRxD2VbNMfWPH%22%3B%7D; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D"

#----ввод-данных-----------------------------------------------

# print("Введите номер подезад: ", end = "") # выводи сообщение без новой строки 
# num_entrance = input()

print("Введите номер квартиры: ", end = "") # выводи сообщение без новой строки 
apartment = input()

# print("Введите ключ: ", end = "") # выводи сообщение без новой строки 
# key = input()

def gates_1():

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

    if response: print(f"OK - ключ добавлен - калитка 1 - {key}")
    else: print(response.status_code);print(response.text)

def gates_2():

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

    if response: print(f"OK - ключ добавлен - калитка 2 - {key}")
    else: print(response.status_code);print(response.text)

def gates_3():

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

    if response: print(f"OK - ключ добавлен - калитка 3 - {key}")
    else: print(response.status_code);print(response.text)

def entrance_1_75():
    
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

    if response: print(f"OK - ключ добавлен - подезд 1 - {key}")
    else: print(response.status_code);print(response.text)

def entrance_2_75():
    
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

    if response: print(f"OK - ключ добавлен - подезд - 2 - {key}", end = "")
    else: print(response.status_code);print(response.text)

for key in file:

    gates_1()
    gates_2()
    gates_3()

    apartment = int(apartment)

    if 1 <= apartment <= 96: # 1 - 96 квартир
        entrance_1_75()

    elif 97 <= apartment <= 272: # 97 - 272 квартиры
        entrance_2_75()

    else: print("Введите корректные данные")

print("Готово")