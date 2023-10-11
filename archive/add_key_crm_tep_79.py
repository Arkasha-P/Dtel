import requests
import json


#---Переменные-------------------------------------------------

mac_tep79_gates_1 = "" 
mac_tep79_gates_2 = ""
mac_tep79_gates_3 = ""

mac_tep79_entrance_1 = "08:13:CD:00:0F:B4"
mac_tep79_entrance_2 = "08:13:CD:00:0F:E9"

mac_tep79_1_entrance_1 = "08:13:CD:00:0F:BB"
mac_tep79_1_entrance_2 = ""

list_home = """Выберете дом (введите номер строки):
1) Тепличная 79
2) Тепличная 79/1"""

mac = str()
key = str()
file = open(r'txt/keys.txt', 'r')
apartment = str()
num_entrance = str() # Номер подезда

# num_home = int()
num_home = 1

# url = f"https://crm.dtel.ru/front/device-keys/{mac}/create-key"
Cookie = "PHPSESSID_TD_CRM=65r54f5l3r6ne8hpvsmfh27js3; _csrf=11319b03dd44ab191f63862cf53eb348ea36d7e773bb47d99df5f539ce7169e8a%3A2%3A%7Bi%3A0%3Bs%3A5%3A%22_csrf%22%3Bi%3A1%3Bs%3A32%3A%22pN_pI8mSdIOpNKkEcMUyRxD2VbNMfWPH%22%3B%7D; _identity=f236f7e09617f4beaf7878357688d69d7be7640c15935b049ca5fb38014c009da%3A2%3A%7Bi%3A0%3Bs%3A9%3A%22_identity%22%3Bi%3A1%3Bs%3A17%3A%22%5B20%2Cnull%2C2592000%5D%22%3B%7D"

#----ввод-данных-----------------------------------------------

print(list_home) # выводи сообщение без новой строки 
num_home = int(input())

print("Введите номер квартиры: ", end = "") # выводи сообщение без новой строки 
apartment = input()

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

    if "true" in response.text: print(f"OK - ключ добавлен - калитка 1 - {key}")
    else: print(response.status_code);print(response.text, " - калитка 1")

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

    if "true" in response.text: print(f"OK - ключ добавлен - калитка 2 - {key}")
    else: print(response.status_code);print(response.text, " - калитка 2")

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

    if "true" in response.text: print(f"OK - ключ добавлен - калитка 3 - {key}")
    else: print(response.status_code);print(response.text, " - калитка 3")

def entrance_1_79():
    
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

    if "true" in response.text: print(f"OK - ключ добавлен - Дом 75 - подезд 1 - {key}")
    else: print(response.status_code);print(response.text, " - 75 под. 1")

def entrance_2_79():
    
    mac = mac_tep79_entrance_2
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
    else: print(response.status_code);print(response.text, "75 под. 2")

def entrance_1_79_1():
    
    mac = mac_tep79_1_entrance_1
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
    else: print(response.status_code);print(response.text, "75/1 под. 1")

def entrance_2_79_2():
    
    mac = mac_tep79_1_entrance_2
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
    else: print(response.status_code);print(response.text, "75/1 под. 2")


for key in file:

    # gates_1()
    # gates_2()
    # gates_3()

    apartment = int(apartment)

    if num_home == 1:

        if 1 <= apartment <= 96: # 1 - 96 квартир
            entrance_1_79()

        elif 97 <= apartment <= 272: # 97 - 272 квартиры
            entrance_2_79()

    elif num_home == 2:

        if 1 <= apartment <= 96: # 1 - 96 квартир
            entrance_1_79_1()

        elif 97 <= apartment <= 272: # 97 - 272 квартиры
            entrance_2_79_2()

    else: print("Введите корректные данные")

print("Готово")
